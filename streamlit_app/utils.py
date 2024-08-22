#  streamlit_app/utils.py
import replicate
import streamlit as st
from streamlit_mic_recorder import speech_to_text


language_options = {
    'English': 'EN',
    'Spanish': 'ES',
    'French': 'FR',
    'German': 'DE',
    'Italian': 'IT',
    'Portuguese': 'PT',
}

def get_prompt_systems(language):
    ''' Get prompt systems from dialogues.txt '''
    with open('./streamlit_app/dialogues.txt', 'r') as file:
        text = file.read()
    language_abrv = '['+ language_options[language] + ']'
    print(language_abrv)
    #language = next(key for key, value in language_options.items() if value == language) # Get key from value
    dialogues = text.split('---')
    for i, lang in enumerate(dialogues):
        if lang.strip().startswith(language_abrv):
            return lang.strip().replace(language_abrv, '').replace('\n', '')
    raise ValueError('Language not found in dialogues.txt')

def generate_response(
    prompt_input,
    model,
    temperature,
    top_p,
    max_tokens,
    presence_penalty,
    country,
    language,
    sentiment="friendly",
):
    """Generate response from LLM model"""

    string_dialogue = (
        get_prompt_systems(language)
        .replace("[demonym]", country)
        .replace("[sentiment]", sentiment)
    )
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"

    output = replicate.run(
        #'meta/meta-llama-3.1-405b-instruct',
        f"{model.lower()}",
        input={
            "prompt": f"{string_dialogue} {prompt_input} Assistant: ",
            "temperature": temperature,
            "top_p": top_p,
            "max_tokens": max_tokens,
            "presence_penalty": presence_penalty,
            "repetition_penalty": 1.0,
        },
        stream=True,
    )
    return output

def generate_gradient_html(text, size, left_color, right_color, class_name):
    ''' Generate HTML with gradient text '''
    html = f"""
    <style>
    .{class_name} {{
        font-weight: bold;
        background: -webkit-linear-gradient(left, {left_color}, {right_color});
        background: linear-gradient(to right, {left_color}, {right_color});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline;
        font-size: {size}em; /* Tamaño ajustable */
    }}
    </style>
    <div class="{class_name}">{text}</div>
    """
    return html



def prompt_audio(language):
    ''' Prompt audio recording '''
    speech = speech_to_text(
        language=language,
        start_prompt='Record voice 🎙️',
        stop_prompt='Stop recording',
        just_once=False,
        use_container_width=False,
        callback=None,
        args=(),
        kwargs={},
        key=None,
    )
    return speech 