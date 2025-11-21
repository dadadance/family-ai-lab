import json
import os
import streamlit as st
from datetime import datetime

DATA_FILE = "data/users.json"

def load_data():
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists(DATA_FILE):
        default_data = {
            "Husband": {"xp": 0, "completed": [], "joined": str(datetime.now().date())},
            "Wife": {"xp": 0, "completed": [], "joined": str(datetime.now().date())}
        }
        with open(DATA_FILE, "w") as f:
            json.dump(default_data, f)
        return default_data
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def get_current_user():
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None
    return st.session_state.current_user

def set_user(name):
    st.session_state.current_user = name
    st.rerun()

def mark_complete(lesson_id, xp_reward=100):
    user = get_current_user()
    if not user:
        st.error("Please login on the Home page first!")
        return
    data = load_data()
    if lesson_id not in data[user]["completed"]:
        data[user]["completed"].append(lesson_id)
        data[user]["xp"] += xp_reward
        save_data(data)
        st.balloons()
        st.success(f"Lesson Completed! +{xp_reward} XP")
    else:
        st.info("You have already completed this lesson.")
