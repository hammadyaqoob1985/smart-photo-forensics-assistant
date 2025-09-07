from langgraph.prebuilt import create_react_agent
from tools.rekognise_utils import analyze_image
from config.config import llm

tools = [analyze_image]

analyze_image_agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt=("you are a simple agent which takes in a filename and analyzes the image using the tool provided and returns the labels detected in the image. "
            "Your response should only include the labels detected in the image.")
)