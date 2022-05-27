# Flaskmin
Flaskmin is a simple admin app for manage user data

---

## Usage

### Clone

Clone this repository using the SSH or HTTPS method

```
git clone git@github.com:itsarreguin/flaskmin.git
```

```
git clone https://github.com/itsarreguin/flaskmin.git
```

### Virtualenv

Now, inside the folder root create a new virtual environment

```
cd flaskmin
```
#### Create venv in MacOs
```
python3 -m venv env
```
#### Create venv in Windows
```
python -m venv env

```
### Activate and deactivate virtual environment

#### MacOs
```
source env/bin/activate
```

#### Windows
```
.\env\Scripts\activate
```

#### Deactivate virtualenv in MacOs and Windows
```
deactivate
```

### Install requirements
To run this project we need install all dependencies and extensions saved in `requirements.txt` file. Runing the follow command to install

`Note` Only can connect a PostgreSQL db.

```
pip install -r requirements.txt
```

### DB connection
For connect a db all we need is a `.env` file to save database credentials. This file stores environment variables.

.env file goes to the project root
```
flaskmin
|- app
|- db
|- tests
|- .env
|- .gitattributes
|- .gitignore
|- LICENSE
|- README.md
|- requirements.txt
|_ wsgi.py
```
Inside `.env` file write the next lines
```
POSTGRESQL_USER = your_username
POSTGRESQL_PASSWORD = your_password
POSTGRESQL_HOST = host
POSTGRESQL_PORT = port
POSTGRESQL_DB = database_name
```
### Finally
Run wsgi.py file to start server
```
python3 wsgi.py
```
```
python wsgi.py
```

### License
This project is under <a href="./LICENSE">MIT license</a>