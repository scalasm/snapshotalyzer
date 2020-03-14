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