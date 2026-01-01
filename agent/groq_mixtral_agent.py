from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, Tool
from langchain_experimental.tools import PythonREPLTool
import os

llm = ChatGroq(
    api_key="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",
    model_name="llama-3.3-70b-versatile"
)

tools = [
    Tool(name="Python Interpreter", func=PythonREPLTool().run, description="Useful for running code on the fly")
]

agent = initialize_agent(
    tools, llm, agent="chat-zero-shot-react-description", verbose=True,handle_parsing_errors=True 
)

def run_agent(prompt):
    return agent.run(prompt)

