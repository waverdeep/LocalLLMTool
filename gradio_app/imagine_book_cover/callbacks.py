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


def start_generate():
    return "프롬프트 생성을 시작합니다..."


def generate_prompt(connect_key, model_name, input_title, input_chapter, input_content, guide_prompt):
    output = ""
    if connect_key != configs.config['MY_ACCESS_KEY']:
        output += "Please check the connect key."
        yield output
        return

    system_prompt = ""
    user_prompt = f"아래 정보를 바탕으로 소설의 커버 이미지를 만들것입니다. 사용자가 제공한 정보를 바탕으로 프롬프트를 재설계 해주세요. 이미지에 글자를 넣도록 지시하지 않습니다. 이미지 생성 규격을 명시하세요. 프롬프트만 생성하세요.\n소설 제목: {input_title}\n챕터 명: {input_chapter}\n내용 및 요약: {input_content}\n이미지 생성 규격: {guide_prompt}"
    stream = chat_client.chat.completions.create(
        model=model_name,
        messages=util.get_conversation(system_prompt, [], user_prompt),
        temperature=0.7,
        stream=True
    )

    output = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            output += chunk.choices[0].delta.content
            yield output