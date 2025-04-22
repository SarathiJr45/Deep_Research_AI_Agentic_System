import streamlit as st
from graph.workflow import build_graph
from dotenv import load_dotenv
import os
from xhtml2pdf import pisa
import io


load_dotenv()

st.set_page_config(page_title="Deep Research Agent", page_icon="🔎")
st.title("🔍 Deep Research Agentic System")
st.markdown("Powered by **Gemini + Tavily + LangGraph**")

topic = st.text_input("Enter a research topic", placeholder="e.g. Quantum Computing")

def convert_html_to_pdf(source_html):
    result_io = io.BytesIO()
    pisa_status = pisa.CreatePDF(io.StringIO(source_html), dest=result_io)
    if pisa_status.err:
        return None
    return result_io

if st.button("Start Research") and topic:
    with st.spinner("Conducting research and drafting your report..."):
        try:
            agent_graph = build_graph()
            result = agent_graph.invoke({"topic": topic})
            final_report = result["final_answer"].content

            st.success("✅ Report Generated Successfully!")
            st.markdown("### 📘 Final Research Report")
            st.markdown(final_report, unsafe_allow_html=True)

            # Convert to PDF
            html_content = f"<html><body>{final_report}</body></html>"
            pdf_file = convert_html_to_pdf(html_content)

            if pdf_file:
                st.download_button(
                    label="📄 Download Report as PDF",
                    data=pdf_file,
                    file_name=f"{topic}_research_report.pdf",
                    mime="application/pdf"
                )
            else:
                st.warning("Failed to generate PDF.")

        except Exception as e:
            st.error(f" Something went wrong:\n{e}")
