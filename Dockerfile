# Use python 3.8 as base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY pyproject.toml poetry.lock ./
COPY requirements.txt ./
COPY app.py ./
COPY streamlit_app/ ./streamlit_app/
COPY images/ ./images/
COPY tests/ ./tests/
COPY .streamlit/ /app/.streamlit/

# Install Poetry
RUN pip install poetry

# Install the dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Install the dependencies
# RUN pip install -r requirements.txt

# Expone el puerto que utilizará Streamlit (8501 por defecto)
EXPOSE 8501

# Establece el comando por defecto para ejecutar la app de Streamlit
CMD ["streamlit", "run", "app.py"]
