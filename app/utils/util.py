from openai import OpenAI


def register_openai_api_key(api_key):
    if api_key:
        return OpenAI(api_key=api_key)
    else:
        return None


def predict(message, history, model_name, system_prompt, temperature, access_key):
    global chat_client
    global allowed_models
    global config

    if "gpt" in model_name and chat_client is None:
        yield "Please register the openai api key."
        return

    if model_name not in allowed_models:
        yield "Please select the model again."
        return

    if access_key != config['MY_ACCESS_KEY']:
        yield "Please check the my access key."
        return

    history_openai_format = []
    if system_prompt != "":
        history_openai_format.append({"role": "system", "content": system_prompt })
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})

    stream = chat_client.chat.completions.create(
        model=model_name,
        messages= history_openai_format,
        temperature=temperature,
        stream=True
    )

    partial_message = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            partial_message = partial_message + chunk.choices[0].delta.content
            yield partial_message
            

