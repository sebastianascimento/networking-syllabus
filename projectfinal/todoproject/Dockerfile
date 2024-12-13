# Base image
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instalar dependências diretamente
RUN pip install django>=4.2

# Copiar o código do projeto para dentro do container
COPY . .

# Expõe a porta 8000 para o Django
EXPOSE 8000

# Comando padrão para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

