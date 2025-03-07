FROM python:3.10

WORKDIR /app

RUN pip install poetry

COPY . /app

RUN poetry config virtualenvs.create false && poetry install --no-root

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
