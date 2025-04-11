import streamlit as st
import re

st.set_page_config(page_title="🔒 Password Strength Meter", layout="centered")
st.title("🔒 Password Strength Meter")
st.write("Check how strong your password is!")

# User input
password = st.text_input("Enter your password:", type="password")

def check_strength(pwd):
    score = 0
    length_criteria = len(pwd) >= 8
    upper_criteria = bool(re.search(r'[A-Z]', pwd))
    lower_criteria = bool(re.search(r'[a-z]', pwd))
    digit_criteria = bool(re.search(r'\d', pwd))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd))

    # Add score
    score += length_criteria
    score += upper_criteria
    score += lower_criteria
    score += digit_criteria
    score += special_criteria

    if score <= 2:
        return "❌ Weak", "red"
    elif score == 3 or score == 4:
        return "⚠️ Medium", "orange"
    else:
        return "✅ Strong", "green"

if password:
    strength, color = check_strength(password)
    st.markdown(f"**Strength:** <span style='color:{color}'>{strength}</span>", unsafe_allow_html=True)
