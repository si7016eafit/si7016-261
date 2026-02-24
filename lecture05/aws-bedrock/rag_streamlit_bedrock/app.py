import os
import boto3
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

REGION = os.getenv("AWS_REGION", "us-east-1")
KB_ID = os.getenv("KB_ID")
MODEL_ID = os.getenv("MODEL_ID")

if not KB_ID or not MODEL_ID:
    raise RuntimeError("Faltan KB_ID o MODEL_ID en el .env")

br = boto3.client("bedrock-agent-runtime", region_name=REGION)

st.set_page_config(page_title="RAG con Bedrock + OpenSearch", page_icon="X", layout="wide")
st.title("RAG (AWS Bedrock Knowledge Base + OpenSearch)")

with st.sidebar:
    st.markdown("### Config")
    st.write("Región:", REGION)
    st.write("KB_ID:", KB_ID)
    st.write("Modelo:", MODEL_ID)
    if st.button("Limpiar chat", use_container_width=True):
        st.session_state.messages = []

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hola. Pregúntame sobre los documentos en S3 (RAG)."}]

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

q = st.chat_input("Escribe tu pregunta…")
if q:
    st.session_state.messages.append({"role": "user", "content": q})
    with st.chat_message("user"):
        st.markdown(q)

    with st.chat_message("assistant"):
        with st.spinner("Consultando Knowledge Base…"):
            resp = br.retrieve_and_generate(
                input={"text": q},
                retrieveAndGenerateConfiguration={
                    "type": "KNOWLEDGE_BASE",
                    "knowledgeBaseConfiguration": {
                        "knowledgeBaseId": KB_ID,
                        "modelArn": MODEL_ID,
                        # Opcional: puedes ajustar retrievalConfiguration si tu caso lo requiere
                        # "retrievalConfiguration": {"vectorSearchConfiguration": {"numberOfResults": 4}}
                    }
                }
            )

            answer = resp["output"]["text"]
            st.markdown(answer)

            # Mostrar citas / fuentes si vienen
            citations = resp.get("citations", [])
            if citations:
                with st.expander("Fuentes / citas"):
                    for i, c in enumerate(citations, start=1):
                        st.markdown(f"**Cita {i}**")
                        # La estructura exacta puede variar; mostramos lo más robusto:
                        st.json(c)

    st.session_state.messages.append({"role": "assistant", "content": answer})