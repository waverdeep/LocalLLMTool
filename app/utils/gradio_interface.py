import os
import time
import gradio as gr

import utils.util as util


allowed_models = [
    "gpt-3.5-turbo-1106",
    "gpt-4-1106-preview",
]

config = {
    "OPENAI_API_KEY": os.environ.get('OPENAI_API_KEY', None),
    "MY_ACCESS_KEY": os.environ.get('MY_ACCESS_KEY', None),
}

chat_client = util.register_openai_api_key(config['OPENAI_API_KEY'])
initial_dataframe = pd.DataFrame({"Column1": [], "Column2": []})


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


def save_chat_history(history):
    pass


def update_dataframe():
    # 여기에 데이터 프레임을 갱신하는 코드를 작성합니다.
    # 예: 새로운 행 추가
    new_row = {"Column1": "New Value1", "Column2": "New Value2"}
    updated_dataframe = initial_dataframe.append(new_row, ignore_index=True)
    return updated_dataframe


chat = gr.ChatInterface(
    util.predict,
    chatbot=gr.Chatbot(height="60vh"),
    textbox=gr.Textbox(
        placeholder="무엇이든 물어보세요!", 
        container=False, 
        scale=7
    ),
    stop_btn=None,
    additional_inputs_accordion_name="configurations",
    additional_inputs=[
        gr.Dropdown(
            choices=allowed_models,
            value="gpt-3.5-turbo-1106",
            interactive=True,
            label="selet model"
        ),
        gr.Textbox(
            "", 
            label="system prompt"), 
        gr.Slider(
            minimum=0, 
            maximum=1, 
            step=0.1,
            value=0.5,
            label="temperature"),
        gr.Textbox(
            label="my access key",
            type="password"
        ),
    ],
).queue()


with gr.Blocks(theme="soft", title="MLT",) as demo:
    with gr.Row():
        with gr.Column(scale=7):
            chat.render()
        with gr.Column(scale=3):
            with gr.Blocks():
                gr.Label(
                    value="Additional Tools"
                )
                save_button = gr.Button(
                    value="Save chat history",
                )
                save_button.click(
                    save_chat_history,
                    inputs=[chat.chatbot],
                    outputs=None
                )
                gr.Interface(
                    fn=update_dataframe,
                    inputs=gr.Button(),
                    outputs="dataframe"
                )