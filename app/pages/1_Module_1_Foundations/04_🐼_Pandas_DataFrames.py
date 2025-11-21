import streamlit as st
import utils_lms
import os
import pandas as pd

st.set_page_config(page_title="M1: Pandas DataFrames", page_icon="🐼")
user = utils_lms.get_current_user()
if not user:
    st.warning("🔒 Please login on the Home page to access this lesson.")
    st.stop()

# Derive lesson_id from filename
lesson_id = os.path.splitext(os.path.basename(__file__))[0].lower().replace('_', '-')
data = utils_lms.load_data()

# Check for previous lesson completion
if "03-numpy-arrays" not in data[user]["completed"]:
    st.error("🚫 Complete the previous lesson first.")
    st.page_link("pages/1_Module_1_Foundations/03_🔢_NumPy_Arrays.py", label="Go to NumPy lesson", icon="🔢")
    st.stop()

st.title("🐼 Pandas DataFrames")
st.markdown("""
Pandas is a library for data manipulation and analysis. Its primary data structure is the DataFrame.

### 1. Creating a DataFrame
You can create a DataFrame from a dictionary.
```python
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)
st.dataframe(df)
```
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)
st.dataframe(df)

### 2. Selecting Data
You can select columns and rows from a DataFrame.
```python
# Select a column
ages = df['Age']
st.write("Ages:")
st.write(ages)

# Select rows based on a condition
over_30 = df[df['Age'] > 30]
st.write("Users over 30:")
st.dataframe(over_30)
```
ages = df['Age']
st.write("Ages:")
st.write(ages)
over_30 = df[df['Age'] > 30]
st.write("Users over 30:")
st.dataframe(over_30)
""")

st.divider()
st.subheader("3. Knowledge Check")

if lesson_id in data[user]["completed"]:
    st.info("You have already completed this lesson and earned 50 XP.")
    st.success("🎉 Module 1 Complete! 🎉")
    st.page_link("Home.py", label="Back to Home", icon="🏠")
else:
    st.write("Which line of code selects the 'Name' column from a DataFrame named `df`?")
    answer = st.radio("Select the correct code:", ["df['Name']", "df.Name", "df.get('Name')", "All of the above"])
    if st.button("Submit Assignment"):
        if answer == "All of the above":
            utils_lms.mark_complete(lesson_id, xp_reward=50)
            st.success("🎉 Module 1 Complete! 🎉")
            st.page_link("Home.py", label="Back to Home", icon="🏠")
        else:
            st.error("Incorrect. While df['Name'] is the most common, all of these are valid ways to select a column in Pandas.")
