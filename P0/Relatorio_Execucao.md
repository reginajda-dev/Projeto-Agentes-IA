# Relatório de Execução - P0

## Projeto 
Classificador de mensagens com Python e LLM.

## Evolução por nível

 ### Nível Básico 
  Em desenvolvimento.

## Decisões principais

  ### Decisão 1 - Problema  escolhido
Desenvolver um classificador de mensagens utilizando Python e um modelo de linguagem (LLM).

  ### Público-alvo 
 Pessoas que recebem mensagens de diferentes assuntos e precisam organizá-las.

  ### Entrada 
 Uma mensagem de texto digitada pelo usuário no terminal.

  ### Saída
 Uma categoria que identifica o assunto da mensagem.

  ### Justificativa
 O uso de um LLM permite interpretar o significado das mensagens, mesmo quando são escritas de maneiras diferentes.

  ### Alternativa considerada
 Utilizar palavras-chaves para identificar as categorias.

  ### Motivo da escolha 
 O LLM pode interpretar o contexto das mensagens, enquanto uma classificação baseada apenas em palavras-chaves é mais limitada. 

## Registro de implementação - Etapa preparatória 

  ### Classificador inicial
  Foi desenvolvido um classificador de mensagens em Python, utilizando regras baseadas em palavras-chave.

  O programa recebe mensagens pelo terminal e retorna uma das seguintes classificações:
- Elogio
- Reclamação
- Dúvida 
- Solicitação 
- Ainda não identificada

### Testes automatizados 
Foram implementados 7 testes automatizados com pytest.
Resultado da execução: 7 testes aprovados.
Os testes verificam as categorias de mensagens, além de:
mensagens vazias, mensagens não identificadas e o tratamento de letras maiúsculas.

### Situação atual
O classificador baseado em palavras-chave está funcional.

A integração com uma API de modelo de linguagem (LLM) ainda não foi implementada.

O Nível Básico do P0 permanece em desenvolvimento.