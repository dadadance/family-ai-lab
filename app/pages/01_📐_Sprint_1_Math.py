import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import utils_lms

st.set_page_config(page_title="Sprint 1: Math", page_icon="📐")
user = utils_lms.get_current_user()
if not user:
    st.warning("🔒 Please login on the Home page to access this lesson.")
    st.stop()

st.title("📐 Sprint 1: The Dot Product")
st.markdown("""
**Why this matters:** The "Dot Product" is the engine of AI. It is how we calculate **Similarity**.
""")

st.subheader("1. Interactive Vector Lab")
col1, col2 = st.columns(2)
with col1:
    st.info("**Vector A (Red)**")
    a_x = st.slider("A - X Value", -10, 10, 2, key="ax")
    a_y = st.slider("A - Y Value", -10, 10, 2, key="ay")
with col2:
    st.info("**Vector B (Blue)**")
    b_x = st.slider("B - X Value", -10, 10, 5, key="bx")
    b_y = st.slider("B - Y Value", -10, 10, 0, key="by")

vector_a = np.array([a_x, a_y])
vector_b = np.array([b_x, b_y])
dot_product = np.dot(vector_a, vector_b)

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.grid(True, linestyle='--', alpha=0.6)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.quiver(0, 0, a_x, a_y, angles='xy', scale_units='xy', scale=1, color='#FF4B4B', label='Vector A')
ax.quiver(0, 0, b_x, b_y, angles='xy', scale_units='xy', scale=1, color='#1E88E5', label='Vector B')
ax.legend()
ax.set_aspect('equal')
st.pyplot(fig)

st.subheader("2. The Calculation")
st.code(f"({a_x} * {b_x}) + ({a_y} * {b_y}) = {dot_product}", language="python")

if dot_product > 5: st.success("High Similarity")
elif dot_product < -5: st.error("Opposite Meaning")
else: st.warning("Orthogonal / Unrelated")

st.divider()
st.subheader("3. Knowledge Check")
st.write("Set Vector A to `[0, 5]` and Vector B to `[5, 0]`. What is the Dot Product?")
answer = st.radio("Select result:", ["25", "10", "0", "-5"])
if st.button("Submit Assignment"):
    if answer == "0":
        utils_lms.mark_complete("sprint_1_vectors", xp_reward=150)
    else:
        st.error("Incorrect.")
