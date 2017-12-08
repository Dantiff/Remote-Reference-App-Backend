# Remote Reference App

Please find the live app working <strong><a href="http://bivestorg.pythonanywhere.com/">Here</a></strong>

This is a web app that allows remote users to look up debt status. The app assumes that there are remote users that need to periodically check the debt status of certain customers and at times download an excel report of customer information.


### Features

* Django backend in `./core`
* AngularJS 2 (v4) frontend in `./ngApp`
* Django REST framework for API support in `./rest_framework`
* Support and integration of both Jinja2 and Django template engines
* Jinja2 Template with variales from django and angular
* Testing support using Karma and Lite-Servers
* Makefile to make your life easy


### Development environment setup

Ensure you have the latest versions of <a href="https://help.pythonanywhere.com/pages/Node/"> npm and node (v4 and above) </a> to esure you can run es5 scripts without errors since VueJS is based on the es5 syntax.

Foremost, be sure to create a virtual environment for your project since the default python instance available will be used. Use the mkvirtualenv command as follows:

```bash
$ mkvirtualenv nenv
```

Install database client. For MySQL, istallation is given as follows:

For Python 2.7

```bash
$ pip install mysql-python
```

For Python 3.x

```bash
$ pip install mysqlclient
```

The requirements.txt file is meant to reduce the number of commands to execute.

These steps will install all required dependencies including development ones, run migrations and start dev server.


## Project Setup
```python
#Create a new Virtual Environment.
virtualenv appenv
cd appenv

#Install a database client
pip install mysqlclient

#Fork or clone this repo.
git clone https://github.com/Dantiff/Remote-Reference-App.git
cd Remote-Reference-App/ngApp/

#prepare the debelopment env
make install

#Open a new terminal window
cd ../

#Migrate and Run Development Server
make run
```


### PS*
There some setup you probably need to ensure are correct to ensure your app works. Some of these include:

   * Ensure the `SECRET_KEY` in your `settings.py` point to the correct key.
   * Ensure you have the correct settings for `DATABASES`, `WSGI_APPLICATION`, and `TIME_ZONE` in `settings.py`.
   * Ensure the folder for the Django REST framework sits on the root of the applications as follows: `./rest_framework`, `./rest_auth`.



