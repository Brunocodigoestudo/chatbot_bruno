# 🤖 ChatBot Davi - Assistente Virtual

Um assistente virtual interativo construído com Python, Streamlit e o modelo de IA Llama 3.3 da Groq.

## 📝 Descrição

ChatBot Davi é uma aplicação web que permite aos usuários interagir com um assistente virtual inteligente. Usando a API da Groq e o modelo Llama 3.3-70B, o assistente pode responder a perguntas, fornecer informações e manter uma conversa natural.

## ✨ Funcionalidades

- Interface de chat amigável e intuitiva
- Respostas geradas pelo modelo de IA Llama 3.3 da Groq
- Exibição apenas da conversa atual (pergunta e resposta)
- Design moderno e responsivo com Streamlit

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal
- **Streamlit**: Framework para criar aplicações web interativas
- **LangChain**: Framework para integração com modelos de linguagem
- **Groq API**: Acesso ao modelo de IA Llama 3.3

## ⚙️ Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/paribe/chatbot-davi.git
   cd chatbot-davi
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

   Ou usando Poetry:
   ```bash
   poetry install
   ```

3. Configure a chave API da Groq:
   - Crie uma conta na [Groq](https://groq.com/)
   - Gere uma chave API
   - Substitua `CHAVE_KEY` no código pela sua chave API ou defina a variável de ambiente `GROQ_API_KEY`

## 🚀 Execução

Para iniciar o ChatBot Davi:

```bash
streamlit run app.py
```

Após a execução, acesse o aplicativo no navegador através do endereço indicado no terminal (geralmente `http://localhost:8501`).

## 🎮 Como Usar

1. Digite sua pergunta na caixa de texto na parte inferior da tela
2. Pressione Enter ou clique no botão para enviar
3. O assistente responderá à sua pergunta
4. Cada nova pergunta substituirá a conversa anterior

## 📋 Requisitos

- Python 3.9+
- Conexão com internet (para acessar a API da Groq)
- Chave API válida da Groq

## 🔒 Considerações de Segurança

**Importante**: A chave API mostrada no código é apenas para fins de demonstração. Nunca compartilhe suas chaves API em repositórios públicos. Considere usar variáveis de ambiente ou arquivos de configuração seguros para armazenar suas chaves API.

