FROM python:3.9.4-slim

ENV VIRTUAL_ENV /.venv
# Better async tracebacks.
ENV PYTHONTRACEMALLOC 32
# Get stdout/stderr messages in real-time.
ENV PYTHONUNBUFFERED 1
# Listen to 0.0.0.0 instead of localhost
ENV API_HOST=0.0.0.0

# Bust cache when requirements.txt changes.
COPY requirements.txt /tmp/requirements.txt

RUN python -m venv ${VIRTUAL_ENV} &&\
    export VIRTUALENV=${VIRTUAL_ENV} &&\
    pip3 install --no-cache-dir -r /tmp/requirements.txt

# Copy dem codes.
COPY . /code
WORKDIR /code
ENV PYTHONPATH /code/src

CMD /code/start_server.sh
