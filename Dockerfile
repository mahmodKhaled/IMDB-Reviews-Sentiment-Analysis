FROM python:3.9-slim-buster

WORKDIR ./

COPY web_server.py .
COPY model_weights model_weights/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "web_server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]