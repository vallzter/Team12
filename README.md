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

## Description of the Project

The project is a website, developed in Django, for users to easily buy groceries. Simular to Eldum Rétt or Blue Apron, the service will send ingrediences to a customer periodically on a weekly basis or more often.

## Sprint 1

We desided on building the website up in Django and Postgres. Possibly using Atomic for the UI in the future. We are currently using built in models; admin and users. We have implemented register, login, look at profile, logout and delete user.

## Software Architecture

Our software is designed in well defined layers; Presentation Layer, Logic Layer and Data Layer. 

![](readme_images/layers.png)

We are using Django to develop both the PL and LL. In the PL we use Django templates, that uses html and css along with a bit of python. In the LL we only use python to build Django views, that deside on templates to show user and we build Django models, this desides what and how data is stored.

The datalayer is stored in SQL using Postgres, we store our models in SQL table format. 

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
