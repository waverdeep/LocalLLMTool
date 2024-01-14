# import utils.gradio_interface as gradio_interface
import utils.user_interface as user_interface


if __name__ == '__main__':
    user_interface.demo.launch(
        server_name="0.0.0.0",
        server_port=6007
    )