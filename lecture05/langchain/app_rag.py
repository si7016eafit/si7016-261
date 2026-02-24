import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def load_docs(folder: str):
    texts = []
    for p in Path(folder).glob("*.txt"):
        texts.append(p.read_text(encoding="utf-8"))
    if not texts:
        raise RuntimeError(f"No encontré .txt en {folder}")
    return "\n\n".join(texts)

def build_vectorstore(raw_text: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=120
    )
    chunks = splitter.split_text(raw_text)

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vs = FAISS.from_texts(chunks, embedding=embeddings)
    return vs

def main():
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Falta OPENAI_API_KEY en tu .env")

    # Ingesta
    corpus = load_docs("docs")
    vectorstore = build_vectorstore(corpus)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    # LLM
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

    # Prompt RAG
    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "Responde usando SOLO el contexto. "
         "Si el contexto no alcanza, di: 'No está en los documentos'."),
        ("human",
         "Pregunta: {question}\n\n"
         "Contexto:\n{context}")
    ])

    # chatbot
    print("RAG básico LangChain + FAISS (escribe 'exit' para salir)\n")
    while True:
        q = input("Tú: ").strip()
        if q.lower() in {"exit", "quit"}:
            break

        docs = retriever.get_relevant_documents(q)
        context = "\n\n---\n\n".join([d.page_content for d in docs])

        chain = prompt | llm | StrOutputParser()
        ans = chain.invoke({"question": q, "context": context})

        print(f"Chatbot: {ans}\n")

if __name__ == "__main__":
    main()