# T-302-HONN Team12

## Collaborators

- Bjarki Már Friðriksson
- Ýmir Þórleifsson 
- Elmar Ólafsson 
- Valgeir Ingi Þórðarson 
- Gunnlaugur Hlynur Birgisson 
- Hrafnkell Þorri Þrastarson 
- Garpur Hnefill Emilíuson
- Fannar Leó Örvarsson

## Description of project

The project is a platform for users to easily buy groceries, that simular to Eldum Rétt or Blue Apron, will send package to the user periodically on a weekly basis or more often.

## How to run

### First time run

1. Download and install python from python.org. 

2. Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py).

3. Install pip.

Open terminal in `get-pip.py` path and type in:

```bash 
python get-pip.py
```



4. Create a virtual environment

Install the module we will be using:

```bash
pip install venv
```

Create the environment

```
python venv python-django
```

5. Activate the virtual environment

on Windows type:
```bash
python-django\Scripts\activate
```
on UNIX (Mac, Linux) type:
``` bash
source python-django/bin/activate
```

6. Install Django

```
pip install django
```

7. Run the project
```bash
python src/Team12/manage.py runserver
```

### Normal run
1. Activate your virtual environment containing Django

2. Run the project
```bash
python src/Team12/manage.py runserver
```
