import streamlit as st

# Page Settings
st.set_page_config(
    page_title="Smart Calculator",
    page_icon="🧮",
    layout="centered"
)

# Title
st.title("🧮 Smart Calculator")
st.write("Perform basic calculations instantly.")

# Sidebar
st.sidebar.header("Settings")

theme = st.sidebar.selectbox(
    "Choose Theme",
    ["Light", "Dark"]
)

if theme == "Dark":
    st.sidebar.success("Dark Mode Enabled")
else:
    st.sidebar.info("Light Mode Enabled")

# Number Inputs
num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

# Operation Selection
operation = st.selectbox(
    "Choose Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Calculate Button
if st.button("Calculate"):

    if operation == "Addition":
        result = num1 + num2

    elif operation == "Subtraction":
        result = num1 - num2

    elif operation == "Multiplication":
        result = num1 * num2

    elif operation == "Division":

        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

    st.success(f"✅ Result: {result}")

# Footer
st.markdown("---")
st.caption("Developed by Anshika Saxena")
