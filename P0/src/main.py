print ("===CLASSIFICADOR DE MENSAGENS ===")

mensagem = input("Digite sua mensagem: ")
print("Mensagem recebida:", mensagem)

if "obrigado" in mensagem.lower():
    print ("Classificação: Elogio")
elif "problema" in mensagem.lower():
    print ("Classificação: Reclamação")
elif "gostaria de saber" in mensagem.lower():
    print ("Classificação: Dúvida") 
elif "solicito" in mensagem.lower():
    print ("Classificação: Solicitação")       
else:
    print ("Classificação: Ainda não identificada")