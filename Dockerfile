FROM python:3.7.2

ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
ENV PYTHONPATH /code/bigpipe_response_example

ENTRYPOINT ["python", "bigpipe_response_example/manage.py"]

CMD []

EXPOSE 8080
