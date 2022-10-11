# Django with Geo Location

<img width="891" alt="Screenshot 2022-10-11 at 17 53 10" src="https://user-images.githubusercontent.com/43213479/195140985-380ab15a-b953-4414-8a13-c2340b4e6099.png">

The study project from [Udemy](https://www.udemy.com/course/django-with-geolocation/).


## What will you learn
* how to use django with geolocation
* use of external libraries such as: geopy, geoip2, folium
* how to work with maxmind geoip database
* how to visualize points on the map, add markers, draw lines between points and calculate the distance


## Setup

You can run the provided example project on your local machine by following the steps outlined below.

Create a new virtual environment:


Navigate to [Maxmind](https://www.maxmind.com) for download databases:
* GeoLite2-City.mmdb
* GeoLite2-Country.mmdb


```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source ./venv/bin/activate
```

Navigate to the folder for the step you're currently on.

Install the dependencies for this project if you haven't installed them yet:

```bash
(venv) $ python -m pip install -r requirements.txt
```

Make and apply the migrations for the project to build your local database:

```bash
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
```

Create a superuser that allows you to log in to your Django admin portal:

```bash
(venv) $ python manage.py createsuperuser
```

Run the Django development server:

```bash
(venv) $ python manage.py runserver
```

Navigate to `http://localhost:8000/admin` and log in with your superuser credentials. 

