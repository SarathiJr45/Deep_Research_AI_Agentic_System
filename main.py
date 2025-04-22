from graph.workflow import build_graph
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    topic = input("Enter your research topic: ")
    agent_graph = build_graph()

    result = agent_graph.invoke({"topic": topic})
    print("\n Final Research Report:\n")
    print(result["final_answer"].content)