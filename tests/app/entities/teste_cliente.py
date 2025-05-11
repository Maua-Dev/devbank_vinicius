import pytest
from src.app.entities.cliente import Cliente
from src.app.errors.entity_errors import ParamNotValidated

class Test_Cliente:
    def test_cliente(self):
        cliente = Cliente("victor", "1234", "12345-6", 1000.0)
        assert cliente.name == "victor"
        assert cliente.agency == "1234"
        assert cliente.account == "12345-6"
        assert cliente.current_balance == 1000.0

    def test_cliente_dict(self):
        cliente = Cliente("victor", "1234", "12345-6", 1000.0)
        assert cliente.to_dict() == {'name': 'victor', 'agency': '1234', 'account': '12345-6', 'current_balance': 1000.0}

    def test_name_is_none(self):
        with pytest.raises(ParamNotValidated):
            Cliente(agency="1234", account="12345-6", current_balance=1000.0)

    def test_name_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name = 1.0, agency="1234", account="12345-6", current_balance=1000.0)

    def test_name_is_too_short(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name = "vi", agency="1234", account="12345-6", current_balance=1000.0)

    def test_agency_is_none(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name = "victor", account= "12345-6", current_balance=1000.0)

    def test_agency_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name = "victor", agency=1.0, account="12345-6", current_balance=1000.0)
    
    def test_agency_is_not_four_digits(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name = "victor", agency="123", account="12345-6", current_balance=1000.0)

    def test_account_is_none(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name = "victor", agency="1234", current_balance=1000.0)

    def test_account_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name = "victor", agency="1234", account=1.0, current_balance=1000.0)
            
    def test_account_is_not_formatted_correctly(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name = "victor", agency="1234", account="123456", current_balance=1000.0)

    def test_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name = "victor", agency="1234", account="12345-6")
    
    def test_account_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name = "victor", agency="1234", account="12345-6", current_balance="1000.0")

    def test_account_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Cliente(name = "victor", agency="1234", account="12345-6", current_balance=-1.0)  