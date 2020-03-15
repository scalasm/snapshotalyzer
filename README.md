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
pipenv install -d setuptools
```

# How to create a redistributable package

We use setup tools:
```
pipenv run python setup.py bdist_wheel
```

Once you have done this, you can install it and run like a normal installed application:
```
pip3 install dist/snapshotalyzer-0.1-py3-none-any.whl
```

```
mario@scalasm-xps:~/src/online-courses/PythonCourse/Snapshotalyzer$ shotty
Usage: shotty [OPTIONS] COMMAND [ARGS]...

  Shotty manages snapshots

Options:
  --help  Show this message and exit.

Commands:
  instances  Commands for instances
  snapshots  Commands for snapshots
  volumes    Commands for volumes
```

```
mario@scalasm-xps:~/src/online-courses/PythonCourse/Snapshotalyzer$ pip3 show snapshotalyzer
Name: snapshotalyzer
Version: 0.1
Summary: Snapshotalyzer is a tool to manage AWS EC2 snapshots
Home-page: https://github.com/scalasm/snapshotalyzer
Author: Mario Scalas
Author-email: mario.scalas@gmail.com
License: GPLv3+
Location: /home/mario/.local/lib/python3.6/site-packages
Requires: boto3, click
Required-by: 
```


# How to run

## Show help
```
mario@scalasm-xps:~/src/online-courses/PythonCourse/Snapshotalyzer$ pipenv run 
```

```
python shotty/shotty.py --help
Usage: shotty.py [OPTIONS] COMMAND [ARGS]...

  Commands for instances

Options:
  --help  Show this message and exit.

Commands:
  list   List EC2 instances
  start  Start EC2 instances
  stop   Stop EC2 instances
```

## List EC2 instances
```
pipenv install
run python shotty/shotty.py list --project="Python Course"
```
will print out something like:
```
i-06922f2f1a6ea5a46, x86_64, t2.micro, running, eu-central-1b, ec2-3-127-148-5.eu-central-1.compute.amazonaws.com, Python Course
```

## Other EC2 commands
```
pipenv run python shotty/shotty.py stop --project="Python Course"
```

```
pipenv run python shotty/shotty.py start --project="Python Course"
```

```
pipenv run python shotty/shotty.py snapshots list
```

# Pipenv hints

* See the [official docs](https://packaging.python.org/tutorials/managing-dependencies/) first and foremost!
* [Why Python devs should use Pipenv](https://opensource.com/article/18/2/why-python-devs-should-use-pipenv)
* [Click website](https://click.palletsprojects.com/)
* [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
* [SetupTools](https://setuptools.readthedocs.io/en/latest/) for making redistributable packages

## Run the shell to get the exact environment:
```
pipenv shell
```

## Install additional dependencies

```
pipenv install requests
```