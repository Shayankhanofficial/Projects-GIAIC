import streamlit as st
import datetime

st.set_page_config(page_title="🌱 Growth Mindset Tracker", layout="centered")
st.title("🌱 Growth Mindset Tracker")
st.write("Reflect, grow, and celebrate your learning journey.")

# Journal Entry
st.subheader("📝 Daily Reflection")
today = datetime.date.today()
journal = st.text_area("What did you learn today or struggle with?", key=str(today))

# Store entry
if st.button("Save Entry"):
    with open("journal_entries.txt", "a") as file:
        file.write(f"{today} - {journal}\n")
    st.success("Entry saved! 🌟")

# Motivation
st.subheader("💡 Growth Mindset Quote")
quotes = [
    "Mistakes are proof that you are trying.",
    "Challenges help us grow.",
    "Effort is the path to mastery.",
    "Failure is a stepping stone to success.",
]
import random
st.info(random.choice(quotes))

# Progress Tracker (optional)
st.subheader("🎯 Goal Tracker")
goal = st.text_input("Set a goal for this week:")
if st.button("Save Goal"):
    with open("goals.txt", "a") as file:
        file.write(f"{today} - {goal}\n")
    st.success("Goal saved! 🚀")
