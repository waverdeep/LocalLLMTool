import gradio as gr
import time


def allocate_model():
    pass


def echo(message, history, system_prompt, tokens):
    response = f"System prompt: {system_prompt}\n Message: {message}."
    for i in range(len(response)):
        time.sleep(0.1)
        yield response[: i+1]


chat = gr.ChatInterface(
    echo, 
    chatbot=gr.Chatbot(height="50vh"),
    textbox=gr.Textbox(
        placeholder="ask me a question", 
        container=False, 
        scale=7
    ),
    stop_btn=None,
    additional_inputs=[
        gr.Textbox(
            "You are helpful AI.", 
            label="system prompt"), 
        gr.Slider(
            minimum=0, 
            maximum=1, 
            step=0.1,
            value=0.5,
            label="temperature")
    ],
).queue()

with gr.Blocks(
    theme="soft",
    title="MyLLMTool",
    head="MyLLMTool by waverDeep") as demo:
    with gr.Row():
        with gr.Column():
            gr.Label(
                value="MyLLMTools by waverDeep"
            )
    with gr.Row():
        with gr.Column():
            with gr.Group():
                model_dropdown = gr.Dropdown(
                    choices=[
                        "Mistral-7B-OpenOrca-GGUF",
                        "OpenAI-GPT-3.5-Turbo"
                    ],
                    value="Mistral-7B-OpenOrca-GGUF",
                    interactive=True,
                    label="selet model"
                )
                allocate_button = gr.Button(
                    value="Allocate"
                )
                allocate_button.click(
                    fn=allocate_model,
                    inputs=model_dropdown,
                    outputs=None,
                    api_name="allocate_model"
                )
        with gr.Column():
            chat.render()
    