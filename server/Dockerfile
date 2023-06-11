FROM python:3.9

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#RUN python manage.py makemigrations
#RUN python manage.py migrate
RUN python manage.py collectstatic --no-input

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
