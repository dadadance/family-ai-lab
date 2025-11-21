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
    m2.metric("Lessons Finished", len(data[user]["completed"]))
    xp = data[user]["xp"]
    rank = "🌱 Novice"
    if xp >= 500: rank = "🛠️ Apprentice"
    if xp >= 1000: rank = "🚀 Engineer"
    if xp >= 5000: rank = "🧙‍♂️ Guru"
    m3.metric("Current Rank", rank)
    st.divider()
    st.header("🗺️ Your Roadmap")
    
    # Get modules by listing directories in the 'pages' folder
    pages_dir = "pages"
    modules = sorted([d for d in os.listdir(pages_dir) if os.path.isdir(os.path.join(pages_dir, d))])
    
    for module_name in modules:
        with st.expander(f"**{module_name.replace('_', ' ')}**", expanded=True):
            module_path = os.path.join(pages_dir, module_name)
            lessons = sorted([f for f in os.listdir(module_path) if f.endswith(".py")])
            
            for lesson_file in lessons:
                lesson_path = os.path.join(module_path, lesson_file)
                lesson_name = os.path.splitext(lesson_file)[0][3:].replace('_', ' ')
                # Create a unique lesson_id from the filename
                lesson_id = os.path.splitext(lesson_file)[0].lower().replace('_', '-')

                col1, col2 = st.columns([4, 1])
                with col1:
                    if lesson_id in data[user]["completed"]:
                        st.markdown(f"✅ ~~_{lesson_name}_~~")
                    else:
                        st.markdown(f"◻️ {lesson_name}")
                with col2:
                    st.page_link(lesson_path, label="Start", icon="▶️")

else:
    st.info("👈 Please login via the sidebar to track your progress.")
    st.image("https://storage.googleapis.com/gemini-agile-prod-storage/project_replit/meme.png")
    st.markdown("""
    ### 🚀 AI Engineer - Zero to Hero!
    This course is designed to take you from the very basics of programming to deploying and managing complex AI systems.
    
    **Login to start your journey!**
    """)
