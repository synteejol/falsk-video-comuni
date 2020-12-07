FROM python:3.7-slim

EXPOSE 80

RUN mkdir /opt/app
COPY ./requirements.txt /opt/app/requirements.txt
# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r /opt/app/requirements.txt
# Add our code
COPY . /opt/app/
WORKDIR /opt/app
# CMD chmod +x /opt/app/wait.sh
CMD gunicorn -b 0.0.0.0:5000 wsgi:app
