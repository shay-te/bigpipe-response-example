FROM python:3.7.2

WORKDIR /bigpipe_response_example
COPY . /bigpipe_response_example

RUN pip install -r requirements.txt

ENV PYTHONPATH /bigpipe_response_example

ENTRYPOINT ["python", "/bigpipe_response_example/manage.py"]
CMD ["runserver", "0.0.0.0:8080"]

EXPOSE 8080
