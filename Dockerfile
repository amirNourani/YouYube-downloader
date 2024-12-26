FROM python:3.10-slim-buster

WORKDIR /authentication

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PSYCOPG2_BUILD=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .
COPY poetry.lock .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .

ENTRYPOINT ["python", "main.py"]