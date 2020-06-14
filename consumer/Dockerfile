FROM python:3.6

WORKDIR /home

RUN pip install kafka-python==2.0.1 \
                cryptography==2.9.2 \
                requests==2.23.0

COPY main.py main.py

CMD [ "python", "-u", "/home/main.py" ]