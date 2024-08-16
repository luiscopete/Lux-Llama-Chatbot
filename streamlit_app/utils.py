#  streamlit_app/utils.py
import replicate
import streamlit as st

def generate_response(prompt_input, model, temperature, top_p, max_tokens, presence_penalty, sentiment='friendly'):
    ''' Generate response from LLM model '''
    string_dialogue = f"""
    You are a helpful assistant. You are a woman. Your name is Lux. You was developed by Luis Copete, a Colombian Data Engineer. 
    You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant' or 'Lux'. 
    You always answer using colombian slangs and expressions from Antioquia, Colombia. You are {sentiment}."""
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

def generate_gradient_html(text, size, left_color, right_color):
    ''' Generate HTML with gradient text '''
    html = f"""
    <style>
    .gradient-text {{
        font-weight: bold;
        background: -webkit-linear-gradient(left, #{left_color}, #{right_color}); /* Degradado de azul */
        background: linear-gradient(to right, #1E90FF, #00BFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline;
        font-size: {size}em;
    }}
    </style>
    <div class="gradient-text">{text}</div>
    """
    return html