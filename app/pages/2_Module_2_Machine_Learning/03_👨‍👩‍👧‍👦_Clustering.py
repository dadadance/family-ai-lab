import streamlit as st
import utils_lms
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

st.set_page_config(page_title="M2: Clustering", page_icon="👨‍👩‍👧‍👦")
user = utils_lms.get_current_user()
if not user:
    st.warning("🔒 Please login on the Home page to access this lesson.")
    st.stop()

# Derive lesson_id from filename
lesson_id = os.path.splitext(os.path.basename(__file__))[0].lower().replace('_', '-')
data = utils_lms.load_data()

# Check for previous lesson completion
if "02-linear-regression" not in data[user]["completed"]:
    st.error("🚫 Complete the previous lesson first.")
    st.page_link("pages/2_Module_2_Machine_Learning/02_📈_Linear_Regression.py", label="Go to Linear Regression lesson", icon="📈")
    st.stop()

st.title("👨‍👩‍👧‍👦 Clustering")
st.markdown("""
Clustering is an unsupervised learning task that involves grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar to each other than to those in other groups.

### 1. K-Means Clustering
K-Means is a popular clustering algorithm. It aims to partition *n* observations into *k* clusters in which each observation belongs to the cluster with the nearest mean.

Below, you can see how K-Means groups a set of randomly generated data points into clusters.
""")

# Generate sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# K-Means model
kmeans = KMeans(n_clusters=4, random_state=0, n_init=10)
y_kmeans = kmeans.fit_predict(X)

# Plotting the results
fig, ax = plt.subplots()
ax.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
ax.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X', label='Centroids')
ax.set_title("K-Means Clustering")
ax.legend()
st.pyplot(fig)


st.divider()
st.subheader("2. Knowledge Check")

if lesson_id in data[user]["completed"]:
    st.info("You have already completed this lesson and earned 50 XP.")
    st.success("🎉 Module 2 Complete! 🎉")
    st.page_link("Home.py", label="Back to Home", icon="🏠")
else:
    st.write("What type of learning is clustering?")
    answer = st.radio("Select the best answer:", ["Supervised", "Unsupervised", "Reinforcement"])
    if st.button("Submit Assignment"):
        if answer == "Unsupervised":
            utils_lms.mark_complete(lesson_id, xp_reward=50)
            st.success("Correct!")
            st.success("🎉 Module 2 Complete! 🎉")
            st.page_link("Home.py", label="Back to Home", icon="🏠")
        else:
            st.error("Incorrect. Clustering is a type of unsupervised learning because it deals with unlabeled data.")
