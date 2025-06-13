# Define variables
APP_NAME = client
CLIENT_FILE_NAME = client.py
VENV_NAME = .venv


# installs "uv" and use it to Create a virtual env
venv:
	pip install uv
	uv init .
	uv venv $(VENV_NAME)

python-upgrade:
	uv venv -p 3.12.4 --allow-existing

# Install dependencies
install:
	uv add requests streamlit

# Installs "streamlit" and Run the Client (Streamlit) app
run-client:
	streamlit run $(CLIENT_FILE_NAME)

# Clean resources
clean:
	rm -rf $(VENV_NAME)
	rm -rf __pychache__
