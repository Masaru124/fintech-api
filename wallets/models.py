from django.db import models

class Wallet(models.Model):
    user = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Wallet({self.user})"

class Transaction(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    sender = models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name='sent_transactions')
    receiver = models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name='received_transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction from {self.sender.user} to {self.receiver.user}: ${self.amount}"

