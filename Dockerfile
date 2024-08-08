FROM python:3.9-slim

WORKDIR /app

COPY API/requirements.txt requirements.txt
COPY API/app/main.py /app
# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt
# Metodo alternativo: RUN pip install -r requirements.txt

EXPOSE 8082

COPY API/app/ app/

CMD ["python", "app/main.py"]
