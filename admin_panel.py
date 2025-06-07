import streamlit as st

def show_admin():
    st.title("Admin Panel")
    st.text_input("Admin Password")
    st.text_area("Edit Configuration (YAML)", height=200)
    if st.button("Save Config"):
        st.success("Saved successfully.")