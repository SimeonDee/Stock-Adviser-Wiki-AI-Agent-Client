from src.utils import get_agent_response, reset_history


# Main Page
def main_page(st):
    # ensure only authenticated user can access this page
    if (
        "logged_in_user" not in st.session_state or
        st.session_state.logged_in_user is None
    ):  # no-qa
        st.session_state.logged_in_user = None
        st.session_state.logged_in = False
        st.session_state.page = "login"

    # Reset chat history and diplay main page elements
    reset_history(
        st,
        user_name=st.session_state.logged_in_user['fullname'].split()[0],
    )
    _, col2, col3 = st.columns([5, 2, 1])
    with col2:
        st.write(
            f"Welcome, ***{st.session_state.logged_in_user['fullname']}***"
        )
    with col3:
        logout_btn = st.button("Logout", type="primary")
        if logout_btn:
            st.session_state.logged_in_user = None
            st.session_state.logged_in = False
            st.session_state.page = "login"
            st.session_state.chat_history = []  # reset history
    st.write("")
    with st.container(border=True):
        st.write("### Chat with Stock Adviser and Wiki Search AI Agent")
        st.write("Type a message and press Enter to send it to the AI")

        with st.container(border=True):
            chat_interface = st.container()
            # Display chat history
            for message in st.session_state.chat_history:
                with chat_interface.chat_message(message["role"]):
                    st.write(message["content"])

            # Get user input
            st.write("")
            st.write("")
            user_input = st.chat_input(placeholder="Type your message here...")

            if user_input:
                # add user message to chat history
                st.session_state.chat_history.append({
                    "role": "user", "content": user_input
                })

                # Display user message
                with chat_interface.chat_message("user"):
                    st.write(user_input)

                # Get API response
                agent_response = get_agent_response(
                    st=st,
                    query=user_input,
                    user_id=st.session_state.logged_in_user["id"],
                )

                # Add agent response to chat history
                st.session_state.chat_history.append({
                    "role": "assistant", "content": agent_response
                })

                # Display user message
                with chat_interface.chat_message("assistant"):
                    st.write(agent_response)
