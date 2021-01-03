FROM python:3.8
COPY ./ /app
WORKDIR /app
RUN pip3 install -r /app/requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg -y
CMD python /app/main.py