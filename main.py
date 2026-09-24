from langchain_openai import ChatOpenAi
from langgraph.Graph import StateGraph

def ask_question(State):
    llm=ChatOpenAi(model="gpt-4o-mini")
    