# T-302-HONN Team12

## Collaborators

- Bjarki Már Friðriksson
- Elmar Ólafsson
- Fannar Leó Örvarsson
- Garpur Hnefill Emilíuson
- Gunnlaugur Hlynur Birgisson
- Hrafnkell Þorri Þrastarson
- Valgeir Ingi Þórðarson
- Ýmir Þórleifsson

## Description of the project

The project is a platform for users to easily buy meal packages containing groceries, similar to Eldum Rétt or Blue Apron, which are delivered to the user to his choosing, whether it is on a weekly basis or more often.

## Agreed tasks with the product owner
The project currently contains a registration/login form where the user can register and login and also a button where the user can delete his account.

## Technical aspects
This is a RESTful API that uses Django as framework and is connected to a PostgreSQL database.

## How to run

### Programs needed
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
> django-env\Scripts\activate
```
Using virtualenv (Mac, Linux):
```
$ source django-env/bin/activate
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

## How to test
