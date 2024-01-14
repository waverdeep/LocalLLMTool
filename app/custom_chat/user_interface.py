import gradio as gr
from utils import configs
from custom_chat import callbacks


with gr.Blocks() as custom_chat:
    with gr.Row():
        with gr.Column(scale=7):
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
                )
        with gr.Column(scale=3):
            with gr.Group():
                chat_id_textbox = gr.Textbox(
                    interactive=False,
                    label="chat id"
                )
            model_dropdown = gr.Dropdown(
                choices=configs.allowed_models,
                value="gpt-3.5-turbo-1106",
                interactive=True,
                label="selet model"
            )
            system_prompt_textbox = gr.Textbox(
                label="system prompt",
            )
            temperature_slider = gr.Slider(
                minimum=0, 
                maximum=1, 
                step=0.1,
                value=0.5,
                label="temperature"
            )
            access_key_textbox = gr.Textbox(
                label="connect key",
                type="password"
            )

    send_button.click(
        callbacks.user,
        inputs=[chat_id_textbox, input_textbox, chatbot],
        outputs=[chat_id_textbox, input_textbox, chatbot]
    ).then(
        callbacks.chat_completion,
        inputs=[chatbot, model_dropdown, access_key_textbox, temperature_slider, system_prompt_textbox],
        outputs=[chatbot]
    )