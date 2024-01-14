import gradio as gr
from imagine import callbacks


with gr.Blocks() as imagine:
    with gr.Row():
        with gr.Column(scale=3):
            access_key_textbox = gr.Textbox(
                label="connect key",
                type="password"
            )
            input_prompt = gr.Textbox(
                label="input prompt",
                interactive=True,
                lines=3,
                max_lines=5
            )
            imagine_button = gr.Button(
                value="imagine"
            )
            model_dropdown = gr.Dropdown(
                interactive=True,
                choices=[
                    "dall-e-2",
                    "dall-e-3"
                ],
                value="dall-e-2"
            )
    with gr.Row():
        imagin_image = gr.Image()

    imagine_button.click(
        callbacks.imagine,
        inputs=[access_key_textbox, model_dropdown, input_prompt],
        outputs=[imagin_image]
    )
