# SIM LABSOS
SIM LABSOS is a website-based application specifically used by students of the Yogyakarta Nahdlatul Ulama University in handling social laboratories,

#informatika2017

# First Preparations

For initial preparation to run * SIM LABSOS * applications. Python version 3 is needed, PostgresSQL, operating system Linux, (or using another OS).

1. Modules used:
 - python3 >= 3.4
 - Django == 2.2
 - django-bootstrap-datepicker-plus == 3.0.5
 - django-crispy-forms == 1.9.2
 - Pillow == 7.0.0
 - psycopg2 == 2.8.5

## Basic Settings

Requirements to start the project must use **python version 3**,

you can download and install [here](https://www.python.org/download/releases/3.0/),

This project also uses the **Postgre database**, the settings can be found in the **SIM_PKL** folder then the **setting.py** 

you can install and configuration in this link [here](https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django)

It is recommended to **use env**, which can be found [here](https://www.petanikode.com/python-virtualenv/)

## Installing Pip
pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org or if you are working in a Virtual Environment created by virtualenv or venv. Just make sure to upgrade pip.

# Windows
The Python installers for Windows include pip. You should be able to access pip using:

```bash
py -m pip --version
pip 9.0.1 from c:\python36\lib\site-packages (Python 3.6.1)
```
You can make sure that pip is up-to-date by running:
```bash
py -m pip install --upgrade pip
```

# Linux and macOS

Debian and most other distributions include a python-pip package, if you want to use the Linux distribution-provided versions of pip see Installing pip/setuptools/wheel with Linux Package Managers.

You can also install pip yourself to ensure you have the latest version. It’s recommended to use the system pip to bootstrap a user installation of pip:

```bash
python3 -m pip install --user --upgrade pip
```
## Installing virtualenv

virtualenv is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. You can install virtualenv using pip.

On macOS and Linux:

```bash
python3 -m pip install --user virtualenv
```
On Windows

```bash
py -m pip install --user virtualenv
```

## Creating a virtual environment

venv (for Python 3) and virtualenv (for Python 2) allow you to manage separate package installations for different projects. They essentially allow you to create a “virtual” isolated Python installation and install packages into that virtual installation. When you switch projects, you can simply create a new virtual environment and not have to worry about breaking the packages installed in the other environments. It is always recommended to use a virtual environment while developing Python applications.

To create a virtual environment, go to your project’s directory and run venv. If you are using Python 2, replace venv with virtualenv in the below commands.

On macOS and Linux:
```bash
python3 -m venv env
```
On Windows:
```bash
py -m venv env
```

## Install Packages

To install all the required packages, run the command

```bash
pip3 install -p requirements.txt / pip3 install -r requirements.txt
```
then install pillow and datepicker plus, countible field, crispy forms

click the following link

1. Crispy form
```bash
pip3 install django-crispy-forms
```

2. Pillow 
```bash
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

3. Datepicker Plus
```bash
pip3 install django-bootstrap-datepicker-plus
```

4. Countible field
```bash
pip3 install coa-django-countable-field
```

### Add app name in settings.py:
```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'bootstrap_datepicker_plus',
    'accounts',
    'countable_field',
    'home',
    'dosen',
    'mahasiswa',
    'catatan',
    'mitra',
    'forum',
]
```
## Migrate the Project

before you run this project you must to be migrate this data 

```bash
python3 manage.py migrate
```

## Run the Project

to run the project, you can use python / python3 

```bash
python3 manage.py runserver

```
## Deploy
this project has been deployed in Heroku (Cloud Application Platform) in this link [here](https://labsosv2.herokuapp.com/)

This project has 3 roles, namely college student, lecturers and staff, 
You can sign in with the account below :

### Collage Student
- Username = user
- Password = praxis123

or you can sign up in this apllication

### Lectures 
- Username = prof.tatam
- Password = praxis123

### Staff 
- Username = staf
- Password = praxis123
