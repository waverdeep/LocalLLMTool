from utils import util
from utils import configs


chat_client = util.register_openai_api_key(configs.config['OPENAI_API_KEY'])


def predict(message, history, connect_key, model_name, system_prompt, temperature):
    global chat_client

    if "gpt" in model_name and chat_client is None:
        yield "Please register the openai api key."
        return

    if model_name not in configs.allowed_models:
        yield "Please select the model again."
        return

    if connect_key != configs.config['MY_ACCESS_KEY']:
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
