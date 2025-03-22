# 🧠 AI Agents Playground

This project explores how AI agents can be implemented using **three different frameworks**. Each framework has its own folder with independent logic and tools, allowing for clear comparisons and modular experimentation.

## 📂 Project Structure

```
.
├── smolagents/     # Agents built with Smol Agents framework
├── llamaindex/     # Agents built with LlamaIndex for document interaction
├── langgraph/      # Agents built with LangGraph's node/edge system
├── requirements.txt  # dependencies
└── README.md       
```

## 🧠 LLMs Used

This project uses the following local LLMs served through **Ollama**:

1. **Qwen2.5 7B** – used in Smol Agents
2. **LLaMA 3.1 8B** – used in LlamaIndex-based agents
3. **Mistral** – used in LangGraph-based email workflow

These models are configured via wrappers like `LiteLLMModel`, `Ollama`, or `ChatOllama` depending on the framework.

## 🚀 Overview
This playground serves as a learning and experimentation space to:
- Compare agent frameworks
- Understand how tools, memory, context, and flow are handled
- Build reusable patterns for future projects

## 🔧 Frameworks Used

### 1. Smol Agents (`smolagents/`)
- Lightweight, tool-based agent system
- Focuses on modularity and simplicity

### 2. LlamaIndex (`llamaindex/`)
- Index and query over documents
- Useful for RAG and data-aware agents

### 3. LangGraph (`langgraph/`)
- Graph-based agent flow with custom edges
- Great for visualizing and managing complex agent logic

## 📦 Setup Instructions

### Create a Virtual Environment
```bash
python -m venv .venv
```

### Activate the Environment
**Windows:**
```bash
.venv\Scripts\activate
```
**macOS/Linux:**
```bash
source .venv/bin/activate
```

### Install Requirements
```bash
pip install -r requirements.txt
```

### Run Ollama Server (keep this running in another terminal)
```bash
ollama serve
```

## ✨ Goals & Features
- Unified design for testing and comparing agents
- Simple folder-based separation
- Extendable and beginner-friendly codebase

## 📝 Notes
- More examples and benchmarking might be added later
- Each folder is standalone and self-documented

---
## 🙏 Acknowledgments

A big **thank you to Hugging Face** for their incredible **AI Agents course**, which served as the inspiration and learning foundation for this project.

The concepts, workflows, and code explored here were directly influenced by the hands-on lessons and guidance provided throughout the course. Massive respect to the instructors and contributors for making advanced agent tooling approachable and practical.

---

> Check out the individual `README.md` in each folder for detailed documentation and usage examples.

