
FROM python:3.9-slim


WORKDIR /app


COPY . /app


RUN apt-get update && apt-get install -y \
    && pip install --upgrade pip

RUN pip install -r requirements.txt


EXPOSE 8000


CMD ["python", "main.py"]
