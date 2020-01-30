FROM python:3.7.2


WORKDIR /code
COPY . /code

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code:/code/bigpipe_response_example

# Install Node js
RUN apt-get update -yq \
    && apt-get install curl gnupg -yq \
    && curl -sL https://deb.nodesource.com/setup_8.x | bash \
    && apt-get install nodejs -yq

# Install project dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Init bigpipe will install nodejs dependencies
WORKDIR /code/bigpipe_response_example
# Init bigpipe at the docker file will cause installation of node js with dependencies
RUN python3 init_bigpipe.py

EXPOSE 8080

ENTRYPOINT ["python3", "manage.py"]
CMD []
