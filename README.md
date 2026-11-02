# LangChain Agent Learning Project

A hands-on learning project exploring the core building blocks of LangChain for AI agents.

## Current Progress

* Connected LangChain to a local LLM using Ollama
* Used Qwen2.5 7B as the local language model
* Created reusable PromptTemplates
* Built LCEL chains using the | operator
* Used StrOutputParser to process model output

## Current Architecture

```text
User Input
    ↓
PromptTemplate
    ↓
LangChain
    ↓
Ollama
    ↓
Qwen2.5 7B
    ↓
StrOutputParser
    ↓
Response
```

## Tech Stack

* Python
* LangChain
* Ollama
* Qwen2.5 7B

## Learning Roadmap

* [x] Models
* [x] Prompt Templates
* [x] Chains / LCEL
* [x] Output Parsers
* [x] Memory
* [ ] Tools
* [ ] Tool Calling
* [ ] Agents

This repository is being built incrementally while learning LangChain and agentic AI concepts.
