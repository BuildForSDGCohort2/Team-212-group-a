## Team-212-group-a

## Smartfarm

### Description

A web application that assits the farmers throughout the whole farming live cycle starting from land preparation,crop and seed selection,sowing, irragation, growth, fertillizing, harvesting, storage as well as marketting.


### Technologies used

- Python
- Django
- Postgresql
- Bootstrap
- Html
- Css

### set-up and installation instructions

You need a few things to get the project running on your machine:-

#### Requirements

- Python3.8 or 3.7 or 3.6
- Pip
* Postgresql
* Postgis >=3.0.0
* GDAL >=2.4.0
* GEOS >=3.7.2
* PROJ>=5.2.0


#### Installation for developers

-Clone the application from this url...https://github.com/BuildForSDGCohort2/Team-212-group-a-backend.git/
- Create a virtual environment
- Activate the virtual environment
- Install all the  application dependencies using~ _pip install -r requirements.txt_ or \*install them individualy using~ \*pip install <package-name>


#### Set-up instructions

- Create a database named _smartfarmdb_
* Navigate _smartfarmdb_ and add the postgis extension using the command _CREATE EXTENSION postigis;_
* In the root folder, create a file named *.env* and add the following settings:
 `
 >##### SECRET_KEY = <YOUR SECRET_KEY>
>##### DB_NAME = 'smartfarmdb'
>##### DB_PASSWORD = <YOUR DATABASE_PASSWORD>
>##### DB_USER = <YOUR DATABASE_USER>
>##### DB_HOST = <YOUR DATABASE_HOST>
>##### MODE = 'dev'
>##### ALLOWED_HOSTS = '*'
>##### DEBUG = True
>##### DISABLE_COLLECTSTATIC= 1 `




#### Running the application

* While inside the root folder, ensure your virtual environment is activated and run *python3.8 manage.py migrate*
* Run python3.8 manage.py runserver
* Open your browser and navigate to the url:http://127.0.0.1:8000/

### Developers

#### Kindly add your github name here

#### [Paul Wamaria](https://github.com/Paulwamaria)

#### [Sharon Kerubo](https://github.com/Sharon-Kerubo)

#### [Wendy Munyasi](https://github.com/wendymunyasi)
# Team-212-group-a

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/29b9f411967f4b17879fb3f3407dc298)](https://app.codacy.com/gh/BuildForSDGCohort2/Team-212-group-a-backend?utm_source=github.com&utm_medium=referral&utm_content=BuildForSDGCohort2/Team-212-group-a-backend&utm_campaign=Badge_Grade_Settings)
