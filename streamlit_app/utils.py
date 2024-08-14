#  streamlit_app/utils.py
import replicate
import streamlit as st

def generate_response(prompt_input, model, temperature, top_p, max_tokens, presence_penalty):
    string_dialogue = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"

    output = replicate.run(
        #'meta/meta-llama-3.1-405b-instruct',
        f'{model.lower()}',
        input={
            "prompt": f"{string_dialogue} {prompt_input} Assistant: ",
            "temperature": temperature, 
            "top_p": top_p, 
            "max_tokens": max_tokens, 
            "presence_penalty": presence_penalty,
            "repetition_penalty": 1.0,
        },
        stream=True
    )
    return output