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
We decided on wanting to implement two critical components to the website; viewing of products and online shopping. We used the RESTful API architecture to display the products. But making the online shopping was more diffcult than we thought, 6 models needed to be implemented for the database. But we managed to create the views and get it up and running.

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

## Testing

Regarding our tests, we have tried relentlessly in the past two sprints to get our test code work as should. However, our database raises an error when trying to test functionality regarding it, saying that certain permission is needed. As said, we have tried with all our might to give us somehow this certain permission or bypass this in some way, but without any success. <br />
<br />
Our project is at that stage that our only tests that we can implement is regarding the database, e.g. that the user is created correctly, products are fetched in the correct manner, data is manipulated the right way etc. <br />
<br />
We are currently using Elephantsql and Postgres but we are strongly considering changing services for next sprint, as this combo is causing us severe headache. Also, as we are using the free tier, allowing only 5 connections which complicates the matter even more. <br />
<br />
We have installed the package, coverage, which at the moment reports 39% of the code is tested.

## Design Patterns

We utilized 6 design patterns in sprint 2 which are listed below: <br />
The registery was utilized with the meal package selection. <br />
Ingredients were implemented as a Value Object. <br />
The shopping Cart was a plugin design. <br />
The Delivery Time was a Service Stub. <br />
Delivery Place was an example of Gateway. <br />
The Shop Sorting system was a Seperate interface. <br />
Adding packages as administrator was an example of the mapper. <br />
Deleting packages was likewise an example of the same design principle.


## Pictures
<table>
    <tr>
        <th>
            Homepage
            <img src="readme_images/homepage.png" width="200"/>
        </th>
        <th>
            Profile Page
            <img src="readme_images/profilepage.png" width="200"/>
        </th>
        <th>
            Product Page
            <img src="readme_images/productpage.png" width="200"/>
        </th>
    </tr>
    <tr> 
        <th>
            Product Detailed
            <img src="readme_images/productdetailed.png" width="200"/>
        </th>
        <th>
            Cart Page
            <img src="readme_images/cartpage.png" width="200"/>
        </th>
    </tr>
</table>
