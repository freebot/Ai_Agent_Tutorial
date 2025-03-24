import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import  ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser 
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool

load_dotenv()
# Obtener la clave de API desde el entorno
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No se encontró la clave de API en las variables de entorno")

class ResearchResponse(BaseMOdel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]
    
llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key=api_key)
parser=PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_execuotr = AgentExecutor(agent=agent, tools=[], verbose=True, )
query = input("What can i help you research? ")
raw_response = agent_executor.invoke({"query": query)

try:
    structured_response = parser.parser(raw_response.get(("output")[0]("text"))
    print(structured_response)
except Exception as e:
    print(f"Error parsing response", e, "Raw Response - ", raw_response)
                                  