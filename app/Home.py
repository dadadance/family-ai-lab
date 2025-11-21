import streamlit as st
import utils_lms
import pandas as pd
import requests
import os

st.set_page_config(page_title="Family AI Lab", page_icon="🧬", layout="wide")
st.title("🧬 Family AI Lab")
st.markdown("*A private, local learning environment for future AI Engineers.*")

data = utils_lms.load_data()
user = utils_lms.get_current_user()

with st.sidebar:
    st.header("👤 Driver Select")
    if user:
        st.success(f"Logged in as: **{user}**")
        if st.button("Logout"):
            utils_lms.set_user(None)
    else:
        st.info("Who is driving today?")
        selected = st.selectbox("Select Profile", ["Husband", "Wife"])
        if st.button("Login"):
            utils_lms.set_user(selected)
    st.divider()
    st.caption("System Status")
    try:
        ollama_url = os.getenv("OLLAMA_URL", "http://ollama:11434")
        if requests.get(f"{ollama_url}/api/tags", timeout=1).status_code == 200:
             st.write("🟢 LLM Engine: Online")
        else:
             st.write("🔴 LLM Engine: Offline")
    except:
        st.write("🔴 LLM Engine: Unreachable")

if user:
    st.subheader(f"Welcome back, {user}!")
    m1, m2, m3 = st.columns(3)
    m1.metric("Total XP", data[user]["xp"])
    m2.metric("Modules Finished", len(data[user]["completed"]))
    xp = data[user]["xp"]
    rank = "🌱 Novice"
    if xp >= 500: rank = "🛠️ Apprentice"
    if xp >= 1000: rank = "🚀 Engineer"
    if xp >= 5000: rank = "🧙‍♂️ Guru"
    m3.metric("Current Rank", rank)
    st.divider()
    st.write("### 🏆 Household Leaderboard")
    df = pd.DataFrame.from_dict(data, orient='index')
    df['user'] = df.index
    st.bar_chart(df, x='user', y='xp', color='#FF4B4B')
else:
    st.info("👈 Please login via the sidebar to track your progress.")
    st.markdown("""
    ### 🗺️ The Roadmap
    **Sprint 1: The Foundations**
    - [x] Environment Setup
    - [ ] Vectors & Dot Products (See Page 1)
    """)
