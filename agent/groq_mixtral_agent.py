from langchain_groq import ChatGroq
from langchain_experimental.tools import PythonREPLTool

# LLM
llm = ChatGroq(
    api_key="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",
    model_name="llama-3.3-70b-versatile"
)

python_tool = PythonREPLTool()

def run_agent(prompt: str):
    # If prompt asks for calculation, use python
    if any(x in prompt.lower() for x in ["calculate", "*", "+", "-", "/", "python"]):
        return python_tool.run(prompt)

    # Otherwise normal LLM call
    response = llm.invoke(prompt)
    return response.content
