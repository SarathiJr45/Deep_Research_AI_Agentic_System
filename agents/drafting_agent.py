from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from agents.research_agent import AgentState

class DraftingAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.7)
        self.prompt = PromptTemplate.from_template(
            """You are an expert research assistant.

Based on the following documents, write a clear, informative research summary on the topic: "{topic}".

Research Documents:
{research_docs}

Answer:"""
        )
        self.chain = self.prompt | self.llm

    def run(self, state: AgentState) -> dict:
        topic = state["topic"]
        docs = state["research_docs"]
        answer = self.chain.invoke({"topic": topic, "research_docs": docs})
        return {"final_answer": answer}

