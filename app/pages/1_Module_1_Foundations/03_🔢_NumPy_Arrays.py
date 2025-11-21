import streamlit as st
import utils_lms
import os
import numpy as np

st.set_page_config(page_title="M1: NumPy Arrays", page_icon="🔢")
user = utils_lms.get_current_user()
if not user:
    st.warning("🔒 Please login on the Home page to access this lesson.")
    st.stop()

# Derive lesson_id from filename
lesson_id = os.path.splitext(os.path.basename(__file__))[0].lower().replace('_', '-')
data = utils_lms.load_data()

# Check for previous lesson completion
if "02-embeddings" not in data[user]["completed"]:
    st.error("🚫 Complete the previous lesson first.")
    st.page_link("pages/1_Module_1_Foundations/02_🧬_Embeddings.py", label="Go to Embeddings lesson", icon="🧬")
    st.stop()

st.title("🔢 NumPy Arrays")
st.markdown("""
NumPy is a fundamental library for numerical computing in Python. It provides a powerful N-dimensional array object.

### 1. Creating NumPy Arrays
You can create a NumPy array from a Python list.
```python
import numpy as np

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array)
# Output: [1 2 3 4 5]
```

### 2. Array Operations
You can perform mathematical operations on the entire array at once.
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
print(a + b)
# Output: [5 7 9]

# Scalar multiplication
print(a * 2)
# Output: [2 4 6]
```
""")

st.divider()
st.subheader("3. Knowledge Check")

if lesson_id in data[user]["completed"]:
    st.info("You have already completed this lesson and earned 50 XP.")
    st.page_link("pages/1_Module_1_Foundations/04_🐼_Pandas_DataFrames.py", label="Next Lesson: Pandas DataFrames", icon="🐼")
else:
    st.write("What is the result of the following code?")
    st.code("np.array([1, 2, 3]) + 5")
    answer = st.radio("Select the result:", ["Error", "[6, 7, 8]", "[1, 2, 3, 5]"])
    if st.button("Submit Assignment"):
        if answer == "[6, 7, 8]":
            utils_lms.mark_complete(lesson_id, xp_reward=50)
            st.page_link("pages/1_Module_1_Foundations/04_🐼_Pandas_DataFrames.py", label="Next Lesson: Pandas DataFrames", icon="🐼")
        else:
            st.error("Incorrect. NumPy performs element-wise operations, so 5 is added to each element in the array.")
