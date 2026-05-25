class SMSProviderBase:
    """Classe base que define a interface para envio de SMS."""
    
    def enviar_sms(self, telefone: str, mensagem: str) -> str:
        raise NotImplementedError("As subclasses devem implementar o método 'enviar_sms'")