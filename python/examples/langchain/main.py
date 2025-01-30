import os

from dotenv import load_dotenv
from langchain import hub
from langchain_openai import AzureChatOpenAI
from langgraph.prebuilt import create_react_agent

from amadeus_agent_toolkit.langchain.toolkit import AmadeusAgentToolkit

load_dotenv()

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    model=os.getenv("AZURE_OPENAI_MODEL_NAME"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),
)

amadeus_agent_toolkit = AmadeusAgentToolkit(
    client_id=os.getenv("AMADEUS_CLIENT_ID"),
    client_secret=os.getenv("AMADEUS_CLIENT_SECRET"),
    configuration={
        "actions": {
            "flights": {
                "search": True,
            },
        }
    },
)

tools = []
tools.extend(amadeus_agent_toolkit.get_tools())

langgraph_agent_executor = create_react_agent(llm, tools)

input_state = {
    "messages": """
        Search flight from BLR to GOI on 5th Feb 2025
    """,
}

print("result")
output_state = langgraph_agent_executor.invoke(input_state)

print(output_state)

print(output_state["messages"][-1].content)
