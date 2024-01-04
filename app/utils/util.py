import time
import pandas as pd
from openai import OpenAI


def register_openai_api_key(api_key):
    if api_key:
        return OpenAI(api_key=api_key)
    else:
        return None


def get_conversation(system_prompt, history, message):
    conversation = []

    if system_prompt != "":
        conversation.append({"role": "system", "content": system_prompt })

    for human, assistant in history:
        conversation.append({"role": "user", "content": human })
        conversation.append({"role": "assistant", "content":assistant})

    conversation.append({"role": "user", "content": message})
    return conversation


def save_button_event(history, title, dataframe):
    id = time.time()

    dataframe.loc[len(dataframe)] = [time.time(), title]


    return f"{history} {title} {dataframe} {type(dataframe)}", dataframe
