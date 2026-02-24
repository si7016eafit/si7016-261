import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def main():
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Falta OPENAI_API_KEY en tu .env")

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres un asistente útil y conciso. Si no sabes algo, dilo."),
        ("human", "{question}")
    ])

    chain = prompt | llm | StrOutputParser()

    print("Chat básico LangChain (escribe 'exit' para salir)\n")
    while True:
        q = input(">>> ").strip()
        if q.lower() in {"exit", "quit"}:
            break
        ans = chain.invoke({"question": q})
        print(f"ChatBot: {ans}\n")

if __name__ == "__main__":
    main()