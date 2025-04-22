from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from agents.research_agent import ResearchAgent
from agents.research_agent import AgentState
from agents.drafting_agent import DraftingAgent
from langchain_core.runnables import RunnableLambda

#  state schema
def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("research", RunnableLambda(ResearchAgent().run))
    builder.add_node("draft", RunnableLambda(DraftingAgent().run))

    builder.set_entry_point("research")
    builder.add_edge("research", "draft")
    builder.add_edge("draft", END)

    return builder.compile()
