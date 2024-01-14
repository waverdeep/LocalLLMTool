# import utils.gradio_interface as gradio_interface
import gradio as gr
from quick_chat.user_interface import quick_chat
from custom_chat.user_interface import custom_chat


if __name__ == '__main__':
    demo = gr.TabbedInterface([quick_chat.render(), custom_chat],["Quick", "Chat"], title="MLT", theme="soft")

    demo.launch(
        server_name="0.0.0.0",
        server_port=6007
    )