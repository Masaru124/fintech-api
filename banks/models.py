from django.db import models
from users.models import User

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bank_accounts')
    account_number = models.CharField(max_length=20, unique=True)
    bank_name = models.CharField(max_length=100)
    simulated_balance = models.DecimalField(max_digits=12, decimal_places=2, default=10000.0)  # Mocked

    def __str__(self):
        return f"{self.bank_name} - {self.account_number}"
