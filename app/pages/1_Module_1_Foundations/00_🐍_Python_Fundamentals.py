import streamlit as st
import utils_lms
import os

st.set_page_config(page_title="M1: Python Fundamentals", page_icon="🐍")
user = utils_lms.get_current_user()
if not user:
    st.warning("🔒 Please login on the Home page to access this lesson.")
    st.stop()

# Derive lesson_id from filename
lesson_id = os.path.splitext(os.path.basename(__file__))[0].lower().replace('_', '-')


st.title("🐍 Python Fundamentals")
st.markdown("""
Welcome to the first step on your journey to becoming an AI Engineer! A strong foundation in Python is essential.

### 1. Basic Data Types
In Python, you'll work with several fundamental data types:
- **Integers**: Whole numbers, like `10`, `-5`, `0`.
- **Floats**: Numbers with a decimal point, like `3.14`, `-0.001`.
- **Strings**: Text, enclosed in quotes, like `"Hello, World!"`.
- **Booleans**: Logical values, either `True` or `False`.

```python
# Examples
an_integer = 10
a_float = 3.14
a_string = "Hello"
a_boolean = True
```

### 2. Data Structures
You'll also need to store collections of data.
- **Lists**: Ordered, changeable collections. `my_list = [1, 2, "apple"]`
- **Dictionaries**: Unordered collections of key-value pairs. `my_dict = {"name": "Alice", "age": 30}`

```python
# Examples
ages = [25, 30, 35]
person = {"first_name": "John", "last_name": "Doe"}
print(f"The first age is {ages[0]}")
print(f"{person['first_name']} is {ages[1]} years old.")
```
""")

st.divider()
st.subheader("3. Knowledge Check")
data = utils_lms.load_data()


if lesson_id in data[user]["completed"]:
    st.info("You have already completed this lesson and earned 50 XP.")
    st.page_link("pages/1_Module_1_Foundations/01_📐_The_Dot_Product.py", label="Next Lesson: The Dot Product", icon="📐")
else:
    st.write("What data type would you use to store a person's age?")
    answer = st.radio("Select the best data type:", ["String", "Integer", "Boolean", "Float"])
    if st.button("Submit Assignment"):
        if answer == "Integer":
            utils_lms.mark_complete(lesson_id, xp_reward=50)
            st.page_link("pages/1_Module_1_Foundations/01_📐_The_Dot_Product.py", label="Next Lesson: The Dot Product", icon="📐")
        else:
            st.error("Not quite. While you could store an age as a string or float, Integer is the most appropriate and common data type for whole numbers like age.")
