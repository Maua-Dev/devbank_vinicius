from typing import Dict, Optional, List

from ..entities.transaction import Transaction
from .transaction_repository_interface import TransacitonRepository
from src.app.enums.transaction_type_enum import Transaction_type

class TransactionRepositoryMock(TransacitonRepository):
    transactions: Dict[int, Transaction]
    
    def __init__(self):
        self.transactions = {
            1: Transaction(type=Transaction_type.WITHDRAW, value= 100.0, current_balance=1000.0, timestamp=12345.000),
            2: Transaction(type=Transaction_type.DEPOSIT, value= 50.0, current_balance=1500.0, timestamp=98765.220),
            3: Transaction(type=Transaction_type.WITHDRAW, value= 2.0, current_balance=5000.0, timestamp=555555.555),
            4: Transaction(type=Transaction_type.DEPOSIT, value= 200.0, current_balance=500.0, timestamp= 1122334455.000)
        }

    def get_all_transactionss(self) -> List[Transaction]:
        return self.transactions.values()
    
    def get_transactions(self, transaction_id: str) -> Optional[Transaction]:
        return self.transactions.get(transaction_id, None)
    
    def create_transactions(self, transactions: Transaction, transaction_id: str) -> Transaction:
        
        self.transactions[transaction_id] = transactions
        return transactions
    
    def delete_transactions(self, transaction_id: str) -> Transaction:
        transactions = self.transactions.pop(transaction_id, None)
        return transactions
        
        
    def update_transactions(self, transaction_id:str, type=Transaction_type, value:float=None, current_balance:float=None, timestamp:float=None) -> Transaction:
        transaction = self.transactions.get(transaction_id, None)
        if transaction is None:
            return None
        
        if type is not None:
            transaction.type = type
        if value is not None:
            transaction.value = value
        if current_balance is not None:
            transaction.current_balance = current_balance
        if timestamp is not None:
            transaction.timestamo = timestamp
        self.transaction[transaction_id] = transaction
        
        return transaction