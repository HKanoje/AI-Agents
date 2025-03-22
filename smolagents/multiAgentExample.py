from smolagents import CodeAgent, LiteLLMModel, DuckDuckGoSearchTool

model = LiteLLMModel(
    model_id="ollama/llama3.1:8b",
    api_base="http://127.0.0.1:11434",
    num_ctx=8192,
)


web_agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
    name="web_search_agent",
    description="Runs web searches for you. Give it your query as an argument."
)

manager_agent = CodeAgent(
    tools=[], model=model, managed_agents=[web_agent]
)

manager_agent.run("Who is the CEO of Hugging Face?")