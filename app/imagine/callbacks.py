from utils import util
from utils import configs


chat_client = util.register_openai_api_key(configs.config['OPENAI_API_KEY'])


def imagine(connect_key, model_name, input_prompt):

    if connect_key != configs.config['MY_ACCESS_KEY']:
        return None

    response = chat_client.images.generate(
        model=model_name,
        prompt=input_prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    return response.data[0].url
