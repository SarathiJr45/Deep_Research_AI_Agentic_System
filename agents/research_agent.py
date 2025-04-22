from langchain_community.tools.tavily_search.tool import TavilySearchResults
from typing import TypedDict

class AgentState(TypedDict):
    topic: str
    research_docs: str
    final_answer: str

#  Research Agent

class ResearchAgent:
    def __init__(self):
        self.tool = TavilySearchResults(k=5)

    def run(self, state: AgentState) -> dict:
        topic = state["topic"]
        results = self.tool.invoke({"query": topic})
        docs = "\n".join([r['content'] for r in results])
        return {"research_docs": docs}

