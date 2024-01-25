import gradio as gr
from quick_chat import callbacks
from utils import configs


with gr.ChatInterface(
    callbacks.predict,
    additional_inputs=[
        gr.Textbox(
            type="password",
            label="connect key"
        ),
        gr.Dropdown(
            choices=configs.allowed_models,
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