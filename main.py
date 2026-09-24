

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph

def ask_question(State):
    llm=ChatOpenAI(model="gpt-4o-mini",api_key="your_api_key_here")
    response=llm.invoke("give me one motivational quote")
    return{"output":response.content}


graph=StateGraph(dict)
graph.add_node("ask",ask_question)
graph.set_entry_point("ask")
graph.set_finish_point("ask")

app=graph.compile()
result=app.invoke({})
print(result["output"])