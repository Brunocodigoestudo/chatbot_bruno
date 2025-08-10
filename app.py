import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.3-70b-versatile')


def resposta_do_bot(lista_mensagens):
  template = ChatPromptTemplate.from_messages(
      [('system', 'Você é um assistente amigável chamado Asimo')] +
      lista_mensagens
  )
  chain = template | chat
  return chain.invoke({}).content

print('Bem-vindo ao ChatBot da Asimo! (Digite x se você quiser sair!)\n')
mensagens = []
while True:
  pergunta = input('Você pode perguntar ?: ')
  if pergunta.lower() == 'x':
    break
  mensagens.append(('user', pergunta))
  resposta = resposta_do_bot(mensagens)
  mensagens.append(('assistant', resposta))
  print(f'Bot: {resposta}')

print('\nMuito obrigado por utilizar o AsimoBot!')
