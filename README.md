skeleton
========

Skeleton is a Django project template developed to encourage rapid contruction of research based, academic websites.

Installation 
============

Easy.

Go to where you store your git controlled code, make a directory to store your project and change to the new directory:

```
cd git
mkdir myproject
cd myproject
```

Make a virtualenv and intsall django:

```
mkvirturalevn myproject
pip install django
```

Copy the skeleton project template into the new directory, notice that you are starting a django project using the command --template. After the zip url from git hub, be sure to change "myprojectname" with the name of your project:

```
django-admin.py startproject --template https://github.com/cultureplex/skeleton/zipball/master --extension py myprojectname
```

Next 









