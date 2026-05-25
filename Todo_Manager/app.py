import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="To-Do Manager",
    page_icon="📝",
    layout="centered"
)

# Session State for Task Storage
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Title
st.title("📝 Smart To-Do Manager")
st.write("Organize your daily tasks efficiently.")

# Sidebar
st.sidebar.header("Task Settings")
st.sidebar.info("Stay productive every day 🚀")

# Task Input
task = st.text_input("Enter a New Task")

priority = st.selectbox(
    "Select Priority",
    ["High", "Medium", "Low"]
)

# Add Task Button
if st.button("Add Task"):

    if task != "":

        st.session_state.tasks.append({
            "task": task,
            "priority": priority,
            "completed": False
        })

        st.success("Task Added Successfully!")

    else:
        st.warning("Please enter a task.")

# Display Tasks
st.subheader("📋 Your Tasks")

if len(st.session_state.tasks) == 0:
    st.info("No tasks added yet.")

for index, item in enumerate(st.session_state.tasks):

    col1, col2 = st.columns([6, 1])

    with col1:

        completed = st.checkbox(
            f"{item['task']} ({item['priority']})",
            value=item["completed"],
            key=index
        )

        st.session_state.tasks[index]["completed"] = completed

    with col2:

        if st.button("❌", key=f"delete_{index}"):

            st.session_state.tasks.pop(index)
            st.rerun()

# Progress Tracking
completed_tasks = sum(
    task["completed"] for task in st.session_state.tasks
)

total_tasks = len(st.session_state.tasks)

if total_tasks > 0:

    progress = completed_tasks / total_tasks

    st.progress(progress)

    st.write(
        f"Completed {completed_tasks} out of {total_tasks} tasks."
    )

# Footer
st.markdown("---")
st.caption("Developed by Anshika Saxena")
