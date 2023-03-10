FROM python:3.11-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV POETRY_VERSION=1.1.13

RUN mkdir -p /src/

RUN apt-get update && apt-get -y install libgdal-dev \
    && pip install "poetry==$POETRY_VERSION" \
    && poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY src/ /src/
WORKDIR /src/

CMD ["gunicorn", "-w", "3", "--bind", ":8000", "config.wsgi:application"]
