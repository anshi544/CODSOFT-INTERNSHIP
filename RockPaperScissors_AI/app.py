import streamlit as st
import random

# Page Configuration
st.set_page_config(
    page_title="AI Rock Paper Scissors",
    page_icon="🎮",
    layout="centered"
)

# Session State Initialization
if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "history" not in st.session_state:
    st.session_state.history = []

# Title
st.title("🎮 AI Rock Paper Scissors")
st.write("Challenge the computer and test your luck!")

# Sidebar
st.sidebar.header("Game Dashboard")
st.sidebar.info("Can you beat the AI? 🤖")

# User Choice
user_choice = st.selectbox(
    "Choose Your Move",
    ["Rock", "Paper", "Scissors"]
)

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Play Button
if st.button("Play Game"):

    computer_choice = random.choice(choices)

    # Winner Logic
    if user_choice == computer_choice:
        result = "It's a Tie!"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or
        (user_choice == "Paper" and computer_choice == "Rock")
        or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):

        result = "You Win! 🎉"
        st.session_state.user_score += 1

    else:
        result = "Computer Wins! 🤖"
        st.session_state.computer_score += 1

    # Store History
    st.session_state.history.append({
        "You": user_choice,
        "Computer": computer_choice,
        "Result": result
    })

    # Display Results
    st.success(f"Your Choice: {user_choice}")
    st.info(f"Computer Choice: {computer_choice}")
    st.warning(result)

# Scoreboard
st.subheader("🏆 Scoreboard")

col1, col2 = st.columns(2)

with col1:
    st.metric("Your Score", st.session_state.user_score)

with col2:
    st.metric("Computer Score", st.session_state.computer_score)

# Game History
st.subheader("📜 Match History")

if len(st.session_state.history) == 0:
    st.write("No games played yet.")

for game in st.session_state.history:

    st.write(
        f"You: {game['You']} | "
        f"Computer: {game['Computer']} | "
        f"Result: {game['Result']}"
    )

# Reset Button
if st.button("Reset Game"):

    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.history = []

    st.success("Game Reset Successfully!")

# Footer
st.markdown("---")
st.caption("Developed by Anshika Saxena")
