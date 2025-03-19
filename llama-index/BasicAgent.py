import asyncio
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.ollama import Ollama

#define the simple cal
def multiply(a: float, b: float) -> float:
    """ Useful for multiplying two numbers """
    return a * b

#crete an agent workflow with our calculator tool
agent = FunctionAgent(
    name="Agent",
    description="Useful for multiplying two numbers",
    tools=[multiply],
    llm=Ollama(model="llama3.1:8b", request_timeout=360.0),
    system_prompt="You are a helpful assistant that can multiply two numbers.",
)

async def main():
    #run the agent
    response = await agent.run("What is 1234 * 5678?")
    print(str(response))

#run the agent
if __name__ == "__main__":
    asyncio.run(main())