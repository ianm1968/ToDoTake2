# DevOps Apprenticeship: To Do Checklist exercise-1

## To Do checklist overview

This demonstration webapp uses Flask and poetry for development.  See below for details.  The application can be accessed on  a standard browser via HTTP port 5000. E.g. https://{server-ip-address-goes-here}:5000

The app allows the user to enter an item into a To Do list.

 - Enter the task text in the 'Task' edit
 - Click Add button - it will be added to the 'To Do' list in the app.
 - Tick a 'To Do' task  - it will move to the 'Doing' list.
 - Tick a 'Doing' task  - it will move to the 'Done' list.
 - Restore a 'Done' task - it will move back to the 'To Do' list
 - Delete any task from either the 'To Do' or 'Done' list.
 
## Configuration using .env
A starter `.env.template` file is  provided but must be filled in using values as follows and renamed `.env`
```bash
SECRET_KEY=secret-key

API_KEY=trello-api-key

TOKEN=trello-token

BOARD_ID = trello-board-id

DEFAULT_TO_DO_NAME = to-do-list-name

DEFAULT_DOING_NAME = doing-list-name

DEFAULT_DONE_NAME = done-list-name
```

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.
