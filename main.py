import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import  ChatOpenAI

load_dotenv()
# Obtener la clave de API desde el entorno
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No se encontró la clave de API en las variables de entorno")


llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key=api_key)
response=llm.invoke("what is the meaning of life?")
print(response)
