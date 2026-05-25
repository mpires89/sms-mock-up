import pytest
from sample.service_sms import ServicoSMS
from sample.sms_provider_base import SMSProviderBase

def test_deve_enviar_via_provedor_primario():
    servico = ServicoSMS("primary")
    
    resultado = servico.disparar("11999999999", "Olá, este é um teste primário!")
    
    assert "Provedor Primário" in resultado
    assert "11999999999" in resultado


    servico = ServicoSMS("secondary")
    
    resultado = servico.disparar("11888888888", "Olá, este é um backup!")
    
    assert "Provedor Secundário" in resultado
    assert "11888888888" in resultado


def test_deve_lancar_excecao_quando_provedor_for_indefinido():
    with pytest.raises(ValueError) as erro_info:
        ServicoSMS("invalid_provider")
    
    assert "Provedor indefinido ou inválido" in str(erro_info.value)


def test_classe_base_deve_lancar_not_implemented_error():
    classe_base = SMSProviderBase()
    
    with pytest.raises(NotImplementedError):
        classe_base.enviar_sms("123", "teste")