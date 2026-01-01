from langchain_groq import ChatGroq
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.tools import PythonREPLTool
from langchain_core.prompts import PromptTemplate

# LLM
llm = ChatGroq(
    api_key="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",
    model_name="llama-3.3-70b-versatile"
)

# Tools
tools = [PythonREPLTool()]

# ReAct prompt (MANDATORY in new LangChain)
prompt = PromptTemplate.from_template(
    """Answer the following questions as best you can.
You have access to the following tools:

{tools}

Use the following format:

Question: the input question
Thought: you should think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
Thought: I now know the final answer
Final Answer: the final answer to the question

Question: {input}
{agent_scratchpad}
"""
)

# Create agent
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

# Executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

def run_agent(prompt: str):
    return agent_executor.invoke({"input": prompt})["output"]
