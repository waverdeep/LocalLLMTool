import gradio as gr
from utils import configs
from gradio_app.imagine_character import callbacks


with gr.Blocks() as imagine_character_ui:
    with gr.Row():
        with gr.Column(scale=7):
            imagine_image = gr.Image()
        with gr.Column(scale=3):
            access_key_textbox = gr.Textbox(
                label="connect key",
                type="password"
            )
            input_prompt = gr.Textbox(
                label="input character",
                interactive=True,
                lines=2,
                max_lines=5
            )
            default_prompt = gr.Textbox(
                label="default prompt",
                interactive=True,
                value="TRPG, 던전월드, 정방형, 판타지, 상반신 초점 아이콘"
            )
            generate_prompt_button = gr.Button(
                value="generate label",
            )
            generate_prompt_textbox = gr.Textbox(
                label="generated prompt"
            )
            imagine_button = gr.Button(
                value="imagine"
            )
            imagine_model_dropdown = gr.Dropdown(
                label="select imagine model",
                interactive=True,
                choices=[
                    "dall-e-2",
                    "dall-e-3"
                ],
                value="dall-e-2"
            )
            chat_model_dropdown = gr.Dropdown(
                choices=configs.allowed_models,
                value="gpt-3.5-turbo-1106",
                interactive=True,
                label="select chat model"
            )

    generate_prompt_button.click(
        callbacks.start_generate,
        inputs=[],
        outputs=[generate_prompt_textbox]
    ).then(
        callbacks.generate_prompt,
        inputs=[access_key_textbox, chat_model_dropdown, input_prompt, default_prompt],
        outputs=[generate_prompt_textbox]
    )

    imagine_button.click(
        callbacks.imagine,
        inputs=[access_key_textbox, imagine_model_dropdown, generate_prompt_textbox],
        outputs=[imagine_image]
    )
