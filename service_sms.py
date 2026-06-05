
from primary_sms_provider import PrimarySMSProvider
from secondary_sms_provider import SecondarySMSProvider

class ServicoSMS:
    """Classe de serviço que decide a estratégia de envio no momento do instanciamento."""
    def __init__(self, tipo_provedor: str):
        match tipo_provedor.lower():
            case "primary":
                self.provedor = PrimarySMSProvider()
            case "secondary":
                self.provedor = SecondarySMSProvider()
            case _:
                raise ValueError(f"Provedor indefinido ou inválido: '{tipo_provedor}'")

    def disparar(self, telefone: str, mensagem: str) -> str:
        return self.provedor.enviar_sms(telefone, mensagem)