FROM python:3.10 AS base

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt --target /python-libs

FROM python:3.10-alpine AS app

WORKDIR /app
COPY --from=base /python-libs /python-libs
COPY . .

ENV PYTHONPATH=/python-libs

CMD ["python", "client.py"]