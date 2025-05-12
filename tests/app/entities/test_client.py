import pytest
from src.app.entities.client import Client
from src.app.errors.entity_errors import ParamNotValidated
import re

class Test_Client:
    def test_client(self):
        client = Client("victor", "1234", "12345-6", 1000.0)
        assert client.name == "victor"
        assert client.agency == "1234"
        assert client.account == "12345-6"
        assert client.current_balance == 1000.0

    def test_client_dict(self):
        client = Client("victor", "1234", "12345-6", 1000.0)
        assert client.to_dict() == {'name': 'victor', 'agency': '1234', 'account': '12345-6', 'current_balance': 1000.0}

    def test_name_is_none(self):
        with pytest.raises(ParamNotValidated):
            Client(agency="1234", account="12345-6", current_balance=1000.0)

    def test_name_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            Client(name = 1.0, agency="1234", account="12345-6", current_balance=1000.0)

    def test_name_is_too_short(self):
        with pytest.raises(ParamNotValidated):
            Client(name = "vi", agency="1234", account="12345-6", current_balance=1000.0)

    def test_agency_is_none(self):
        with pytest.raises(ParamNotValidated):
            Client(name = "victor", account= "12345-6", current_balance=1000.0)

    def test_agency_is_not_four_digits(self):
        with pytest.raises(ParamNotValidated):
            Client(name = "victor", agency="123", account="12345-6", current_balance=1000.0)

    def test_account_is_none(self):
        with pytest.raises(ParamNotValidated):
            Client(name = "victor", agency="1234", current_balance=1000.0)
            
    def test_account_is_not_formatted_correctly(self):
        with pytest.raises(ParamNotValidated):
            Client(name = "victor", agency="1234", account="123456", current_balance=1000.0)

    def test_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            Client(name = "victor", agency="1234", account="12345-6")
    
    def test_account_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Client(name = "victor", agency="1234", account="12345-6", current_balance="1000.0")

    def test_account_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Client(name = "victor", agency="1234", account="12345-6", current_balance=-1.0)  