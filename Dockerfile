FROM python:3.11-bookworm

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]