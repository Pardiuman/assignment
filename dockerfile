FROM python:3.9.18-slim

WORKDIR /app

COPY ./requirements.txt .

# RUN pip install flask
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]