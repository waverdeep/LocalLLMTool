import gradio as gr
import time


def echo(message, history, system_prompt, tokens):
    response = f"System prompt: {system_prompt}\n Message: {message}."
    for i in range(min(len(response), int(tokens))):
        time.sleep(0.3)
        yield response[: i+1]


chat = gr.ChatInterface(
                echo, 
                chatbot=gr.Chatbot(height="70vh"),
                textbox=gr.Textbox(placeholder="Ask me a yes or no question", container=False, scale=7),
                title="MyLLMTool__",
                description="재미있는 무언가를 만들어보자\nby waverDeep",
                theme="soft",
                stop_btn=None,
                additional_inputs=[
                    gr.Textbox("You are helpful AI.", label="System Prompt"), 
                    gr.Slider(10, 100)
                ]
            ).queue()

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            gr.Dropdown(
                choices=[
                    "Mistral-7B-OpenOrca-GGUF"
                ]
            )
            gr.Button(
                value="Submit"
            )
        with gr.Column():
            chat.render()
    