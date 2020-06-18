# REST API Implementation

Django REST framework is a powerful and flexible toolkit for building Web APIs.

Some reasons you might want to use REST framework:

- The Web browsable API is a huge usability win for your developers.
- Authentication policies including packages for OAuth1a and OAuth2.
- Serialization that supports both ORM and non-ORM data sources.
- Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
- Extensive documentation, and great community support.
- Used and trusted by internationally recognised companies including Mozilla, Red Hat, Heroku, and Eventbrite.


# Usage

Run server.
```
$ ./manage.py migrate
$ ./manage.py createsuperuser
$ ./manage runserver
```

Ex) Send GET Request.
```
$ curl 'http://localhost:8000/users/vision_api/?format=json&url=https%3A%2F%2Fwww.sciencemag.org%2Fsites%2Fdefault%2Ffiles%2Fstyles%2Farticle_main_large%2Fpublic%2Fdogs_1280p_0.jpg'
```
