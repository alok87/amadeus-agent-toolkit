import os

import streamlit as st
from dotenv import load_dotenv
from langchain import hub
from langchain_openai import AzureChatOpenAI
from langgraph.prebuilt import create_react_agent

from amadeus_agent_toolkit.langchain.toolkit import AmadeusAgentToolkit

load_dotenv()

# Initialize LLM and Amadeus toolkit
try:
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

except Exception as e:
    st.error(f"Error initializing components: {e}")
    st.stop()  # Stop execution if initialization fails


# Streamlit app
st.title("Flight Search Agent")

user_input = st.text_area("Enter your flight search query (e.g., Search flight from BLR to GOI on 5th Feb 2025):")

if st.button("Search"):
    if user_input:
        input_state = {"messages": user_input}
        with st.spinner("Searching for flights..."):
            try:
                output_state = langgraph_agent_executor.invoke(input_state)
                # Display results
                st.write("## Search Results:")
                st.write(output_state["messages"][-1].content)  # Display the agent's response

                # Enhanced display (optional):  If the response is structured (e.g., JSON), you can parse and display it more nicely.
                # Example (assuming the agent returns a dictionary or list of dictionaries):
                # import json
                # try:
                #     results = json.loads(output_state["messages"][-1].content)
                #     st.json(results) # Or display in a table, etc.
                # except json.JSONDecodeError:
                #     st.write("Agent's response is not in JSON format. Displaying raw output.")

            except Exception as e:
                st.error(f"An error occurred during the search: {e}")
    else:
        st.warning("Please enter a flight search query.")
