FROM python:3.8-slim-buster as base
WORKDIR /app
COPY . /app
EXPOSE 5000
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install poetry && pip3 install flask && pip3 install pytest && pip3 install python-dotenv

FROM base as production
RUN pip3 install gunicorn
ENTRYPOINT [ "poetry", "run", "gunicorn", "--bind", "0.0.0.0:5000", "todo_app.app:create_app()" ]

FROM base as development
ENTRYPOINT [ "poetry", "run", "flask", "run", "--host=0.0.0.0" ]

