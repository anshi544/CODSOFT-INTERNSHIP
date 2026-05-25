import streamlit as st
import random
import string

# Page Configuration
st.set_page_config(
    page_title="Secure Password Generator",
    page_icon="🔐",
    layout="centered"
)

# Title
st.title("🔐 Secure Password Generator")
st.write("Generate strong and secure passwords instantly.")

# Sidebar
st.sidebar.header("Password Settings")

password_length = st.sidebar.slider(
    "Select Password Length",
    min_value=4,
    max_value=32,
    value=12
)

include_uppercase = st.sidebar.checkbox(
    "Include Uppercase Letters",
    value=True
)

include_numbers = st.sidebar.checkbox(
    "Include Numbers",
    value=True
)

include_symbols = st.sidebar.checkbox(
    "Include Symbols",
    value=True
)

# Character Selection
characters = string.ascii_lowercase

if include_uppercase:
    characters += string.ascii_uppercase

if include_numbers:
    characters += string.digits

if include_symbols:
    characters += string.punctuation

# Password Generator Function
def generate_password(length):
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate Button
if st.button("Generate Password"):

    password = generate_password(password_length)

    st.success("✅ Password Generated Successfully!")

    st.code(password)

    # Password Strength
    if password_length >= 12 and include_numbers and include_symbols:
        st.info("Strong Password 💪")

    elif password_length >= 8:
        st.warning("Medium Strength Password ⚠️")

    else:
        st.error("Weak Password ❌")

# Footer
st.markdown("---")
st.caption("Developed by Anshika Saxena")
