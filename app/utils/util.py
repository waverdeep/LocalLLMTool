from openai import OpenAI


def register_openai_api_key(api_key):
    if secret_key:
        return OpenAI(api_key=secret_key)
    else:
        return None
