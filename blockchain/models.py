from django.db import models
from django.utils import timezone

from authenticate.models import Composter,Greener


class Transaction(models.Model):
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.sender} sent {self.amount} credits to {self.recipient}"


class Block(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    previous_hash = models.CharField(max_length=100)
    hash = models.CharField(max_length=100)
    nonce = models.IntegerField()
    
    def __str__(self):
        return f"Block {self.id}"
    
    def extract_transactions(self):
        transactions = []
        for transaction in self.transactions:
            sender = Composter.objects.get(id=transaction['sender'])
            recipient = Greener.objects.get(id=transaction['recipient'])
            amount = transaction['amount']
            transactions.append(Transaction(sender=sender.orgName, recipient=recipient.firstName, amount=amount))
        return transactions
