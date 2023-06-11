FROM python:3.9

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY wait-for /usr/bin/
RUN chmod +x /usr/bin/wait-for

RUN chmod +x entrypoint.sh
