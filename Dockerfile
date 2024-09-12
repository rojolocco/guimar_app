# Usa una imagen base de Python
FROM python:3.11-slim

# Define el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo pyproject.toml y poetry.lock para instalar dependencias
COPY pyproject.toml poetry.lock* /app/

# Instalar Poetry
RUN pip install poetry

# Instalar dependencias sin crear el virtualenv
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

# Copiar el resto del código del proyecto (incluyendo la carpeta 'app')
COPY . /app

# Expone el puerto que usará FastAPI
EXPOSE 80

# Comando para ejecutar la aplicación (ajustado para el directorio 'app')
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
