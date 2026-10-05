# 💬 Chatbot com IA

Chatbot com inteligência artificial no estilo do ChatGPT, desenvolvido em Python com Streamlit e integrado à API do Google Gemini.

   🔗 **[Testar o chatbot online]([https://seu-link.streamlit.app](https://chatbot-ia-md.streamlit.app/))**
   
Projeto desenvolvido a partir do **Intensivão de Python** da [Hashtag Treinamentos](https://www.hashtagtreinamentos.com/) e aprimorado por mim após o evento.

## ✨ Funcionalidades

- **Interface de chat:** exibe as mensagens do usuário e da IA em formato de conversa
- **Histórico da conversa:** todas as mensagens enviadas e recebidas ficam visíveis na tela
- **Memória de contexto:** a IA recebe o histórico completo a cada pergunta e lembra o que já foi dito
- **Nova conversa:** botão na barra lateral que apaga o histórico e inicia um novo chat
- **Integração com o Gemini:** utiliza a biblioteca da OpenAI conectada à API compatível do Google Gemini

## 🚀 Aprimoramentos após o evento

Depois do Intensivão, desenvolvi por conta própria melhorias na experiência e no visual do chatbot:

- **Identidade visual própria:** tema escuro com destaque em roxo, configurado no `config.toml` do Streamlit
- **Avatares na conversa:** ícones diferentes para o usuário e para a IA, facilitando a leitura do chat
- **Barra lateral:** com informações sobre o assistente e o botão de nova conversa
- **Título e subtítulo:** apresentação do chat na tela e nome e ícone na aba do navegador
- **Proteção da chave de API:** credencial armazenada fora do código e fora do repositório

## 🔒 Segurança

A chave de API não fica no código. Ela é armazenada no arquivo `secrets.toml` do Streamlit, que não faz parte do repositório. Assim, a credencial nunca fica exposta publicamente.

## 🛠️ Tecnologias

- **Python**
- **Streamlit:** interface web do chat
- **OpenAI SDK:** comunicação com o modelo de IA
- **Google Gemini:** modelo de linguagem que gera as respostas

## ▶️ Como executar

1. Instale as dependências:

```
pip install -r requirements.txt
```

2. Crie uma chave de API gratuita no [Google AI Studio](https://aistudio.google.com/apikey).

3. Na pasta do projeto, crie a pasta `.streamlit` e, dentro dela, o arquivo `secrets.toml` com o conteúdo:

```
GEMINI_API_KEY = "sua-chave-aqui"
```

4. Execute o chatbot:

```
streamlit run chatbot.py
```

O navegador vai abrir automaticamente com o chat.

## 👩‍💻 Autora

**Maria Eduarda Tucunduva**

[LinkedIn](https://www.linkedin.com/in/maria-eduarda-tucunduva) · [GitHub](https://github.com/madutucunduva)
