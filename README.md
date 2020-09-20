# T-302-HONN Team12
![](https://img.shields.io/badge/python-v3.8-blue)
![](https://img.shields.io/github/pipenv/locked/dependency-version/vallzter/Team12/django)
![](https://img.shields.io/github/pipenv/locked/dependency-version/vallzter/Team12/psycopg2)

---
### Collaborators

- Bjarki Már Friðriksson
- Elmar Ólafsson
- Fannar Leó Örvarsson
- Garpur Hnefill Emilíuson
- Gunnlaugur Hlynur Birgisson
- Hrafnkell Þorri Þrastarson
- Valgeir Ingi Þórðarson
- Ýmir Þórleifsson

---
### Description of the project
The project is a website, developed in Django, for users to easily buy meal packages containing groceries. Similar to Eldum Rétt or Blue Apron, the service will send ingredients to a customer periodically, e.g. on a weekly basis or more often.

---
## Sprints

### Sprint 1
We decided on building the website with Django as framework connected to a Postgres as database. Possibly using Atomic for the UI in the future. We are currently using built-in models, admin and users. As of now, the website contains functionality for users to register, login, look at their profile, logout and delete their account.

---

### Sprint 2
We desided that we wanted to implement two critical components to the website, products and online shopping. We used the restful API architecture to display the products. But making the online shopping was more diffcult than we thought, 6 modelst needed to be implemented for the database. But we managed to create the views and get it up and running.

---
## Software architecture

Our software is designed in well defined layers; Presentation Layer, Logic Layer and Data Layer.

![](readme_images/layers.png)

We are using Django to develop both the PL and LL. In the PL we use Django templates, that use HTML and CSS along with a bit of Python. In the LL we only use Python to build Django views, that decide on templates to show user. We also build Django models, that decide what and how data is stored.

The data layer is stored in SQL using Postgres, we store our models in SQL table format.

---
## How to run
Have [Python 3.8](https://www.python.org/downloads/) and [pip](https://bootstrap.pypa.io/get-pip.py) installed. In the root directory, Team12, open the shell. 
```
> pip install pipenv
> pipenv install
```
Now run the server
```
> cd src\Team12
> py manage.py runserver
```
Now you can visit our [website](http://localhost:8000).

---
### How to download `pip.py`

Download [pip](https://bootstrap.pypa.io/get-pip.py). 
Open the shell where `get-pip.py` was downloaded.

```
> python get-pip.py
```
---

### How to test
```
> python manage.py test
```

## Pictures
<div style="display:flex; flex-wrap;">
    <div>
        <p>Homepage</p>
        <img src="readme_images/homepage.png" width="200"/>
    </div>
    <div>
        <p>Profile Page</p>
        <img src="readme_images/profilepage.png" width="200"/>
    </div>
    <div>
        <p>Product Page</p>
        <img src="readme_images/productpage.png" width="200"/>
    </div>
    <div>
        <p>Product Detailed</p>
        <img src="readme_images/productdetailed.png" width="200"/>
    </div>
    <div>
        <p>Cart Page</p>
        <img src="readme_images/cartpage.png" width="200"/>
    </div>
</div>