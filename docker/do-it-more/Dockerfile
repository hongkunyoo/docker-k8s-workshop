FROM python:3.7

RUN apt-get update
RUN pip install flask pymysql cryptography
COPY app.py .

CMD ["python", "-u", "app.py"]

