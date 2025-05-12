import pytest
from src.app.entities.transaction import Transaction
from src.app.errors.entity_errors import ParamNotValidated
from src.app.enums.transaction_type_enum import Transaction_type

class Test_Transaction:
    def test_transaction(self):
        transaction = Transaction(Transaction_type.DEPOSIT, 100.0, 1000.0, 12345.6789)
        assert transaction.type == Transaction_type.DEPOSIT
        assert transaction.value == 100.0
        assert transaction.current_balance == 1000.0
        assert transaction.timestamp == 12345.6789

    def test_transaction_dict(self):
        transaction = Transaction(Transaction_type.DEPOSIT, 100.0, 1000.0, 12345.6789)
        assert transaction.to_dict() == {'type': 'Deposit', 'value': 100.0, 'current_balance': 1000.0, 'timestamp' : 12345.6789}
           
    def test_type_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value = 100.0, current_balance= 1000.0, timestamp= 12345.6789)

    def test_type_is_not_enum(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type= "Deposit", value = 100.0, current_balance= 1000.0, timestamp= 12345.6789)

    def test_value_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=Transaction_type.DEPOSIT, current_balance= 1000.0, timestamp= 12345.6789)

    def test_value_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=Transaction_type.DEPOSIT, value = "100.0", current_balance= 1000.0, timestamp= 12345.6789)

    def test_value_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=Transaction_type.DEPOSIT,value = -1.0, current_balance= 1000.0, timestamp= 12345.6789)

    def test_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=Transaction_type.DEPOSIT, value = 100.0, timestamp= 12345.6789)

    def test_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=Transaction_type.DEPOSIT, value = 100.0,current_balance="1000.0", timestamp= 12345.6789)

    def test_current_balance_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=Transaction_type.DEPOSIT, value = 100.0, current_balance=-1000.0, timestamp= 12345.6789)

    def test_timestamp_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=Transaction_type.DEPOSIT, value = 100.0, current_balance=1000.0)

    def test_timestamp_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=Transaction_type.DEPOSIT, value = 100.0, current_balance=1000.0, timestamp="12345.6789")

    def test_timestamp_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=Transaction_type.DEPOSIT, value = 100.0, current_balance=1000.0, timestamp=-12345.6789)