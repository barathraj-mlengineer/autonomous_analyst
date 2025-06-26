from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, Tool
from langchain_experimental.tools import PythonREPLTool
import os

llm = ChatGroq(
    api_key="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",
    model_name="llama3-70b-8192"
)

tools = [
    Tool(name="Python Interpreter", func=PythonREPLTool().run, description="Useful for running code on the fly")
]

agent = initialize_agent(
    tools, llm, agent="chat-zero-shot-react-description", verbose=True,handle_parsing_errors=True 
)

def run_agent(prompt):
    return agent.run(prompt)

