FROM python:3.11

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt && pip install -e .
EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
