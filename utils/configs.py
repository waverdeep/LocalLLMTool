import os


allowed_models = [
    "gpt-3.5-turbo-1106",
    "gpt-4-1106-preview",
]

config = {
    "OPENAI_API_KEY": os.environ.get('OPENAI_API_KEY', None),
    "MY_ACCESS_KEY": os.environ.get('MY_ACCESS_KEY', None),
}
