# TNA Interview Coding Challenge: Archive Cache

## Installation details

These instructions assume at least minimal familiarity with using the command line interpreter on your operating system, and knowledge of cloning a repository from GitHub. You will require Python version 3.8 or higher.

### Getting the code

Clone the repository into a folder on your local system. once you have compelted this step, the content of the repository root folder should look like this:

```
archive/
.gitignore
INSTALLATION.md
README.nmd
requirements.txt
```

### Setting up the environment

Open a terminal/command prompt/Powershell and navigate to this folder, then set up a virtual environment (the commands may be slightly different depending on your operating system and shell) and install the requirements:

```
> python -m venv venv
> ./venv/bin/activate
(venv)> pip install -r requirements.txt
```

### Building the django project

Change directory to `archive` (usually just `> cd archive`): the folder structure should look like this:

```
archive/
local/
tests/
manage.py
```

Now set up the migrations that ensure django has registered all the models and commands required to run the app:

```
> ./manage.py makemigrations
> ./manage.py migrate
```

### Run the app and tests

You are all set up and can continue following the instructions in [README.md](./README.md) to run the app and tests.

