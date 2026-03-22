FROM python:3.14.3-trixie
RUN apt update && apt upgrade -y
RUN apt install sqlite3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
CMD [ "python3", "./app.py"]
