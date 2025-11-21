import streamlit as st
import utils_lms
import os
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="M3: Neural Networks", page_icon="🧠")
user = utils_lms.get_current_user()
if not user:
    st.warning("🔒 Please login on the Home page to access this lesson.")
    st.stop()

# Derive lesson_id from filename
lesson_id = os.path.splitext(os.path.basename(__file__))[0].lower().replace('_', '-')
data = utils_lms.load_data()

# Check for previous module completion
if "03-clustering" not in data[user]["completed"]:
    st.error("🚫 Complete Module 2 first.")
    st.page_link("pages/2_Module_2_Machine_Learning/03_👨‍👩‍👧‍👦_Clustering.py", label="Go to Module 2 Finale", icon="👨‍👩‍👧‍👦")
    st.stop()

st.title("🧠 Neural Networks")
st.markdown("""
A neural network is a series of algorithms that endeavors to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates.

### 1. Simple Neural Network Visualization
Here is a simple neural network with one hidden layer.
""")

# Visualization of a simple neural network
fig, ax = plt.subplots()
ax.axis('off')
ax.set_aspect('equal')

# Nodes
input_layer = [(-1, 1), (-1, 0), (-1, -1)]
hidden_layer = [(-0, 1.5), (-0, 0.5), (-0, -0.5), (-0, -1.5)]
output_layer = [(1, 0)]

# Draw nodes
for x, y in input_layer:
    ax.add_artist(plt.Circle((x, y), 0.1, color='blue'))
for x, y in hidden_layer:
    ax.add_artist(plt.Circle((x, y), 0.1, color='red'))
for x, y in output_layer:
    ax.add_artist(plt.Circle((x, y), 0.1, color='green'))

# Draw connections
for ix, iy in input_layer:
    for hx, hy in hidden_layer:
        ax.plot([ix, hx], [iy, hy], 'k-', alpha=0.5)

for hx, hy in hidden_layer:
    for ox, oy in output_layer:
        ax.plot([hx, ox], [hy, oy], 'k-', alpha=0.5)

ax.text(-1, 2, "Input Layer")
ax.text(-0.2, 2, "Hidden Layer")
ax.text(0.8, 2, "Output Layer")


st.pyplot(fig)


st.divider()
st.subheader("2. Knowledge Check")

if lesson_id in data[user]["completed"]:
    st.info("You have already completed this lesson and earned 50 XP.")
    st.success("More lessons coming soon!")
    st.page_link("Home.py", label="Back to Home", icon="🏠")
else:
    st.write("What is the name of the middle layer in a neural network?")
    answer = st.radio("Select the best answer:", ["Input Layer", "Hidden Layer", "Output Layer"])
    if st.button("Submit Assignment"):
        if answer == "Hidden Layer":
            utils_lms.mark_complete(lesson_id, xp_reward=50)
            st.success("Correct!")
            st.info("More lessons coming soon!")
            st.page_link("Home.py", label="Back to Home", icon="🏠")
        else:
            st.error("Incorrect. The middle layer is called the hidden layer.")
