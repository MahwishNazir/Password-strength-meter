import streamlit as st
import re

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Upper and Lowercase check
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1

    # Number check
    if re.search(r"\d", password):
        score += 1

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Password strength evaluation
    if score <= 2:
        return "Weak 🔴"
    elif score == 3:
        return "Medium 🟡"
    elif score == 4:
        return "Strong 🟢"
    else:
        return "Very Strong 💪"

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.write("Enter a password below to check its strength.")

password = st.text_input("Enter Password", type="password")

if password:
    strength = check_password_strength(password)
    
    # Show strength result
    st.subheader(f"Password Strength: {strength}")
    
    # Show progress bar based on strength
    strength_map = {"Weak 🔴": 0.25, "Medium 🟡": 0.5, "Strong 🟢": 0.75, "Very Strong 💪": 1.0}
    st.progress(strength_map[strength])
