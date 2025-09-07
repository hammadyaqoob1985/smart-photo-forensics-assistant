from model.AgentState import GraphState
from agents.upload_agent import upload_agent

def upload_file_node(state: GraphState):
    result = upload_agent.invoke(state["file_obj"], state["filename"])
    state["s3_bucket_original_url"] = result
    return state