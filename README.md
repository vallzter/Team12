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

### Programs need
1. [Python 3.8](https://www.python.org/downloads/)

2. [pip](https://bootstrap.pypa.io/get-pip.py)

3. [Anaconda](https://www.anaconda.com/products/individual) (Optional)

In the terminal where `get-pip.py` is located install the pip file:

```
> python get-pip.py
```

### Create virtual environment

Using conda:

```
> conda create --name django-env python=3.8
```

Using virtualenv:

```
> pip install virtualenv
> virtualenv django-env
```
### Activate virtual environment
Using conda:
```
> activate django-env
```
Using virtualenv (Windows):
```
> python-django\Scripts\activate
```
Using virtualenv (Mac, Linux):
```
$ source python-django/bin/activate
```

### Install the modules
While using the virtual environment:
```
> pip install -r requirements.txt
```

### Run server
Navigate to `manage.py`
```
> python manage.py runserver
```
