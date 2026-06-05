from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from service_sms import ServicoSMS

app = FastAPI(title="SMS Service API", description="API para envio de SMS.")

class SMSRequest(BaseModel):
    telefone: str
    mensagem: str
    provedor: str = "primary"

class SMSResponse(BaseModel):
    status: str
    detalhe: str

@app.post("/enviar-sms", response_model=SMSResponse)
def enviar_sms(request: SMSRequest):
    try:
        servico = ServicoSMS(request.provedor)
        resultado = servico.disparar(request.telefone, request.mensagem)
        return SMSResponse(status="sucesso", detalhe=resultado)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except NotImplementedError:
        raise HTTPException(status_code=500, detail="Provedor não implementado corretamente.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
