import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Verificar se a chave da API foi carregada
if not os.getenv('GROQ_API_KEY'):
    st.error("❌ Erro: GROQ_API_KEY não encontrada no arquivo .env")
    st.stop()

# Inicializar o modelo de IA
chat = ChatGroq(model='llama-3.3-70b-versatile')

# Função para obter resposta do bot
def resposta_do_bot(pergunta):
    system_message = 'Você é um assistente amigável chamado ChatBot (Davi)'
    template = ChatPromptTemplate.from_messages([
        ('system', system_message),
        ('user', pergunta)
    ])
    chain = template | chat
    return chain.invoke({}).content

# Interface com Streamlit
st.title("🤖 ChatBot (Davi) - Seu Assistente Virtual")

# Inicializar o estado da sessão para a pergunta atual e resposta
if "pergunta_atual" not in st.session_state:
    st.session_state.pergunta_atual = None
    
if "resposta_atual" not in st.session_state:
    st.session_state.resposta_atual = None

# Campo de entrada para o usuário
pergunta = st.chat_input("Digite sua pergunta...")

if pergunta:
    # Atualizar a pergunta atual
    st.session_state.pergunta_atual = pergunta
    
    try:
        # Obter resposta do bot
        resposta = resposta_do_bot(pergunta)
        st.session_state.resposta_atual = resposta
    except Exception as e:
        st.error(f"❌ Erro ao obter resposta: {str(e)}")
        st.session_state.resposta_atual = "Desculpe, ocorreu um erro. Tente novamente."
    
# Exibir apenas a conversa atual, se existir
if st.session_state.pergunta_atual:
    st.chat_message("user").write(st.session_state.pergunta_atual)
    
if st.session_state.resposta_atual:
    st.chat_message("assistant").write(st.session_state.resposta_atual)