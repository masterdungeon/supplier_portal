# Supplier Portal
---------------

This is a simple supplier portal in which supplier can register and update
their basic details and admin can see all the registations.

## Supplier Registration

User have to fill basic details to register, and email that is used while
registation can be used to updating profile.

## Profile Update

User can update and add some other details.

## Custom Admin Page

Admin can view all registation with search and sort option.

## Building

It is best to use the python `virtualenv` tool to build locally:

```sh
$ virtualenv-3.6 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver
```

Then visit `http://localhost:8000` to view the app.
