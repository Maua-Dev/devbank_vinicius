from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from src.app.enums.transaction_type_enum import Transaction_type

from ..entities.transaction import Transaction

class TransacitonRepository(ABC):
    
    
    @abstractmethod
    def get_all_transactions(self) -> List[Transaction]:
        '''
        Returns all transactions in the database 
        '''
        pass
    
    @abstractmethod
    def get_transactions(self, transaction_id: str) -> Optional[Transaction]:
        '''
        Returns the transactions with the given id.
        If the transactions does not exist, returns None
        '''
        pass
    
    @abstractmethod
    def create_transactions(self, transaction: Transaction, transaction_id: str) -> Transaction:
        '''
        Creates a new transaction in the database
        '''
        pass
    
    @abstractmethod
    def delete_transaction(self, transaction_id: str) -> Transaction:
        '''
        Deletes the transaction with the given transaction_id.
        If the transaction does not exist, returns None
        '''
        
    @abstractmethod
    def update_transaction(self, transaction_id:str, type:Transaction_type=None, value:float=None, current_balance:float=None, timestamp: float=None) -> Transaction:
        '''
        Updates the transaction with the given transaction_id.
        If the transaction does not exist, returns None
        '''
        pass