import streamlit as st
import utils_lms
import os

st.set_page_config(page_title="M1: Word Embeddings", page_icon="🧬")
user = utils_lms.get_current_user()
if not user:
    st.warning("🔒 Login required.")
    st.stop()

# Derive lesson_id from filename
lesson_id = os.path.splitext(os.path.basename(__file__))[0].lower().replace('_', '-')

st.title("🧬 Sprint 2: Word Embeddings")
data = utils_lms.load_data()
if "01-the-dot-product" not in data[user]["completed"]:
    st.error("🚫 Complete Sprint 1 first.")
    st.page_link("pages/1_Module_1_Foundations/01_📐_The_Dot_Product.py", label="Go to Sprint 1", icon="📐")
    st.stop()

st.success("🎉 Unlocked!")
st.markdown("""
In the last lesson, you learned that the dot product measures the similarity between two vectors.

**Word Embeddings** are simply vectors that represent words. Words with similar meanings will have vectors that are 'close' to each other in space, resulting in a high dot product!
""")

if lesson_id in data[user]["completed"]:
    st.info("You have already completed this lesson and earned 100 XP.")
    st.page_link("Home.py", label="Back to Home", icon="🏠")
else:
    st.subheader("Knowledge Check")
    st.write("If the vector for 'King' is `[0.9, 0.1]` and the vector for 'Queen' is `[0.8, 0.2]`, would their dot product be high or low?")
    answer = st.radio("Select result:", ["High (similar)", "Low (unrelated)"])
    if st.button("Submit Assignment"):
        if answer == "High (similar)":
            utils_lms.mark_complete(lesson_id, xp_reward=100)
            st.write("Correct! Similar words have a high dot product.")
            st.info("More lessons coming soon!")
            st.page_link("Home.py", label="Back to Home", icon="🏠")
        else:
            st.error("Incorrect. Remember, a high dot product means high similarity.")
