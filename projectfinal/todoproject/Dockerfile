# Base image
FROM python:3.10-slim

WORKDIR /app

RUN pip install django>=4.2
RUN pip install djangorestframework>=3.15.2
RUN pip install requests
RUN pip install django-cors-headers
RUN pip install django-extensions
RUN pip install djangorestframework djangorestframework-simplejwt



COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

