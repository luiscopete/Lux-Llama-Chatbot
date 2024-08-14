"""
Llama 3 Chatbot App
This is a Streamlit chatbot app with LLaMA3 models.

Author: Luis Copete
Created: August 2024
Status: Development
Python version: 3.8.18
Version: 0.1
State: Development
"""

import streamlit as st
import replicate
import os
from streamlit_app.utils import generate_response

#Stramlit configuration
st.set_page_config(
    page_title="Lux Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",)

# Replicate API token
#os.environ['REPLICATE_API_TOKEN'] = st.secrets["REPLICATE_API_TOKEN"]
replicate_api = st.secrets['REPLICATE_API_TOKEN']
#replicate_api = 'test'


gradient_text_html = """
<style>
.gradient-text {
    font-weight: bold;
    background: -webkit-linear-gradient(left, #68B7BA, #00BFFF); /* Degradado de azul */
    background: linear-gradient(to right, #1E90FF, #00BFFF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline;
    font-size: 3em;
}
</style>
<div class="gradient-text">LuxChat</div>
"""

model_options = {
    'Llama 3.1 70b': 'Meta-Llama-3-70b-instruct',
    'Llama 3.1 405b': 'Meta-Llama-3.1-405b-instruct'
}


def main():
    #Set title
    st.markdown(gradient_text_html, unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; color: gray;'>By Luis Copete</p>", unsafe_allow_html=True)
    #st.caption('By Luis Copete')
    #st.title("""Lux Assistant - by Luis Copete 💬""")
    model = st.radio(
        'Choose your model',
        options=list(model_options.keys()),
        #format_func=lambda x: model_options[x],
        index=0,
        horizontal=True)
    model = model_options[model]
    


    with st.sidebar:
        #API Validation
        st.title('Lux Assistant Settings 🛠️')
        st.image('images/Banner2.jpg')
        #model = st.selectbox('Select model', ['Meta-Llama-3-70b-instruct', 'Meta-Llama-3.1-405b-instruct'])
           
        #   #################### Secret settings for API token #############
        if 'REPLICATE_API_TOKEN' in st.secrets:
            st.success('API token loaded')
            replicate_api = st.secrets['REPLICATE_API_TOKEN']
           
        #   # Enter API token
        else:
            replicate_api = st.text_input('Enter API token', type='password')
            if not (replicate.api_token.startswith('r8_') and len(replicate.api_token) == 40):
                st.warning('Invalid API token', icon='🔑')
            else:
                st.success('Proceed to enter your prompt', icon='✍️')
        os.environ['REPLICATE_API_TOKEN'] = replicate_api

        #Model settings
        
        st.subheader('Model settings')
        temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=9.9, value=0.7, step=0.01)
        top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=0.9, value=1.0, step=0.01)
        presence_penalty = st.sidebar.slider('presence_penalty', min_value=0.01, max_value=2.0, value=1.15, step=0.01)
        max_tokens = st.sidebar.slider('max_tokens', min_value=0, max_value=1000, value=300, step=1)
        #min_tokens = st.sidebar.slider('min_tokens', min_value=0, max_value=, value=0, step=1)
        system_prompt = 'You are a helpful assistant\n\nUser:'
        prompt_template = 'system\n\nYou are a helpful assistant\n\n{prompt}assistant\n\n'

    #store LLM responses
    if 'messages' not in st.session_state.keys():
        st.session_state.messages = [{
            'role': 'assistant',
            'content': "Hello! I'm Lux, your personal AI assistant. How can I help you today?"
            }]

    assistant_icon = 'images/bot.png'
    user_icon = 'images/user2.png'
    #display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message['role'], avatar=assistant_icon):
            st.write(message['content'])

    def clear_chat_history():
        st.session_state.messages = [{
            'role': 'assistant', 
            'content': "Hello! I'm Lux, your personal AI assistant. How can I help you today?"}]
    st.sidebar.button('Clear chat history', on_click=clear_chat_history)

    # Chat input
    if prompt := st.chat_input(disabled=not replicate_api):
        st.session_state.messages.append({'role': 'user', 'content': prompt})
        with st.chat_message('user', avatar=user_icon):
            st.write(prompt)

    # Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant", avatar=assistant_icon):
            with st.spinner("Generating answer..."):
                response_iterator = generate_response(
                    prompt, 
                    model, 
                    temperature, 
                    top_p, 
                    max_tokens, 
                    presence_penalty)
                placeholder = st.empty()
                full_response = ''
                for item in response_iterator:
                    full_response += item
                    placeholder.markdown(full_response + "▌")
                placeholder.markdown(full_response)
        message = {"role": "assistant", "content": full_response}
        st.session_state.messages.append(message)

if __name__ == '__main__':
    main()
    with st.sidebar:
        st.markdown("---")
        st.markdown(
            '<h6>Made in &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="16">&nbsp by <a href="https://github.com/luiscopete">luiscopete</a></h6>',
            unsafe_allow_html=True)
        st.markdown(
            '<a href="https://www.linkedin.com/in/luiscopete/"><img src="https://www.edigitalagency.com.au/wp-content/uploads/Linkedin-logo-png.png" alt="LinkedIn logo" height="16"></a>',
            unsafe_allow_html=True)