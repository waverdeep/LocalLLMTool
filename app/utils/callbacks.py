import random
import time


def chat_completion(system_prompt, message, chat_history, chat_id):
    if not chat_id:
        chat_id = time.time()
        
    chat_history.append((message, "you typed: "+message))
    
    return chat_id, chat_history, ""
    
    
