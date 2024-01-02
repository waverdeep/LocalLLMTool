from openai import OpenAI


def register_openai_api_key(api_key):
    if api_key:
        return OpenAI(api_key=api_key)
    else:
        return None
