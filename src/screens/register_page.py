import time
from src.utils import register_user


def register_page(st):
    st.title("Register New User")
    back_to_login = st.button("Back to Login Page", type="secondary")
    with st.form("register_form"):
        fullname = st.text_input("Full Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Register")
        if submitted:
            if register_user(st, fullname, email, password):
                st.success("Registered Successfully")
                time.sleep(2)
                st.session_state.logged_in = False
                st.session_state.page = "login"
                st.rerun()
            else:
                st.error("Registration failed. Check your input.")
    if back_to_login:
        st.session_state.logged_in = False
        st.session_state.page = "login"
