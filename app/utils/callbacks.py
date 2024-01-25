import random
import time
from openai import OpenAI
from utils import util
from utils.configs import config
from utils.configs import allowed_models


chat_client = util.register_openai_api_key(config['OPENAI_API_KEY'])


def chat_completion(system_prompt, message, chat_history, chat_id):
    if not chat_id:
        chat_id = time.time()
        
    chat_history.append((message, "you typed: "+message))
    
    return chat_id, chat_history, ""
    

def predict(message, history, connect_key, model_name, system_prompt, temperature):
    global chat_client
    global allowed_models
    global config

    if "gpt" in model_name and chat_client is None:
        yield "Please register the openai api key."
        return

    if model_name not in allowed_models:
        yield "Please select the model again."
        return

    if connect_key != config['MY_ACCESS_KEY']:
        yield "Please check the connect key."
        return

    stream = chat_client.chat.completions.create(
        model=model_name,
        messages= util.get_conversation(system_prompt, history, message),
        temperature=temperature,
        stream=True
    )

    partial_message = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            partial_message = partial_message + chunk.choices[0].delta.content
            yield partial_message
