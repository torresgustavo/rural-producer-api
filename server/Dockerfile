FROM python:3.12.3-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip install poetry && \
  poetry config virtualenvs.create false && \
  poetry install

COPY . /app

EXPOSE 8000

CMD ["python", "manage.py runserver 0.0.0.0:8000"]

