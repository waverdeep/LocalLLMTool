import gradio as gr
import time

from langchain.chat_models import ChatOpenAI


chat_model = None


def allocate_model(model_name, private_key):
    if model_name == "LangChain-OpenAI-GPT-3.5-turbo":
        chat_model = ChatOpenAI(
            openai_api_key=private_key, 
            model="gpt-3.5-turbo"
        )
        return {model_name: 1}
    else:
        chat_model = None
        return {}


def echo(predict, history, system_prompt, temperature):
    history_langchain_format = []
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))
    history_langchain_format.append(HumanMessage(content=message))
    gpt_response = llm(history_langchain_format)
    yield gpt_response.content


chat = gr.ChatInterface(
    predict, 
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
    title="MLT",) as demo:
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
                        "LangChain-OpenAI-GPT-3.5-turbo"
                    ],
                    value="Mistral-7B-OpenOrca-GGUF",
                    interactive=True,
                    label="selet model"
                )
                private_key = gr.Textbox(
                    label="private key"
                )
                allocated_model = gr.Label(
                    label="result"
                )
                allocate_button = gr.Button(
                    value="Allocate"
                )
                allocate_button.click(
                    fn=allocate_model,
                    inputs=[model_dropdown, private_key],
                    outputs=[allocated_model],
                    api_name="allocate_model"
                )
        with gr.Column():
            chat.render()
    