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
The project is a website, developed in Django, for users to easily buy meal packages containing groceries. Similar to Eldum Rétt or Blue Apron, the service will send ingredients to a customer periodically, e.g. on a weekly basis or more often.

## Sprint 1
We decided on building the website with Django as framework connected to a Postgres as database. Possibly using Atomic for the UI in the future. We are currently using built-in models, admin and users. As of now, the website contains functionality for users to register, login, look at their profile, logout and delete their account.

## Software architecture
Our software is designed in well defined layers; Presentation Layer, Logic Layer and Data Layer.

![](readme_images/layers.png)

We are using Django to develop both the PL and LL. In the PL we use Django templates, that use HTML and CSS along with a bit of Python. In the LL we only use Python to build Django views, that decide on templates to show user. We also build Django models, that decide what and how data is stored.

The data layer is stored in SQL using Postgres, we store our models in SQL table format.

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
````
> python manage.py test
