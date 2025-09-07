from model.AgentState import GraphState
from agents.analyse_photo_agent import analyze_image_agent
from langchain_core.messages import AIMessage
from langgraph.types import Command

def analyse_photo_node(state: GraphState):
    result = analyze_image_agent.invoke(state)

    return Command(
        update={
            "messages": state["messages"] + [
                AIMessage(content=result["messages"][-1].content, name="analyse_photo_node")
            ]
        }
    )