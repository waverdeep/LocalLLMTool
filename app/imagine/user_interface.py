import gradio as gr


with gr.Blocks() as imagine:
    with gr.Row():
        with gr.Column(scale=3):
            input_prompt = gr.Textbox(
                label="input prompt",
                interactive=True,
                lines=3,
                max_lines=5
            )
            imagine_button = gr.Button(
                value="imagine"
            )
            imagin_image = gr.Image("https://oaidalleapiprodscus.blob.core.windows.net/private/org-9XJGt9pgEZbF1dQ8yg98FNGE/user-C0BghryLHll37veHPr7qa85Y/img-scJZg3CpTLqybMFmgiw7ZNVO.png?st=2024-01-14T13%3A01%3A05Z&se=2024-01-14T15%3A01%3A05Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-01-14T11%3A17%3A45Z&ske=2024-01-15T11%3A17%3A45Z&sks=b&skv=2021-08-06&sig=e64qbCi5dxn27NJ5T33QR6Lrx5qnXUliC3HGdKEdAhE%3D")
