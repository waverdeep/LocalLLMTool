import uvicorn
from fastapi import FastAPI
import gradio as gr
from gradio_app.custom_chat.user_interface import custom_chat


app = FastAPI()
demo = gr.TabbedInterface([custom_chat],["Chat"], title="MLT", theme="soft")
app = gr.mount_gradio_app(app, demo, path="/")


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)