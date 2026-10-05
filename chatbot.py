# CHATBOT COM IA
# DISPLAY INICIAL - titulo e input
# RESPOSTAS COM IA
# MEMORIA ARMAZENADA

import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Chatbot com IA", page_icon="💬", layout="centered")

st.title("💬 Chatbot com IA")
st.caption("Converse com uma inteligência artificial integrada ao Google Gemini")

cliente = OpenAI(
    api_key=st.secrets["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",)

# memoria armazenada
if "mensagens" not in st.session_state:
    st.session_state["mensagens"] = []

# barra lateral: informações e botão de nova conversa
with st.sidebar:
    st.write("## Sobre")
    st.write("Assistente de IA que lembra o contexto da conversa.")
    if st.button("🗑️ Nova conversa"):
        st.session_state["mensagens"] = []
        st.rerun()

# ícones de cada participante da conversa
avatares = {"user": "🙂", "assistant": "🤖"}

# mostrar mensagens armazenadas
for mensagem in st.session_state["mensagens"]:
    st.chat_message(mensagem["role"], avatar=avatares[mensagem["role"]]).write(mensagem["content"])

pergunta = st.chat_input("Digite sua pergunta aqui...")

if pergunta:
    # mostrar e guarda a pergunta do usuário
    st.chat_message("user", avatar=avatares["user"]).write(pergunta)
    mensagem_usuario = {"role": "user", "content": pergunta}
    st.session_state["mensagens"].append(mensagem_usuario)

    # resposta da IA
    resposta_modelo = cliente.chat.completions.create(
        model="gemini-flash-lite-latest",
        messages=st.session_state["mensagens"]
    )
    resposta_ia = resposta_modelo.choices[0].message.content

    # exibir a resposta da IA na tela
    st.chat_message("assistant", avatar=avatares["assistant"]).write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["mensagens"].append(mensagem_ia)