import pytest
from src.app.entities.transacao import Transacao
from src.app.errors.entity_errors import ParamNotValidated

class Test_Transacao:
    def test_transacao(self):
        transacao = Transacao("deposit", 100.0, 20.0, 12345.6789)
        assert transacao.type == "deposit"
        assert transacao.value == 100.0
        assert transacao.current_balance == 1000.0
        assert transacao.timestamp == 12345.6789

    def test_transacao_dict(self):
        transacao = Transacao("deposit", 100.0, 1000.0, 12345.6789)
        assert transacao.to_dict() == {'type': 'deposit', 'value': 100.0, 'current_balance': 1000.0, 'timestamp' : 12345.6789}
           
    def test_type_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transacao(value = 100.0, current_balance= 1000.0, timestamp= 12345.6789)

    def test_type_is_not_deposit_or_withdraw(self):
        with pytest.raises(ParamNotValidated):
            Transacao(type="test", value = 100.0, current_balance= 1000.0, timestamp= 12345.6789)

    def test_value_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transacao(type="deposit", current_balance= 1000.0, timestamp= 12345.6789)

    def test_value_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transacao(type="deposit", value = "100.0", current_balance= 1000.0, timestamp= 12345.6789)

    def test_value_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Transacao(type="deposit",value = -1.0, current_balance= 1000.0, timestamp= 12345.6789)

    def test_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transacao(type="deposit", value = 100.0, timestamp= 12345.6789)

    def test_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transacao(type="deposit", value = 100.0,current_balance="1000.0", timestamp= 12345.6789)

    def test_current_balance_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Transacao(type="deposit", value = 100.0, current_balance=-1000.0, timestamp= 12345.6789)

    def test_timestamp_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transacao(type="deposit", value = 100.0, current_balance=1000.0)

    def test_timestamp_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transacao(type="deposit", value = 100.0, current_balance=1000.0, timestamp="12345.6789")

    def test_timestamp_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Transacao(type="deposit", value = 100.0, current_balance=1000.0, timestamp=-12345.6789)