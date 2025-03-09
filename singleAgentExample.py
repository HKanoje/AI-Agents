from smolagents import CodeAgent, LiteLLMModel

model = LiteLLMModel(
    model_id="ollama/qwen2.5:7b",
    api_base="http://127.0.0.1:11434",
    num_ctx=8192,
)

agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run("Could you give me the 118th number in the Fibonacci sequence?")

