from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


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