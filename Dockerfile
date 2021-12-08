FROM python:3.9-slim-buster AS pysony

COPY requirements.txt /pysony/

WORKDIR /pysony

RUN python3 -m pip install --upgrade pip build && \
    python3 -m pip install --no-cache-dir -r requirements.txt

COPY . /pysony

RUN python3 ./setup.py bdist_wheel && \
    python3 -m pip install ./dist/pysony-1.0-py3-none-any.whl && \
    rm -Rf /pysony