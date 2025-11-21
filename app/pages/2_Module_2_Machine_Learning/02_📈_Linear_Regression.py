import streamlit as st
import utils_lms
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="M2: Linear Regression", page_icon="📈")
user = utils_lms.get_current_user()
if not user:
    st.warning("🔒 Please login on the Home page to access this lesson.")
    st.stop()

# Derive lesson_id from filename
lesson_id = os.path.splitext(os.path.basename(__file__))[0].lower().replace('_', '-')
data = utils_lms.load_data()

# Check for previous lesson completion
if "01-intro-to-ml" not in data[user]["completed"]:
    st.error("🚫 Complete the previous lesson first.")
    st.page_link("pages/2_Module_2_Machine_Learning/01_🤖_Intro_to_ML.py", label="Go to Intro to ML lesson", icon="🤖")
    st.stop()

st.title("📈 Linear Regression")
st.markdown("""
Linear regression is a supervised learning algorithm used to predict a continuous output. It models the relationship between a dependent variable and one or more independent variables by fitting a linear equation to the observed data.

### 1. Interactive Example
Here we have some data on house size and price. We can use linear regression to find the line of best fit.
""")

# Sample data
X = np.array([1000, 1500, 2000, 2500, 3000, 3500, 4000]).reshape(-1, 1)
y = np.array([300000, 450000, 550000, 680000, 720000, 750000, 800000])

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

fig, ax = plt.subplots()
ax.scatter(X, y, color='blue', label='Actual Prices')
ax.plot(X, y_pred, color='red', linewidth=2, label='Predicted Prices')
ax.set_xlabel("Size (sq ft)")
ax.set_ylabel("Price ($)")
ax.legend()
st.pyplot(fig)

st.write(f"Predicted price for a 2800 sq ft house: ${model.predict([[2800]])[0]:,.2f}")


st.divider()
st.subheader("2. Knowledge Check")

if lesson_id in data[user]["completed"]:
    st.info("You have already completed this lesson and earned 50 XP.")
    st.success("More lessons coming soon!")
    st.page_link("Home.py", label="Back to Home", icon="🏠")
else:
    st.write("What is the goal of linear regression?")
    answer = st.radio("Select the best answer:", ["To classify data into categories", "To find the line of best fit", "To group similar data points"])
    if st.button("Submit Assignment"):
        if answer == "To find the line of best fit":
            utils_lms.mark_complete(lesson_id, xp_reward=50)
            st.success("Correct!")
            st.info("More lessons coming soon!")
            st.page_link("Home.py", label="Back to Home", icon="🏠")
        else:
            st.error("Incorrect. The goal of linear regression is to find the line of best fit that can be used to make predictions.")
