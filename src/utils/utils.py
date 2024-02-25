import os


def fetch_openai_key():
    try:
        return os.environ.get("OPENAI_API_KEY")
    except Exception as e:
        raise EnvironmentError(f"Failed to read OpenAI key - {e}")


def fetch_fitbit_keys():
    try:
        client_id = os.environ.get("FITBIT_CLIENT_ID")
        client_secret = os.environ.get("FITBIT_CLIENT_SECRET")
        return [client_id, client_secret]
    except Exception as e:
        raise EnvironmentError(f"Failed to read FitBit keys - {e}")
