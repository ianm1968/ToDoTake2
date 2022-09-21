FROM python:3.8-slim-buster as base
WORKDIR /app
COPY . /app
EXPOSE 5000
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install poetry

FROM base as production
RUN poetry install -n --no-root --no-dev
ENTRYPOINT [ "poetry", "run", "gunicorn", "--bind", "0.0.0.0:5000", "todo_app.app:create_app()" ]

FROM base as development
RUN poetry install -n
ENTRYPOINT [ "poetry", "run", "flask", "run", "--host=0.0.0.0" ]

FROM base as test 
RUN poetry install -n -E "pytest pytest-watch"
ENTRYPOINT [ "bash", "test.sh" ]
