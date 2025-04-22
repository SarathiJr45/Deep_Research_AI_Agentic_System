#  Deep Research Agentic System

A fully agentic AI-powered research assistant that autonomously collects information, synthesizes it, and drafts high-quality research reports based on a given topic. It leverages LangGraph for stateful agent orchestration, Tavily for web search, and Gemini Pro for content generation — all wrapped in a Streamlit UI with PDF export.

##  Features

-  **Research Agent**: Gathers factual insights from the web using Tavily Search API.
-  **Writer Agent**: Drafts a well-structured, coherent research report using Gemini Pro (Google's LLM).
-  **Cyclic Graph-based Agent Execution**: Powered by LangGraph for memory/state persistence.
-  **Streamlit Frontend**: Clean, user-friendly UI for interaction.
-  **PDF Report Generation**: Download the final report as a beautifully formatted PDF.

## Installation

1. **Clone this repo**

git clone https://github.com/SarathiJr45/Deep_Research_AI_Agentic_System.git

cd Deep_Research_AI_Agentic_System

2. **Create virtual environment & install dependencies**

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

3. **Add your API keys to .env**

GOOGLE_API_KEY=your_gemini_api_key

TAVILY_API_KEY=your_tavily_api_key

4. **Run the app**

streamlit run app.py
