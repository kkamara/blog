# blog

This repository follows Tomi Tokko's course Python Backend Web Development Course at https://www.youtube.com/watch?v=jBzwzrDvZ18 .

* [Requirements](#requirements)

* [Installation](#installation)

* [Usage](#usage)

* [Django Shell](#django-shell)

* [Cache View Templates](#cache-view-templates)

## Requirements

* [Tested using Python 3.13](https://www.python.org)

## Installation

```bash
pip install virtualenv && \
  virtualenv env && \
  source env/bin/activate

python manage.py makemigrations
python manage.py migrate
```

## Usage

```bash
python manage.py runserver
# http://localhost:8000
```

## Django Shell

```bash
python manage.py shell
```

## Cache View Templates

```bash
python manage.py collectstatic
```
