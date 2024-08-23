# Lux Chatbot

<p align="center">
  <img src="images/Banner2.jpg" alt="Lux Logo" width="450"/>
</p>

<!-- ![Lux Logo](images/Banner2.jpg) -->

**Lux** is a conversational AI assistant powered by advanced Llama 3.1 models and others. This project is a Streamlit-based chatbot application that offers intelligent, multilingual responses tailored to user sentiment and regional context.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Models](#models)
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

## Usage

### Running the Application

To use Lux Chatbot, you have two options: run it locally using Docker or access the hosted version.

#### Option 1: Running Locally with Docker

1. **Build the Docker Image:**

   If you haven't built the Docker image yet, you can do so by running the following command in the root directory of the project (where the Dockerfile is located):

   ```bash
   docker build -t lux-chatbot .

2. **Run the Docker Container:**

    Start the Lux Chatbot container with:
    ```bash
    docker run -p 8501:8501 -e REPLICATE_API_TOKEN=your_token_here lux-chatbot

Replace your_token_here with your actual Replicate API token.

2. **Access the Chatbot:**

    Open your web browser and navigate to http://localhost:8501. You should see the Lux Chatbot interface

**Option 2: Accessing the Hosted Version**
If you prefer not to run the chatbot locally, you can use the hosted version of Lux Chatbot:


<a href='https://lux-chat.streamlit.app/'> Lux Chatbot Hosted App </a>

### Using the Chatbot
Once the application is running, you can interact with Lux by following these instructions:

1. **Choosing a Model:**

    At the top of the page, you can select which language model you want to use. Options include:

    - Llama 3.1 70b Instruct
    - Llama 3.1 405b Instruct
    - Mixtral 8x7b Instruct
    - Flan T5 XL
    
2. **Setting Chat Parameters:**

    - **Sentiment:** Choose the sentiment you want Lux to use in its responses (e.g., Happy, Sad, Angry).
    - **Country:** Select the country to customize responses based on regional context.
    -  **Language:** Choose the language for interaction (e.g., Spanish, English, French).

3. **Interacting with Lux:**

    - **Text Input:** Type your message in the input box at the bottom of the chat interface and press Enter to send it.
    - **Voice Input:** Click on the microphone icon to speak your message. Lux will process your voice input and generate a response.

4. **Viewing Responses:**

    Lux will generate a response to your input, which will be displayed in the chat window. Responses are generated in real-time, so you can continue the conversation seamlessly.

5. **Clearing Chat History:**

    If you want to start a new conversation, click the "Clear chat history" button in the sidebar. This will reset the chat, and Lux will greet you again.

### Troubleshooting

- **API Token Issues:** Ensure that your Replicate API token is correctly set as an environment variable when running the Docker container. If Lux cannot access the token, it will display a warning message.

- **Application Not Loading:** If the application does not load, check that Docker is running and that the container is correctly started. Make sure port 8501 is not blocked by any firewall or other network settings.


## Contributing

I welcome contributions to the Lux Chatbot project! Whether you want to fix a bug, add a new feature, or improve documentation, your help is greatly appreciated.

### How to Contribute

1. **Fork the Repository:**

   Start by forking the Lux Chatbot repository to your GitHub account. You can do this by clicking the "Fork" button at the top of the repository page.

2. **Clone Your Fork:**

   Clone your forked repository to your local machine using the following command:

   ```bash
   git clone https://github.com/luiscopete/Lux-Llama-Chatbot.git


3. **Create a New Branch:**

    Before making any changes, create a new branch for your work:

    ``` bash
    git checkout -b feature-or-bugfix-name

4. **Make Your Changes:**

    Implement your changes in the new branch. This could involve updating code, adding new features, fixing bugs, or improving documentation.

5. **Run Tests:**

    If your changes involve code, make sure to run existing tests and add new tests if needed. This ensures that your changes do not break any existing functionality.

    ```bash
    pytest tests/

6. **Commit Your Changes:**

    After making your changes, commit them with a descriptive message:

    ``` bash
    git add .
    git commit -m "Description of your changes"

7. **Push Your Branch:**

    Push your branch to your forked repository:

    ``` bash
    git push origin feature-or-bugfix-name

8. **Submit a Pull Request:**

    Go to the original Lux Chatbot repository and click on "New Pull Request." Select your branch and describe your changes in detail. If your pull request addresses a specific issue, please reference it in the description.

9. **Code Review:**

    Once your pull request is submitted, it will be reviewed by me. They may ask for some changes or provide feedback. Please address any comments and update your pull request as necessary.

10. **Merge:**

    After your pull request is approved, it will be merged into the main branch. Congratulations, and thank you for contributing!

### Code Style Guidelines

- Follow the PEP 8 style guide for Python code.
- Ensure your code is clean, readable, and well-documented.
- Use descriptive variable and function names.
- Avoid unnecessary complexity.

### Reporting Issues

If you encounter any issues or bugs, please open an issue in the repository. Be sure to include details such as steps to reproduce the issue, expected behavior, and any relevant logs or screenshots.


### Authors


**Luis Copete**  

Creator and Developer of Lux Chatbot  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/luiscopete)  
[![GitHub](https://img.shields.io/badge/GitHub-171515?style=flat&logo=github&logoColor=white)](https://github.com/luiscopete)  

Feel free to connect on LinkedIn or check out more projects on GitHub!
