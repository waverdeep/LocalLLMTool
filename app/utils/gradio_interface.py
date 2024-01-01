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

with gr.Group() as head_info_group:
    gr.Dropdown(
        choices=[
            "Mistral-7B-OpenOrca-GGUF",
            "Mistral-7B-Instruct-v0.2",
            "OpenAI-GPT-3.5-Turbo"
        ]
    )
    gr.Button(
        value="Select Model"
    )

with gr.Blocks(theme="soft") as demo:
    with gr.Row():
        with gr.Column():
            gr.Label(
                value="MyLLMTools by waverDeep"
            )
    with gr.Row():
        with gr.Column():
            head_info_group.render()
            
        with gr.Column():
            chat.render()
    