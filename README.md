# Django-Blog
a simple django blog website 

# About


The website exposes a blog with the following elements:
-Title.
-A photo.
-Text content of a post.
-Tags of a post.

It was made using Python 3.6 + Django and database is SQLite. Bootstrap was used for styling. 

There is a login and registration functionality included.

The admin can add, modify or delete any article.

# Pre-requisites
[ Optional] Install virtual environment:
```
$ python -m virtualenv env
```

[ Optional] Activate virtual environment:

On macOS and Linux:
```
$ source env/bin/activate
```
On Windows:
```
$ .\env\Scripts\activate
```


# How to run

You can run the application from the command line with manage.py. Go to the root folder of the application.

Run migrations:
```
$ python manage.py migrate
```
Run server on port 8000:
```
$ python manage.py runserver 8000
```
## Docker

It is also possible to run the blog app using docker:

Build the Docker image:
```
$ docker build -t reljicd/django-blog -f docker\Dockerfile .
```
Run the Docker container:
```
$ docker run --rm -i -p 8000:8000 reljicd/django-blog
```

# Post Installation
Go to the web browser and visit http://localhost:8000/home

Admin username: admin

Admin password: admin


Django Admin
It is possible to add additional admin user who can login to the admin site. Run the following command:
```
$ python manage.py createsuperuser
```
Enter your desired username and press enter.
```
Username: admin_username
```
You will then be prompted for your desired email address:
```
Email address: admin@example.com
```
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
```
Password: **********
Password (again): *********
```
Superuser created successfully.
Go to the web browser and visit http://localhost:8000/admin
