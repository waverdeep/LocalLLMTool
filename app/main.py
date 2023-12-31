import utils.gradio_interface as gradio_interface


if __name__ == '__main__':
    gradio_interface.demo.launch(
        server_name="0.0.0.0",
        server_port="8000"
    )