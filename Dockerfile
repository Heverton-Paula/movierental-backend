# Imagem baseada na última versão estável do Python
FROM python:3.11-slim

# Variável de ambiente para não escrever arquivos .pyc no disco
ENV PYTHONDONTWRITEBYTECODE 1

# Variável de ambiente para não armazenar histórico de comandos no shell
ENV PYTHONUNBUFFERED 1

# Diretório de trabalho dentro do container
WORKDIR /src

# Cópia do arquivo requirements.txt para o container
COPY ./requirements.txt .

# Instalação das dependências
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
    
# Copia o código da aplicação para o diretório de trabalho do container
COPY /src /src/

# Porta em que a aplicação irá escutar
EXPOSE 8000

# Comando para executar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]