# Bookmarks CRUD

TASK ASSIGNMENT:

Create a REST api for web bookmarks. These bookmarks can be private or
public. After authentication, users can create and delete / update their
bookmarks. They can also view their bookmarks and other users public
bookmarks. Anonymous users can only view public bookmarks. Every bookmark
should have "title","url" and "created_at" fields. Other fields are up to
you.

Additional important notes:

- use latest versions of Python and Django / Django Rest Framework; no other
  package is required for this task
- write tests (the bigger coverage, the better)
- please provide a script for running the endpoints (a text file with list of
  curl commands should do)
- add a readme file for project setup / test running

This task shouldn't take more than 3 hours to complete. Please send the code
even if not done in given time.

Bonus - answer these questions:

1) What database would you use for this project in production and why?
2) How would you implement a bookmark "newsletter" (users receive emails with
   newest public bookmarks)?
3) Write a sql statement of fetching all public bookmarks, not older than 10
   days, for a user with id = 1.


## Setup dev environment

Goal is to have latest stable versions of Python, Django and Django REST Framework

### Python on Ubuntu 18.04

Add PPA with latest python releases

```shell
sudo add-apt-repository ppa:deadsnakes/ppa
```

Install python 3.8

```shell
sudo apt install python3.8 python3.8-venv
```

Install pipenv to manage virtual environment and python packages

```shell
pip install pipenv
```

### Clone github repository

```shell
git clone https://github.com/msvalina/ksolutions && cd ksolutions
```


### Install dependencies and activate virtual environment

Inside ksolutions run

```shell
pipenv install

pipenv shell
```


## Testing

```shell
curl --user admin:mantis5c 'http://127.0.0.1:8000/bookmarks/' -X POST --data  '{ "is_public": true, "owner": 1, "title": "Foolish", "url": "http://foolish.com" }'
```