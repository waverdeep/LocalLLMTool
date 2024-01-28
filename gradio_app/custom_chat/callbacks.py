import time
from utils import util
from utils import configs


chat_client = util.register_openai_api_key(configs.config['OPENAI_API_KEY'])


def user(chat_id, message, history):
    if not chat_id:
        chat_id = time.time()
    return chat_id, "", history + [[message, None]]


def chat_completion(history, model_name, connect_key, temperature, system_prompt):
    global chat_client

    history[-1][1] = ""

    if "gpt" in model_name and chat_client is None:
        history[-1][1] += "Please register the openai api key."
        yield history
        return
    if model_name not in configs.allowed_models:
        history[-1][1] += "Please select the model again."
        yield history
        return
    if connect_key != configs.config['MY_ACCESS_KEY']:
        history[-1][1] += "Please check the connect key."
        yield history
        return
    
    stream = chat_client.chat.completions.create(
        model=model_name,
        messages= util.get_conversation(system_prompt, history, history[-1][0]),
        temperature=temperature,
        stream=True
    )
    history[-1][1] = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            history[-1][1] += chunk.choices[0].delta.content
            yield history
        