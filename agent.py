from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage


model = ChatOllama(
    model="qwen2.5:7b"
)


prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} to a complete beginner in 2-3 sentences."
)


parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic": "AI agents"})

print(result)
# Create an in-memory conversation store
memory = InMemoryChatMessageHistory()

# Store previous conversation messages
memory.add_message(
    HumanMessage(content="My name is Alex and I'm learning LangChain.")
)

memory.add_message(
    AIMessage(content="Nice to meet you, Alex!")
)

memory.add_message(
    HumanMessage(content="What should I learn next?")
)

memory.add_message(
    AIMessage(content="You should learn PromptTemplates, chains, tools and agents.")
)

# Display stored messages
print("\n=== Memory Contents ===")

for msg in memory.messages:
    print(f"[{msg.type}]: {msg.content}")
    