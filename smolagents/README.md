
# 🤖 Smol Agents

This folder contains examples of AI agents built using the **[Smol Agents](https://github.com/smol-ai/smol-developer)** framework. Smol Agents are lightweight, modular, and designed for fast development of autonomous agent systems.

## 📁 Contents

- `singleAgentExample.py` – A single agent capable of answering questions using base tools.
- `multiAgentExample.py` – A manager agent that delegates tasks to a web search agent (using DuckDuckGo).
- `AgenticRAGvsRAG.ipynb` – A Jupyter Notebook comparing traditional RAG with Agentic RAG.

## ⚙️ How It Works

### 1. `LiteLLMModel`

- Uses **mistral 4B** model served locally via `ollama`.
- All agents are powered by this local LLM.

### 2. `CodeAgent`

- The core agent class from `smolagents`.
- Supports tools and tool delegation.

### 3. Web Search Tool

- The multi-agent example adds a `DuckDuckGoSearchTool` for real-time web queries.

## 🚀 Running the Examples

Make sure you’ve followed the [root setup instructions](../README.md#setup-instructions) to activate your virtual environment and install dependencies.

Then, run:

### 🧪 Single Agent

```bash
python singleAgentExample.py
```

*Asks the agent to compute the 118th Fibonacci number.*

### 🤝 Multi-Agent with Web Search

```bash
python multiAgentExample.py
```

*The manager agent asks the web agent to search "Who is the CEO of Hugging Face?"*

## 🧠 Agent Architecture

```
multiAgentExample.py
└── Manager Agent
    └── Web Agent (with DuckDuckGo Tool)
```

## 🔍 Example Output


**Input:**

> Who is the CEO of Hugging Face?

**Output:**

> [Agent searches and returns an answer from DuckDuckGo]

![Output](..\asserts\sm1.png)
![Output](..\asserts\sm2.png)

## 📊 RAG vs Agentic RAG (Notebook Comparison)


- 📓 `AgenticRAGvsRAG.ipynb` – A Jupyter Notebook that compares traditional RAG pipelines with agent-augmented RAG using Smol Agents.

### 🔬 What's Covered
- Traditional Retrieval-Augmented Generation vs Agentic RAG
- Output quality, reasoning steps, and response depth
- Visual results and commentary


---

## 📌 Notes

- These agents require `ollama` to be running in the background.
- You can expand the agents with more tools (APIs, files, scraping, etc).

---

> This is part of the [AI Agents Playground](../README.md) project. Check other folders for more frameworks!

