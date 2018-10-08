# Flask-App

This is a basic Flask app built with an application factory pattern and a single blueprint. It also contains Bootstrap 4 styles and FontAwesome icons.

## Getting Started

### Prerequesits
You need to have Python 3 and `pip` installed on your machine.

### Installing

Clone the repository:

```shell
git clone https://github.com/jasminefiner/flask-app.git
```

Set up and activate the virtual environment:

```shell
python3 -m venv venv
. venv/bin/activate
```

Install dependencies:

```shell
pip install -r requirements.txt
```

## Running the Tests

Automated testing with `unittest` available. In the command line, run:

```shell
flask test
```

## Running the Application

```shell
export FLASK_APP='application.py'
flask run
```

## Built With

- [Flask](http://flask.pocoo.org/): Web Framework
- [Flask-Bootstrap4](https://pypi.org/project/Flask-Bootstrap4/): Front-End CSS Framework
- [Font-Awesome](https://fontawesome.com/free): Icons
