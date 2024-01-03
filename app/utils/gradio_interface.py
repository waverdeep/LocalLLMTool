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


def save_chat_history(history):
    chat_history.input(
        inputs=[39203.20, "hello?"]
    )


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
                chat_history = gr.DataFrame(
                    headers=["session_id", "title"],
                    datatype=["float", "str"],
                    value=None,
                )