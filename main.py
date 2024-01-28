import uvicorn
from fastapi import FastAPI
import gradio as gr
from gradio_app.custom_chat.user_interface import custom_chat
from gradio_app.imagine_character.user_interface import imagine_character_ui


app = FastAPI()
demo = gr.TabbedInterface(
    [custom_chat, imagine_character_ui],
    ["Chat", "my character"],
    title="MLT",
    theme="soft"
)
app = gr.mount_gradio_app(app, demo, path="/")


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)