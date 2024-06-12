FROM python:3.12

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev

COPY . .

CMD ["python", "poetry_ci_cd_project/app.py"]
