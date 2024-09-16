import pytest
from banco.models.conta import Conta

@pytest.fixture
def conta_valida():
    return  Conta(123,456)

def test_validando_atributo_numero_conta(conta_valida):
    assert conta_valida.numero_conta == 123

def test_validando_atributo_agencia(conta_valida):
    assert conta_valida.agencia == 456

def test_validando_atributo_saldo(conta_valida):
    assert conta_valida._saldo == 0

def test_depositar_valor_positivo(conta_valida):
    conta_valida.depositar(100)
    assert conta_valida._saldo == 100

def test_sacar_valor_positivo_com_saldo_suficiente(conta_valida):
    conta_valida.depositar(100)
    conta_valida.sacar(50)
    assert conta_valida._saldo == 50

