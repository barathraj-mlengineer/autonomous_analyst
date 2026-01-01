from langchain_groq import ChatGroq
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.tools import PythonREPLTool
from langchain_core.prompts import PromptTemplate

# LLM
llm = ChatGroq(
    api_key="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",
    model_name="llama-3.3-70b-versatile"
)

# Tool
tools = [PythonREPLTool()]

# Required prompt (ReAct)
prompt = PromptTemplate.from_template(
    """Answer the question using the tools if needed.

Tools:
{tools}

Use this format:

Question: {input}
Thought: think step by step
Action: tool name
Action Input: input
Observation: result
Final Answer: answer

{agent_scratchpad}
"""
)

# Create agent
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

# Executor (replacement for initialize_agent)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

def run_agent(prompt: str):
    result = agent_executor.invoke({"input": prompt})
    return result["output"]
