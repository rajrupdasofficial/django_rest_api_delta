FROM python:3.9.10-slim

COPY . /app
WORKDIR /app

RUN python3 -m venv /opt/env


RUN /opt/env/pip install --upgrade pip && \ 
    /opt/env/pip install -r requirements.txt && \ 
    chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]

