import pytest
from BankAccount import BankAccount

def test_deposit():
    account = BankAccount("John Doe", 100)
    account.deposit(50)
    assert account.balance == 150

def test_withdraw():
    account = BankAccount("Jane Doe", 200)
    account.withdraw(50)
    assert account.balance == 150

def test_transfer():
    account1 = BankAccount("John", 300)
    account2 = BankAccount("Jane", 100)
    account1.transfer(account2, 100)
    assert account1.balance == 200
    assert account2.balance == 200

def test_insufficient_balance():
    account = BankAccount("John Doe", 100)
    with pytest.raises(ValueError):
        account.withdraw(150)

def test_negative_initial_balance():
    with pytest.raises(ValueError):
        BankAccount("Invalid", -50)

