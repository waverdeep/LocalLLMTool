import gradio as gr
import time


def echo(message, history, system_prompt, tokens):
    response = f"System prompt: {system_prompt}\n Message: {message}."
    for i in range(min(len(response), int(tokens))):
        time.sleep(0.1)
        yield response[: i+1]


chat = gr.ChatInterface(
                echo, 
                chatbot=gr.Chatbot(height="50vh"),
                textbox=gr.Textbox(placeholder="Ask me a question", container=False, scale=7),
                stop_btn=None,
                additional_inputs=[
                    gr.Textbox("You are helpful AI.", label="System Prompt"), 
                    gr.Slider(10, 100)
                ]
            ).queue()

with gr.Blocks(theme="soft") as demo:
    with gr.Row():
        with gr.Column():
            gr.Dropdown(
                choices=[
                    "Mistral-7B-OpenOrca-GGUF"
                ],
                value="Mistral-7B-OpenOrca-GGUF"
            )
            gr.Button(
                value="Submit"
            )
        with gr.Column():
            chat.render()
    