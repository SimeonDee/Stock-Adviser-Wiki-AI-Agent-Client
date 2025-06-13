import streamlit as st
from src.screens.login_page import login_page
from src.screens.register_page import register_page
from src.screens.main_page import main_page

st.markdown(
    """
    <style>
        button{
            padding: 5px 15px;
            background-color: #888888;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.logged_in_user = None

if "page" not in st.session_state:
    st.session_state.page = "login"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


def main_app():
    if not st.session_state.logged_in:
        if st.session_state.page == "login":
            login_page(st)
        elif st.session_state.page == "register":
            register_page(st)
    else:
        main_page(st)


main_app()
