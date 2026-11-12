def saudacao():
    print ("\nBem-vindo !")

def classificar_mensagem(texto):
    texto = texto.lower()

    if "obrigado" in texto:
        return "Elogio"
    elif "problema" in texto or "quebrado" in texto or "insatisfeito" in texto:
        return "Reclamação"
    elif "gostaria de saber" in texto:
        return "Dúvida"
    elif "solicito" in texto:
        return "Solicitação"
    else:
        return "Ainda não identificada"  
if __name__ == "__main__":
    saudacao()

    print ("\n===CLASSIFICADOR DE MENSAGENS ===")

    while True:
     mensagem = input("\nDigite sua mensagem (ou 'sair' para encerrar): ")
     if mensagem.lower() == "sair":
      print("Programa encerrado!")
      break
     if not mensagem.strip():
      print("\nAtenção! Por favor, digite uma mensagem.")
      continue
     resultado = classificar_mensagem(mensagem)
     print("Mensagem Recebida:", mensagem)
     print("Classificação:", resultado)
 