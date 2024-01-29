import gradio as gr
from utils import configs
from gradio_app.imagine_book_cover import callbacks


with gr.Blocks() as imagine_book_cover_ui:
    with gr.Row():
        with gr.Column(scale=7):
            imagine_image = gr.Image(interactive=False)
        with gr.Column(scale=3):
            access_key_textbox = gr.Textbox(
                label="connect key",
                type="password"
            )
            input_title = gr.Textbox(
                label="소설 제목",
                interactive=True,
                placeholder="태양의 사막에서의 리플레이"
            )
            input_chapter = gr.Textbox(
                label="챕터 명 혹은 부제목",
                interactive=True,
                placeholder=""
            )
            input_content = gr.Textbox(
                label="내용 혹은 요약",
                interactive=True,
                max_lines=7
            )
            guide_prompt = gr.Textbox(
                label="guide prompt",
                interactive=True,
                value="판타지, 이미지 생성 사이즈는 1024*1747, 레터박스 없는 꽉찬 커버 이미지"
            )
            chat_model_dropdown = gr.Dropdown(
                choices=configs.allowed_models,
                value="gpt-3.5-turbo-1106",
                interactive=True,
                label="select chat model"
            )
            generate_prompt_button = gr.Button(
                value="generate prompt",
            )
            generate_prompt_textbox = gr.Textbox(
                label="generated prompt",
                max_lines=7
            )
            imagine_model_dropdown = gr.Dropdown(
                label="select imagine model",
                interactive=True,
                choices=[
                    "dall-e-2",
                    "dall-e-3"
                ],
                value="dall-e-3"
            )
            imagine_button = gr.Button(
                value="imagine book cover"
            )


    generate_prompt_button.click(
        callbacks.start_generate,
        inputs=[],
        outputs=[generate_prompt_textbox]
    ).then(
        callbacks.generate_prompt,
        inputs=[access_key_textbox, chat_model_dropdown, input_title, input_chapter, input_content, guide_prompt],
        outputs=[generate_prompt_textbox]
    )

    imagine_button.click(
        callbacks.imagine,
        inputs=[access_key_textbox, imagine_model_dropdown, generate_prompt_textbox],
        outputs=[imagine_image]
    )

