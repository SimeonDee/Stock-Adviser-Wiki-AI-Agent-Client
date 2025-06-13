from src.utils import login_user


# Login Page
def login_page(st):
    col1, col2 = st.columns([5, 1])
    col1.title("Login")
    register_nav = col2.button("Sign Up!", type="secondary")
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        _, col = st.columns([2, 2])
        with col:
            login = st.form_submit_button("Login", type="primary")
        if login:
            if login_user(st, email, password):
                st.session_state.logged_in = True
                st.session_state.page = "home"
            else:
                st.error("Authentication failed. Check your credentials.")
                st.session_state.logged_in = False
                st.session_state.page = "login"

    if register_nav:
        st.session_state.logged_in = False
        st.session_state.page = "register"
