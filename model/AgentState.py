from typing import TypedDict, Annotated

from langchain_core.messages import AnyMessage
from langgraph.graph import add_messages

class GraphState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    filename: str
    s3_bucket_original_url: str
    photo_labels: dict