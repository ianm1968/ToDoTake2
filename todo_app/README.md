# DevOps Apprenticeship: To Do Checklist exercise-1

## To Do App overview

This webapp uses Flask and poetry for development.  See below for details.  The application can be accessed on  a standard browser via HTTP port 5000. E.g. https://{server-ip-address-goes-here}:5000
## Using the app

The app allows the user to create a 'To Do' item and track and update its progress using **To Do**, **Doing** and **Done** lists.

 - Enter the task text in the 'Task' edit at the top (black panel).
 - Click **'Add'** button - it will be added to the **'To Do' list (red panel)**.
 - Click the **'Start'** button on a 'To Do' task  - it will move to the **'Doing' list (yellow panel)***.
 - Click the **Done (tick)** button on a 'Doing' task  - it will move to the **'Done' list (green panel)**.
 - **Restart** a 'Done' task - it will move back to the 'To Do' list
 - **Delete** any task in any list using the **'Delete' button**
- **Note 1:** items are sorted in lists strictly on descending date/time
- **Note 2:** the **Done list** will always show items done today in **green** and items done before today in **blue**.  However if there are 5 or more in total, any done before today will be shown in **a separate 'Done before today' details list (blue panel)** which can be hidden by clicking on the header.  All items in this list can be deleted in one action using the delete in the list header.

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
Ensure you have a Trello account, create a board with **To Do, Doing and Done lists** names matching the default names you have entered.  Identify the value for BOARD_ID following these steps as taken from https://community.atlassian.com/t5/Trello-questions/How-to-get-Trello-Board-ID/qaq-p/1347525 ...
1. Go to your Trello Board
2. Add ".json" to end of the URL
3. Format the JSON so it's readable (you can find a JSON viewer online)
4. Search for idBoard - this will list your full Board ID.

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

## Running the Tests
To execute tests from a command line open a command prompt, browse to the project root folder and execute...

```
poetry run pytest
```

## Docker Images and Containers
The dockerfile provided is multi-stage and allows building of a 'production', 'development' or 'test' image by running one of the following commands...

```
docker build --target production --tag todo-app .
docker build --target development --tag todo-app .
docker build --target test --tag todo-app .
```
The 'production' image uses gunicorn and can be run using...
```
docker run --env-file .env --publish 5000:5000 todo-app
```
The 'development' and 'test' images uses Flask and can be run as follows (which maps the local /todo_app folder to the /app/todo_app folder on the image).

```
docker run --env-file .env --publish 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app
```
The tests can be executed on the test container from a bash window using...
```
poetry run pytest
```