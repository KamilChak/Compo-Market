from decimal import Decimal
import hashlib
import json
from time import time
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from authenticate.models import Composter, Greener
from blockchain.models import Transaction

class Blockchain:

    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='0')

    def create_block(self, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True, cls=DjangoJSONEncoder).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def get_previous_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        transaction = Transaction.objects.create(
            sender=sender,
            recipient=recipient,
            amount=amount
        )
        transaction.save()

    def mine_block(self):
        previous_block = self.get_previous_block
        previous_hash = self.hash(previous_block)
        block = self.create_block(previous_hash)
        return block

    def get_chain(self):
        chain = []
        for block in self.chain:
            chain.append({
                'index': block['index'],
                'timestamp': block['timestamp'],
                'transactions': block['transactions'],
                'previous_hash': block['previous_hash'],
            })
        return chain


blockchain = Blockchain()

@csrf_exempt
def transaction(request):
    composter_id = request.POST['composter_id']
    greener_id = request.POST['greener_id']
    amount = Decimal(request.POST['amount'])
    composter = Composter.objects.get(id=composter_id)
    greener = Greener.objects.get(id=greener_id)
    blockchain.add_transaction(composter.id, greener.id, amount)
    block = blockchain.mine_block()
    greener.wallet += amount
    greener.save()
    response = {
        'message': f'Transaction successful! {amount} credits added to greener wallet.',
        'block': block
    }
    return JsonResponse(response)


@csrf_exempt
def display_chain(request):
    chain = blockchain.get_chain()
    request = {
        'chain': chain,
    }
    return JsonResponse(request)
