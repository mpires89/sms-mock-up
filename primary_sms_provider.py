from sms_provider_base import SMSProviderBase

class PrimarySMSProvider(SMSProviderBase):
    """Implementação principal (ex: Provedor mais rápido/confiável)."""
    def enviar_sms(self, telefone: str, mensagem: str) -> str:
        return f"SMS enviado via Provedor Primário para {telefone}: {mensagem}"