FROM python:3.11

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /code

CMD ["./wait-for-it.sh", "db:5432", "--", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
