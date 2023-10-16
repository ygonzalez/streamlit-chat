FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y gcc

WORKDIR /app

COPY . /app

RUN pip install streamlit==1.26.0 langchain==0.0.281 openai==0.27.5 faiss-cpu==1.7.4 tiktoken

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
