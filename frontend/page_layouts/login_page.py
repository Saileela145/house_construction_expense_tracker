import streamlit as st
from services.api_client import login

def login_form():
    st.title("HC_Expense Tracker Login")

    email = st.text_input("Email", placeholder="Enter your email")
    password = st.text_input("Password", type="password",placeholder="Enter your password")

    if st.button("Login"):
        res = login(email, password)

        if res.status_code == 200:
            data = res.json()
            st.session_state.token = data["access_token"]
            st.session_state.authenticated = True

            # Store user info in session
            st.session_state["user"] = email
            st.session_state["logged_in"] = True

            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid credentials")
            