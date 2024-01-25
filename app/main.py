# import utils.gradio_interface as gradio_interface
import gradio as gr
from quick_chat.user_interface import quick_chat
from custom_chat.user_interface import custom_chat
from imagine.user_interface import imagine


if __name__ == '__main__':
    demo = gr.TabbedInterface([custom_chat, imagine],["Chat", "Imagine"], title="MLT", theme="soft")

    demo.launch(
        server_name="0.0.0.0",
        server_port=6007
    )