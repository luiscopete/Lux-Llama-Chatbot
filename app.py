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

#Stramlit configuration
st.set_page_config(
    page_title="Lux Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",)

# Replicate API token
#os.environ['REPLICATE_API_TOKEN'] = '' ## Tests
#os.environ['REPLICATE_API_TOKEN'] = st.secrets["REPLICATE_API_TOKEN"]
replicate_api = st.secrets['REPLICATE_API_TOKEN']

def main():
    #Set title
    st.title("""Lux Assistant - by Luis Copete 💬""")

    with st.sidebar:
        #API Validation
        st.title('Lux Assistant Settings 🛠️')
        st.image('images/Banner2.jpg')
        model = st.selectbox('Select model', ['Meta-Llama-3-70b-instruct', 'Meta-Llama-3.1-405b-instruct'])
           
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
        st.session_state.messages = [{'role': 'assistant', 'content': 'Hello! How can I help you today?'}]

    #display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.write(message['content'])

    def clear_chat_history():
        st.session_state.messages = [{'role': 'assistant', 'content': 'Hello! How can I help you today?'}]
    st.sidebar.button('Clear chat history', on_click=clear_chat_history)


    def generate_response(prompt_input):
        string_dialogue = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
        for dict_message in st.session_state.messages:
            if dict_message["role"] == "user":
                string_dialogue += "User: " + dict_message["content"] + "\n\n"
            else:
                string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"

        output = replicate.run(
            #'meta/meta-llama-3.1-405b-instruct',
            f'meta/{model.lower()}',
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

    if prompt := st.chat_input(disabled=not replicate_api):
        st.session_state.messages.append({'role': 'user', 'content': prompt})
        with st.chat_message('user'):
            st.write(prompt)

    # Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Generating answer..."):
                response_iterator = generate_response(prompt)
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