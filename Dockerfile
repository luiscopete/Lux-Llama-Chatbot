# Use python 3.8 as base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the necessary files to the container
COPY pyproject.toml poetry.lock ./
COPY app.py ./
COPY streamlit_app/ ./streamlit_app/
COPY images/ ./images/
COPY tests/ ./tests/
COPY .streamlit/ /app/.streamlit/

# Install Poetry
RUN pip install poetry

# Install the dependencies with Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Expose the port that Streamlit will use (default is 8501)
EXPOSE 8501

# Set the default command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
