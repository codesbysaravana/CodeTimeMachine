import streamlit as st
import requests

# Streamlit page config
st.set_page_config(page_title="🕰️ Code Time Machine", layout="wide")

st.title("🧠 Code Time Machine")
st.markdown("Search COBOL codebase and get intelligent explanations with RAG.")

# User input
query = st.text_input("🔍 Enter your query:")

# Select mode
mode = st.radio("Select Mode:", ["Search Codebase", "RAG Explanation"])

# On search
if st.button("🚀 Run"):
    if not query:
        st.warning("Please enter a query.")
    else:
        with st.spinner("Processing..."):
            try:
                if mode == "Search Codebase":
                    response = requests.post("http://localhost:8000/query-code", json={"query": query})
                    if response.status_code == 200:
                        data = response.json()
                        st.subheader("🔎 Top Code Matches")
                        for match in data.get("matches", []):
                            st.code(match, language="cobol")
                    else:
                        st.error("Error from /query-code endpoint")

                elif mode == "RAG Explanation":
                    response = requests.post("http://localhost:8000/rag", json={"query": query})
                    if response.status_code == 200:
                        data = response.json()
                        st.subheader("📄 Retrieved Code")
                        st.code(data.get("code", "No code returned."), language="cobol")

                        st.subheader("🧠 Explanation")
                        st.write(data.get("explanation", "No explanation found."))
                    else:
                        st.error("Error from /rag endpoint")

            except Exception as e:
                st.error(f"An error occurred: {e}")
