from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..entities.client import Client

class ClientRepository(ABC):
    
    
    @abstractmethod
    def get_all_clients(self) -> List[Client]:
        '''
        Returns all clients in the database 
        '''
        pass
    
    @abstractmethod
    def get_client(self, client_id: str) -> Optional[Client]:
        '''
        Returns the client with the given account.
        If the item does not exist, returns None
        '''
        pass
    
    @abstractmethod
    def create_client(self, client: Client, client_id: str) -> Client:
        '''
        Creates a new client in the database
        '''
        pass
    
    @abstractmethod
    def delete_client(self, client_id: str) -> Client:
        '''
        Deletes the client with the given client_id.
        If the client does not exist, returns None
        '''
        
    @abstractmethod
    def update_client(self, client_id:str, name:str=None, agency:str=None, account:str=None, current_balance:float=None) -> Client:
        '''
        Updates the client with the given client_id.
        If the client does not exist, returns None
        '''
        pass