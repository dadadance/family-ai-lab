import streamlit as st
import utils_lms
st.set_page_config(page_title="Sprint 2: Embeddings", page_icon="🧬")
user = utils_lms.get_current_user()
if not user:
    st.warning("🔒 Login required.")
    st.stop()
st.title("🧬 Sprint 2: Word Embeddings")
data = utils_lms.load_data()
if "sprint_1_vectors" in data[user]["completed"]:
    st.success("🎉 Unlocked!")
    st.write("Welcome to Embeddings.")
else:
    st.error("🚫 Complete Sprint 1 first.")
