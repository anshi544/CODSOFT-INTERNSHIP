import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Contact Book Manager",
    page_icon="📒",
    layout="centered"
)

# Session State Initialization
if "contacts" not in st.session_state:

    st.session_state.contacts = []

# Title
st.title("📒 Smart Contact Book")
st.write("Store and manage your contacts efficiently.")

# Sidebar
st.sidebar.header("Contact Dashboard")
st.sidebar.info("Manage your contacts easily 📱")

# Contact Input Fields
name = st.text_input("Enter Name")
phone = st.text_input("Enter Phone Number")
email = st.text_input("Enter Email Address")

# Add Contact Button
if st.button("Add Contact"):

    if name and phone and email:

        st.session_state.contacts.append({
            "Name": name,
            "Phone": phone,
            "Email": email
        })

        st.success("Contact Added Successfully!")

    else:
        st.warning("Please fill all fields.")

# Search Feature
st.subheader("🔍 Search Contact")

search = st.text_input("Search by Name")

# Contact Display
st.subheader("📋 Saved Contacts")

filtered_contacts = []

if search:

    for contact in st.session_state.contacts:

        if search.lower() in contact["Name"].lower():
            filtered_contacts.append(contact)

else:

    filtered_contacts = st.session_state.contacts

# Display Contacts
if len(filtered_contacts) == 0:

    st.info("No contacts found.")

else:

    df = pd.DataFrame(filtered_contacts)

    st.dataframe(df, use_container_width=True)

# Delete Contact
st.subheader("❌ Delete Contact")

if len(st.session_state.contacts) > 0:

    contact_names = [
        contact["Name"]
        for contact in st.session_state.contacts
    ]

    selected_contact = st.selectbox(
        "Select Contact to Delete",
        contact_names
    )

    if st.button("Delete Selected Contact"):

        st.session_state.contacts = [

            contact
            for contact in st.session_state.contacts

            if contact["Name"] != selected_contact
        ]

        st.success("Contact Deleted Successfully!")
        st.rerun()

# Footer
st.markdown("---")
st.caption("Developed by Anshika Saxena")
