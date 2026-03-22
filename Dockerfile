FROM python:latest
RUN apt update && apt upgrade -y
RUN apt install sqlite3
WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD [ "python3", "./app.py"]
