from typing import Dict, Optional, List

from ..entities.client import Client
from .client_repository_inteface import ClientRepository


class ClientRepositoryMock(ClientRepository):
    clients: Dict[int, Client]
    
    def __init__(self):
        self.clients = {
            1: Client(name="Victor", agency="1234", account="12345-6", current_balance=4000.0),
            2: Client(name="Luiz", agency="9876", account="00000-0", current_balance=3000.0),
            3: Client(name="Vinicius", agency="5555", account="04321-5", current_balance=2000.0),
            4: Client(name="Fernando", agency="0000", account="22222-2", current_balance=1000.0)
        }

    def get_all_clients(self) -> List[Client]:
        return self.clients.values()
    
    def get_client(self, client_id: str) -> Optional[Client]:
        return self.clients.get(client_id, None)
    
    def create_client(self, client: Client, client_id: str) -> Client:
        
        self.clients[client_id] = client
        return client
    
    def delete_client(self, client_id: str) -> Client:
        client = self.clients.pop(client_id, None)
        return client
        
        
    def update_client(self, client_id:str, name:str=None, agency:str=None, account:str=None, current_balance:float=None) -> Client:
        client = self.clients.get(client_id, None)
        if client is None:
            return None
        
        if name is not None:
            client.name = name
        if agency is not None:
            client.agency = agency
        if account is not None:
            client.account = account
        if current_balance is not None:
            client.current_balance = current_balance
        self.clients[client_id] = client
        
        return client