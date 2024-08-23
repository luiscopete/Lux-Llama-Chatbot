# Lux Chatbot

![Lux Logo](images/Banner2.jpg)

**Lux** is a conversational AI assistant powered by advanced Llama 3.1 models. This project is a Streamlit-based chatbot application that offers intelligent, multilingual responses tailored to user sentiment and regional context.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Models](#models)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Multilingual Support:** Interact in Spanish, English, French, German, Italian, and Portuguese.
- **Sentiment Adjustment:** Choose from a variety of emotions such as Neutral, Happy, Sad, Angry, and more.
- **Voice Commands:** Supports speech-to-text input for a hands-free experience.
- **Customizable Models:** Choose from multiple pre-configured language models including Llama 3.1 and Flan T5 XL.
- **Streamlit Integration:** User-friendly interface built with Streamlit, offering easy setup and interaction.

## Setup

### Prerequisites

- Python 3.8.18
- [Streamlit](https://streamlit.io/)
- [Replicate API Token](https://replicate.com/) (for running models)
- streamlit_mic_recorder (for Speech-To-Text prompts)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/luiscopete/Lux-Llama-Chatbot.git
   cd Lux-Llama-Chatbot

2. **Build the Docker Image:**
    ``` bash
    docker build -t lux-chatbot .

3. **Run the Docker Container:**
    ``` bash
    docker run -p 8501:8501 lux-chatbot  


### Authors

**Luis Copete**  
Creator and Developer of Lux Chatbot  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/luiscopete)  
[![GitHub](https://img.shields.io/badge/GitHub-171515?style=flat&logo=github&logoColor=white)](https://github.com/luiscopete)  

Feel free to connect on LinkedIn or check out more projects on GitHub!
