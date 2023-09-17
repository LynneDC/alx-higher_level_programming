#Python - Object-relational mapping

## Introduction

This README file provides instructions and information for the Python - Object-relational mapping project. This project focuses on working with Python, SQLAlchemy, and MySQL databases. You will be working with Python's Object-Relational Mapping (ORM) to interact with a MySQL database. The project aims to help you understand the basics of connecting to a database, performing SQL operations, and using SQLAlchemy to simplify database interactions.

## Table of Contents

1. [Background Context](#background-context)
2. [Requirements](#requirements)
3. [Tasks](#tasks)
   - [Task 0: Get all states](#task-0-get-all-states)
   - [Task 1: Filter states](#task-1-filter-states)
   - [Task 2: Filter states by user input](#task-2-filter-states-by-user-input)
   - [Task 3: SQL Injection...](#task-3-sql-injection)
   - [Task 4: Cities by states](#task-4-cities-by-states)
   - [Task 5: All cities by state](#task-5-all-cities-by-state)
   - [Task 6: First state model](#task-6-first-state-model)
   - [Task 7: All states via SQLAlchemy](#task-7-all-states-via-sqlalchemy)
   - [Task 8: First state](#task-8-first-state)
   - [Task 9: Contains 'a'](#task-9-contains-a)
   - [Task 10: Get a state](#task-10-get-a-state)
   - [Task 11: Add a new state](#task-11-add-a-new-state)
   - [Task 12: Update a state](#task-12-update-a-state)
   - [Task 13: Delete states](#task-13-delete-states)
   - [Task 14: Cities in state](#task-14-cities-in-state)
4. [Resources](#resources)
5. [Getting Started](#getting-started)
6. [Usage](#usage)
7. [Contributing](#contributing)
8. [License](#license)

## Background Context

In this project, you will work with Python's Object-Relational Mapping (ORM) to interact with a MySQL database. You will connect to the database, execute SQL queries, and perform various database operations using SQLAlchemy, an ORM tool. The project aims to help you understand the fundamentals of database interactions and the advantages of using an ORM.

## Requirements
### Installation Instructions

- To create a Python Virtual Environment, allowing you to install specific dependencies for this Python project, you can use the following commands:

```bash
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

- To install the MySQLdb module version 2.0.x, you'll need to have MySQL installed. You can follow the instructions provided [here](https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/) to install MySQL 8.0 on Ubuntu 20.04.


install MySQLdb:

```bash
$ pip install mysqlclient
```

- To install SQLAlchemy version 1.4.x, use the following command:

```bash
$ pip install SQLAlchemy
```

- Ensure you have a MySQL server running and have the necessary credentials and database set up for this project.

## Tasks

### Task 0: Get all states

In this task, you will retrieve all the states from the database and print them to the standard output.

**File**: `0-select_states.py`

### Task 1: Filter states

You will filter and print the states that start with the letter 'N'.

**File**: `1-filter_states.py`

### Task 2: Filter states by user input

Extend the previous task to accept user input and filter the states accordingly.

**File**: `2-my_filter_states.py`

### Task 3: SQL Injection...

Show the dangers of SQL injection by accepting user input and querying the database without proper input sanitization.

**File**: `3-my_safe_filter_states.py`

### Task 4: Cities by states

Write a Python script that lists all cities from the database in ascending order by `cities.id`.

**File**: `4-cities_by_states.py`

### Task 5: All cities by state

Print all cities for a given state (given as input) using SQLAlchemy.

**File**: `5-filter_cities.py`

### Task 6: First state model

Define a State model in SQLAlchemy and display all records from the states table.

**File**: `model_state.py`

### Task 7: All states via SQLAlchemy

Print all `State` objects from the database using SQLAlchemy.

**File**: `7-model_state_fetch_all.py`

### Task 8: First state

Print the first `State` object from the database using SQLAlchemy.

**File**: `8-model_state_fetch_first.py`

### Task 9: Contains 'a'

Print all `State` objects that contain the letter 'a' using SQLAlchemy.

**File**: `9-model_state_filter_a.py`

### Task 10: Get a state

Fetch a specific `State` object by id using SQLAlchemy.

**File**: `10-model_state_my_get.py`

### Task 11: Add a new state

Add a new `State` object to the database using SQLAlchemy.

**File**: `11-model_state_insert.py`

### Task 12: Update a state

Change the name of a `State` object using SQLAlchemy and commit the change.

**File**: `12-model_state_update_id_2.py`

### Task 13: Delete states

Delete all `State` objects with a name containing the letter 'a' using SQLAlchemy.

**File**: `13-model_state_delete_a.py`

### Task 14: Cities in state

Print all `City` objects from the database that are linked to a specific `State` object using SQLAlchemy.

**File**: `14-model_city_fetch_by_state.py`

## Resources

- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/)
- [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/20/orm/tutorial/index.html)
- [MySQLdb Documentation](https://mysqlclient.readthedocs.io/en/2.0/index.html)

## Getting Started

Follow the installation instructions to set up your Python environment and install the necessary dependencies. Make sure your MySQL server is running, and you have the required credentials and database set up.

## Usage

To run any of the tasks, execute the corresponding Python script in your terminal. For example:

```bash
$ python 0-select_states.py
```

Refer to the individual task descriptions for more details on each task.

## Contributing
- no contribution allowed at the moment
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

