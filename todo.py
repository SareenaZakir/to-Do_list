import streamlit as st

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("📝 To-Do List App")
st.write("Add, complete, and delete your daily tasks easily.")

# Input for new task
new_task = st.text_input("Enter a new task")

col1, col2 = st.columns([1, 3])

# Add task button
with col1:
    if st.button("➕ Add"):
        if new_task.strip() != "":
            st.session_state.tasks.append({"task": new_task, "done": False})
            st.rerun()  # Clear input
        else:
            st.warning("Task cannot be empty!")

# Safely track which task to delete
task_to_delete = None

# Display tasks
if st.session_state.tasks:
    st.subheader("Your Tasks:")
    for i, task in enumerate(st.session_state.tasks):
        cols = st.columns([0.1, 0.75, 0.15])
        # Checkbox for completion
        is_done = cols[0].checkbox("", task["done"], key=f"check_{i}")
        st.session_state.tasks[i]["done"] = is_done

        # Display task
        task_text = f"~~{task['task']}~~" if is_done else task["task"]
        cols[1].markdown(task_text)

        # Delete button — mark for deletion, don't delete here
        if cols[2].button("❌", key=f"del_{i}"):
            task_to_delete = i

    # Perform deletion after the loop to avoid crash
    if task_to_delete is not None:
        st.session_state.tasks.pop(task_to_delete)
        st.rerun()
else:
    st.info("No tasks added yet.")
