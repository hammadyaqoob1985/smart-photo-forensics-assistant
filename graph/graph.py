
from langgraph.checkpoint.memory import MemorySaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph

from nodes.upload_node import upload_file_node
from nodes.analyse_photo_node import analyse_photo_node
from model.AgentState import GraphState



builder = StateGraph(GraphState)
memory = MemorySaver()
builder.add_node("analyse_photo_node", analyse_photo_node)
builder.add_edge(START, "analyse_photo_node")
builder.add_edge("analyse_photo_node", END)
graph = builder.compile(checkpointer=memory)
