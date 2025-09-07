from langgraph.prebuilt import create_react_agent
from tools.s3_utils import upload_file_to_s3
from config.config import llm
tools = [upload_file_to_s3]

upload_agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt="you are a simple agent which takes in a file and filename and uploads it to s3 and returns the url using the tool provided"
)