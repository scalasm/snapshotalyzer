# Snapshotalyzer
Python application that manages AWS EC2 snapshots

# Requirements

This project uses [pipenv](https://opensource.com/article/18/2/why-python-devs-should-use-pipenv), so you need it to be installed in your sistem:
```
pip3 install pipenv
pipenv --three
pipenv install boto3
pipenv install -d ipython
pipenv install -d pylint
```

# How to run

```
pipenv install
pipenv run python shotty/shotty.py
```

# Pipenv hints

See the [official docs](https://packaging.python.org/tutorials/managing-dependencies/) first and foremost!

## Run the shell to get the exact environment:
```
pipenv shell
```

## Install additional dependencies

```
pipenv install requests
```