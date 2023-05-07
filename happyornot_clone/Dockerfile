# base iamage
FROM python:3.10.6
#set up environment variable
ENV PYTHONUNBUFFERE 1
WORKDIR /home/meztroinhinyeroelektronico/Desktop/django_prj/happyornot_prj/
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "127.0.0.1:8000"]