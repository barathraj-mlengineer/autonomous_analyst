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
