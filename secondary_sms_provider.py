from sms_provider_base import SMSProviderBase

class SecondarySMSProvider(SMSProviderBase):
    """Implementação secundária (ex: Provedor de backup/mais barato)."""
    def enviar_sms(self, telefone: str, mensagem: str) -> str:
        return f"SMS enviado via Provedor Secundário para {telefone}: {mensagem}"