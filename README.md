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
### Sprint 3
The team decided to focus more in this sprint on getting the tests up and running, as it had been a huge headache for quite some time, as well as the lecture aspects. We finally managed to fix the testing issues and added some nice features as well. Sketching up all the diagrams went rather smoothly, except for the delivery diagram, as it proved to be fairly difficult finding an example of such online or in the textbook.

#### Dependency injection

When adding meal package to the cart, the add(request) method in src/Team12/cart/views.py has a setter injection which is used when setting the customer. The variable customer is set with the correct User object, which represents the customer who is adding a meal package to his cart.

#### Single Responsibility Principle

The function detailed_product() has the single responisibility of sending out details on a product to a template  
The function cancelSubscription() has the single responsibility of canceling any subscription  
The function editProfileRedirect() has the single responsibility if redirecting to an edit profile template  
The function edit_quantity() has the single responsibility of recieving a number and changing the quantity of a product in the cart

---
### Sprint 4

#### Conway's law

As Conway's law states: ,,Any organization that designs a system (defined broadly) will produce a design whose structure is a copy of the organization's communication structure.".

Therefore, as our software is structured in a layered architecture, our communication structure would have certain team/s working on a particular layer, whether it is the presentation layer, the logic layer or the data layer.

This is not really the case in our project. While this show in some extend, where some team members tend to work only in one layer of the software, but more often that not team members work across all layers, i.e. from the presentation layer to the data layer

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
```
First thing you need to do is create a customer model
1. Create an account
2. Go to profile and click "Edit Profile"
3. Fill in all the fields
4. Now you can freely use the website

```
---
### How to download `pip.py`

Download [pip](https://bootstrap.pypa.io/get-pip.py). 
Open the shell where `get-pip.py` was downloaded.

```
> python get-pip.py
```
---

### How to test
IMPORTANT: if the user wishes to run the tests, then he has to do so on a local database
our elephantSQL database does not allow us to run tests as we are no granted the permission to
create a dummy database for running the tests

```
> python manage.py test
# or for the coverage run 
> coverage run manage.py test
```



## Coverage Report

Name                                            Stmts   Miss  Cover
-------------------------------------------------------------------
Team12\__init__.py                                  0      0   100%
Team12\settings.py                                 22      0   100%
Team12\urls.py                                      5      0   100%
cart\__init__.py                                    0      0   100%
cart\admin.py                                       1      0   100%
cart\migrations\0001_initial.py                     5      0   100%
cart\migrations\0002_auto_20201004_1419.py          7      0   100%
cart\migrations\__init__.py                         0      0   100%
cart\models.py                                     83     21    75%
cart\tests.py                                      10      0   100%
cart\urls.py                                        3      0   100%
cart\views.py                                      96     75    22%
manage.py                                          12      2    83%
meal_package\__init__.py                            0      0   100%
meal_package\migrations\__init__.py                 0      0   100%
meal_package\tests.py                               1      0   100%
product\__init__.py                                 0      0   100%
product\admin.py                                    5      0   100%
product\migrations\0001_initial.py                  5      0   100%
product\migrations\0002_mealplan_allergies.py       4      0   100%
product\migrations\__init__.py                      0      0   100%
product\models.py                                  18      2    89%
product\tests.py                                   25      0   100%
product\urls.py                                     5      0   100%
product\views.py                                   19      0   100%
user\__init__.py                                    0      0   100%
user\admin.py                                       2      0   100%
user\migrations\0001_initial.py                     7      0   100%
user\migrations\__init__.py                         0      0   100%
user\models.py                                     20      2    90%
user\tests.py                                      64      0   100%
user\urls.py                                        4      0   100%
user\views.py                                      84     14    83%
-------------------------------------------------------------------
TOTAL                                             507    116    77%

As it can be seen above, all our apps are almost completely coved by the test. All that remains is the cart view. 


## Testing

Regarding our tests, we have tried relentlessly in the past two sprints to get our test code work as should. However, our database raises an error when trying to test functionality regarding it, saying that certain permission is needed. As said, we have tried with all our might to give us somehow this certain permission or bypass this in some way, but without any success. <br />
<br />
Our project is at that stage that our only tests that we can implement is regarding the database, e.g. that the user is created correctly, products are fetched in the correct manner, data is manipulated the right way etc. <br />
<br />
We are currently using Elephantsql and Postgres but we are strongly considering changing services for next sprint, as this combo is causing us severe headache. Also, as we are using the free tier, allowing only 5 connections which complicates the matter even more. <br />
<br />
We have installed the package, coverage, which at the moment reports 39% of the code is tested.

## Design Patterns

We utilized 6 design patterns in sprint 2 which are listed below:
<ul>
    <li>The user accesses the meal packages via a registry (database).
	The meal package database feeds information that can be displayed. 
	However, it can also be accessed by search and sort interfaces.</li>
    <li>The meal packages themselves are value objects and their prices can be compared.
	They are individually defined and have a few attributes.
	However, they are used by the user when viewing, selecting and purchasing.</li>
    <li>The selected delivery time of an order is represented by a service stub.
	External factors influence available time slots, e.g. the number of prepping and delivery staff as well as the number of deliveries on a given day.</li>
    <li>Delivery place is an example of a gateway.
	The delivery gateway is gets information such as the user's location and cart contents, and returns available delivery locations.</li>
    <li>The sorting implementation for the meal packages is a seperated interface.
	It is dependant on the data interface but other parts can also access the data irrespective of the sort.</li>
    <li>The meal packages that users see displayed are managed by a mapper.
	The admininstrator can see and edit the packages which are then displayed to users if available.</li>
</ul>

## Screens
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
