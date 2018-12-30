# The Register

A unique website that helps both the educators and the students to keep a track of their attendance.
Faculties can easily take attendance of their classes online using their laptops and mobile devices
and the students will also be able to keep a track of their attendance.

## **Technologies and Tools**  

**Language** - Python 3.6  
**Backend Framework** - Django 2.1  
**Database** - POSTGRESQL  
**DBMS** - Pgadmin  
**Version-control** - Git and Github  
**JavaScript Library** - jquery
**Style Libraries** - Bootstrap, Material Design  

## **Instructions to run locally**  

1. Install Python and some dev tools for Python
- `$ sudo apt-get install python-pip python-dev build-essential`
- `$ apt install Python3.6`
- use easy_install for older versions of ubuntu e.g -$ easy_install python3-pip
2. Install Pip
- `$ apt install python3-pip`
3. Install other requirements given` in requirements.txt file
- `$ pip install requirements.txt
4. Modify database engine,
- Rename the database section in settings.py
- add username and password and port accordingly
- save changes
5. Sync db and make superuser
- `$ python manage.py makemigrations`
- `$ python manage.py migrate`
- `$ python manage.py createsuperuser`
6. Collect Static files
- `python manage.py collectstatic`
7. Runserver
- `$ python manage.py runserver`
- `$ visit 127.0.0.1:8000`  

## Contributor
- [Rohit Raj Anand](https://github.com/rht6226)