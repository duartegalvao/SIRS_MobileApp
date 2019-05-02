# SIRS Mobile App

## Description

This is part of a project for the [Network and Computer Security (SIRS)](https://fenix.tecnico.ulisboa.pt/disciplinas/SIRS/2018-2019/1-semestre) course in Instituto Superior Técnico of the University of Lisbon.

The repo contains the SIRS project mobile app component.

## Instructions

### Set-up

After cloning the project, you should create a virtual-env in the root folder, as follows:

```bash
virtualenv -p python3 mobile-env
```

### Running

Make sure you are inside the environment:

```bash
source mobile-env/bin/activate
```

Your shell prompt should have "`(mobile-env)`" in the beginning.

Then, make sure all of the project requirements are installed:

```bash
pip3 install -r requirements.txt
```

After that you can just run the test-server:

```bash
python3 mobile/manage.py runserver
```

### Developing

Django documentation is available [here](https://docs.djangoproject.com/en/2.1/).

### Exiting

To leave the environment, run:

```bash
deactivate
```

## Team

| Student Number | Name             | Github Profile                                  |
| -------------- | ---------------- | ----------------------------------------------- |
| 83422          | Amândio Faustino | [Nandinski](https://github.com/Nandinski)       |
| 83449          | Duarte Galvão    | [duartegalvao](https://github.com/duartegalvao) |
| 83524          | Marta Cruz       | [rbouru](https://github.com/rbouru)             |
