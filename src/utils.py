import requests
from requests.exceptions import RequestException

# from requests.exceptions import HTTPError
import json

BASE_URL = "http://localhost:5000"


# function to register new user
def register_user(st, fullname: str, email: str, password: str) -> bool:
    user_data = {
        "fullname": fullname,
        "email": email,
        "password": password,
    }
    url = f"{BASE_URL}/users/register"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    try:
        response = requests.post(
            url=url,
            data=json.dumps(user_data),
            headers=headers,
        )
        response.raise_for_status()
        if response.status_code == 200:
            return True
        else:
            return False
    except RequestException as e:
        st.error(e.__str__())
        return False
    except Exception as e:
        st.error(e.__str__())
        return False


# function to login user
def login_user(st, email: str, password: str) -> bool:
    auth_data = {
        "email": email,
        "password": password,
    }
    url = f"{BASE_URL}/users/login"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    try:
        response = requests.post(
            url=url,
            data=json.dumps(auth_data),
            headers=headers,
        )
        response.raise_for_status()
        if response.status_code == 200:
            result = response.json()
            st.session_state.logged_in_user = result
            return True
        else:
            return False
    except RequestException as e:
        st.error(e)
        return False
    except Exception as e:
        st.error(e)
        return False


def get_agent_response(st, query: str, user_id: int) -> str:
    input_data = {"message": query}
    url = f"{BASE_URL}/agents/run/{user_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    try:
        response = requests.post(
            url=url,
            data=json.dumps(input_data),
            headers=headers,
        )
        response.raise_for_status()
        return response.json()["response"]
    except RequestException as e:
        st.error(e)
        return f"Error: {e}"
    except Exception as e:
        st.error(e)
        return f"Error: {e}"


def reset_history(st, user_name: str = ""):
    greetings = f"Hello, {user_name}" if user_name else "Hello"
    default_chat_message = {
        "role": "assistant",
        "content": (
            f"{greetings}! How can I assist you with stock analysis "
            "and wiki search today?"
        )
    }
    st.session_state.chat_history = [default_chat_message]
