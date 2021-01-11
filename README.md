# Todo-logs (backend)

Uses Django as a backend to store a list of todo's. Built with
``Django`` version 3.1.5,  ``django-cors-headers`` version 3.6, ``Django Rest Framework`` (DRF) version 3.12.2 and ``DRF Simple JWT`` version 4.6.

## Usage
* Create a virtual environment with ``python3 -m venv {your-env}`` and activate it with ``source {your-env}/bin/activate``.
* Install the above packages (for example with pip): \
    ``python -m pip install django django-cors-headers djangorestframework djangorestframework-simple-jwt``
* Create ``backend/secret_key.py`` (same directory as ``settings.py``) with the line ``SECRET_KEY = 'YourSecretKey'``.
* Update ``CORS_ALLOWED_ORIGIN_REGEXES`` in ``settings.py`` to include this app's front-end domain. 
* Run the following commands:
    * ``python manage.py migrate``
    * ``python manage.py createsuperuser``
    * ``python manage.py runserver``
* The development server should be up and running at ``http://localhost:8000``. Other relevant url's are in ``backend/url.py``.

## Credits
<https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react>
<https://medium.com/@dakota.lillie/django-react-jwt-authentication-5015ee00ef9a>