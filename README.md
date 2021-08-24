# README

This project is to evaluate the scalability of developing with the FastAPI Framework in Python, and to help hone my own ability using more advanced python techniques.

## <ins>Initial Setup</ins>

On your local machine you will need to ensure you have the following tools installed:

- Python
- Docker
- Database Viewing Tool
- Postman

### <ins>Python Setup</ins>

So firstly, you will need to install the latest Python on to your local machine. You can find the instructions on how to install Python at the following [link.](https://www.python.org/downloads/)

Once you have installed Python you will want to install only one module to the global packages for your local envoirment and that is `virtualenv`. The following commands can be used for the corresponding operating system.

- Mac / Linux - `python3 -m pip install --user virtualenv`
- Windows - `py -m pip install --user virtualenv`

Once you have the module for creating a virtual environment installed, you will need to create a virtual env for the project within the root of the project with the following commands:

- MacOS/Linux - `python3 -m venv .venv`
- Windows - `py -m venv .venv`

Once they have been created, you then will need to run the virtual env everytime you want to do work in the project.

- MacsOS/Linux - `source .venv/bin/activate`
- Windows - `.venv\Scripts\activate`

### <ins> Docker Setup </ins>

So for the Docker setup, we're going to focus on setting up for Windows as the Mac setup is a lot more straight forward.

For the setup, it's best to follow the setup on their offical page [here](https://docs.docker.com/desktop/windows/install/)

### <ins> Database Viewing Tool </ins>

You only need to ensure you have a Database Viewing Tool that is compatible with viewing MySQL, but my personal recommendation is [DBeaver](https://dbeaver.io/).

# Running the Project

So for the first time, you will need to run the docker composent to start the database: `docker-compose up -d` and `pip install -r requirments.txt`

Once you have the Database ruuning, you will need to connect to in and execute the DB Scripts inside the "database_scripts" folder. All the information for a localhost connection can be found "database.env"

Once you have installed all the modules for the corresponding modules for the project, connected to the database and run the database scripts all you will need to do is run the following command:

- `uvicorn main:app --reload --env-file database.env`

# Mics

- https://code.visualstudio.com/docs/python/environments#_manually-specify-an-interpreter
- Documentation: https://fastapi.tiangolo.com/
