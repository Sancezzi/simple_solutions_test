FROM python:3.10

RUN mkdir /store

WORKDIR /store

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
