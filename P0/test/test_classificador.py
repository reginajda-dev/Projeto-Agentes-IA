import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from main import classificar_mensagem

def test_reclamacao():
    resultado = classificar_mensagem("Meu produto chegou quebrado")
    assert resultado == "Reclamação"


def test_elogio():
    resultado = classificar_mensagem("Muito obrigado pelo atendimento")
    assert resultado == "Elogio"



def test_duvida():
    resultado = classificar_mensagem("Gostaria de saber o prazo de entrega")
    assert resultado == "Dúvida"



def test_solicitacao():
    resultado = classificar_mensagem("Solicito a segunda via do boleto")
    assert resultado == "Solicitação"



def test_mensagem_desconhecida():
    resultado = classificar_mensagem("O céu está azul hoje")
    assert resultado == "Ainda não identificada"



def test_mensagem_vazia():
    resultado = classificar_mensagem("")
    assert resultado == "Ainda não identificada"



def test_letras_maiusculas():
    resultado = classificar_mensagem("MUITO OBRIGADO PELO ATENDIMENTO")
    assert resultado == "Elogio"

