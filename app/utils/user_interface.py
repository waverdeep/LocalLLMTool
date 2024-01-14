import gradio as gr
from utils.configs import *
from utils.callbacks import *


with gr.Blocks() as config_demo:
    with gr.Row():
        with gr.Column():
            model_dropdown = gr.Dropdown(
                choices=allowed_models,
                value="gpt-3.5-turbo-1106",
                interactive=True,
                label="selet model"
            )
            system_prompt_textbox = gr.Textbox(
                label="system prompt",
            ), 
            temerature_silder = gr.Slider(
                minimum=0, 
                maximum=1, 
                step=0.1,
                value=0.5,
                label="temperature"
            ),
            access_key_textbox = gr.Textbox(
                label="my access key",
                type="password"
            ),


with gr.Blocks() as history_demo:
    with gr.Row():
        with gr.Column(scale=3):
            gr.Label(
                value="Chat History"
            )
        with gr.Column(scale=7):
            history_chatbot = gr.Chatbot(
                show_copy_button=True
            )
            

with gr.Blocks() as chat_demo:
    with gr.Group():
        chat_id_textbox = gr.Textbox(
            interactive=False,
            label="chat id"
        )
    chatbot = gr.Chatbot()
    with gr.Group():
        input_textbox = gr.Textbox(
            show_label=False,
            interactive=True,
            container=False,
            max_lines=5
        )
        send_button = gr.Button(
            value="Send",
            interactive=True,
        ).click(
            chat_completion,
            inputs=[system_prompt_textbox[0], input_textbox, chatbot, chat_id_textbox],
            outputs=[chat_id_textbox, chatbot, input_textbox]
        )

with gr.ChatInterface(
    predict,
    additional_inputs=[
        gr.Textbox(
            type="password",
            label="connect key"
        ),
        gr.Dropdown(
            choices=allowed_models,
            value="gpt-3.5-turbo-1106",
            interactive=True,
            label="selet model"
        ),
        gr.Textbox(
            label="system prompt",
        ), 
        gr.Slider(
            minimum=0, 
            maximum=1, 
            step=0.1,
            value=0.5,
            label="temperature"
        )
    ]
).queue() as quick_chat:
    pass
    

demo = gr.TabbedInterface([quick_chat.render(), chat_demo, history_demo, config_demo],["Quick", "Chat", "history", "Config"], title="MLT", theme="soft")