import streamlit as st
import utils_lms
import os

st.set_page_config(page_title="M2: Intro to ML", page_icon="🤖")
user = utils_lms.get_current_user()
if not user:
    st.warning("🔒 Please login on the Home page to access this lesson.")
    st.stop()

# Derive lesson_id from filename
lesson_id = os.path.splitext(os.path.basename(__file__))[0].lower().replace('_', '-')
data = utils_lms.load_data()

# Check for previous module completion
if "04-pandas-dataframes" not in data[user]["completed"]:
    st.error("🚫 Complete Module 1 first.")
    st.page_link("pages/1_Module_1_Foundations/04_🐼_Pandas_DataFrames.py", label="Go to Module 1 Finale", icon="🐼")
    st.stop()

st.title("🤖 Introduction to Machine Learning")
st.markdown("""
Machine Learning (ML) is a type of artificial intelligence (AI) that allows software applications to become more accurate at predicting outcomes without being explicitly programmed to do so.

### 1. Supervised Learning
In supervised learning, we use labeled data to train our model. The model's goal is to learn a mapping function that can predict the output for new, unseen data.
- **Classification**: The output is a category (e.g., "spam" or "not spam").
- **Regression**: The output is a continuous value (e.g., predicting a house price).

### 2. Unsupervised Learning
In unsupervised learning, we use unlabeled data. The goal is to find hidden patterns or intrinsic structures in the data.
- **Clustering**: Grouping similar data points together.
- **Association**: Discovering relationships between variables in a large dataset.
""")

st.divider()
st.subheader("3. Knowledge Check")

if lesson_id in data[user]["completed"]:
    st.info("You have already completed this lesson and earned 50 XP.")
    st.success("More lessons coming soon!")
    st.page_link("Home.py", label="Back to Home", icon="🏠")
else:
    st.write("You are building a model to predict if an email is 'spam' or 'not spam'. What type of problem is this?")
    answer = st.radio("Select the problem type:", ["Regression", "Clustering", "Classification"])
    if st.button("Submit Assignment"):
        if answer == "Classification":
            utils_lms.mark_complete(lesson_id, xp_reward=50)
            st.success("Correct!")
            st.info("More lessons coming soon!")
            st.page_link("Home.py", label="Back to Home", icon="🏠")
        else:
            st.error("Incorrect. Predicting a category is a classification problem.")
