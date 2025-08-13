import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Tentar pegar a chave do ambiente local ou dos secrets do Streamlit
groq_api_key = os.getenv('GROQ_API_KEY') or st.secrets.get('GROQ_API_KEY')

if not groq_api_key:
    st.error("❌ Erro: GROQ_API_KEY não encontrada. Verifique seu .env (local) ou Secrets (deploy).")
    st.stop()

# Inicializar o modelo de IA com a chave
chat = ChatGroq(model='llama-3.3-70b-versatile', api_key=groq_api_key)


# Função para obter resposta do bot
def resposta_do_bot(pergunta):
    system_message = 'Você é um assistente amigável chamado ChatBot (Bruno)'
    template = ChatPromptTemplate.from_messages([
        ('system', system_message),
        ('user', pergunta)
    ])
    chain = template | chat
    return chain.invoke({}).content

# Interface com Streamlit
st.title("🤖 ChatBot (Bruno) - Seu Assistente Virtual")

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