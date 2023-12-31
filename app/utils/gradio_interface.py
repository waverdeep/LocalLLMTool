import gradio as gr
import time


def echo(message, history, system_prompt, tokens):
    response = f"System prompt: {system_prompt}\n Message: {message}."
    for i in range(min(len(response), int(tokens))):
        time.sleep(0.3)
        yield response[: i+1]


demo = gr.ChatInterface(
    echo, 
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="Ask me a yes or no question", container=False, scale=7),
    title="Yes Man",
    description="Ask Yes Man any question",
    theme="soft",
    examples=["Hello", "Am I cool?", "Are tomatoes vegetables?"],
    cache_examples=True,
    stop_btn=None,
    additional_inputs=[
        gr.Textbox("You are helpful AI.", label="System Prompt"), 
        gr.Slider(10, 100)
    ]
).queue()
    