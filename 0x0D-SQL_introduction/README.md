# 0x0D. SQL - Introduction

## Resources
### Read or watch:

- [What is Database & SQL?](link-to-resource)
- [A Basic MySQL Tutorial](link-to-resource)
- [Basic SQL statements: DDL and DML](link-to-resource) (no need to read the chapter “Privileges”)
- [Basic queries: SQL and RA](link-to-resource)
- [SQL technique: functions](link-to-resource)
- [SQL technique: subqueries](link-to-resource)
- [What makes the big difference between a backtick and an apostrophe?](link-to-resource)
- [MySQL Cheat Sheet](link-to-resource)
- [MySQL 8.0 SQL Statement Syntax](link-to-resource)
- [Installing MySQL in Ubuntu 20.04](link-to-resource)

## Learning Objectives
### General
In this project, we will explore the fundamentals of SQL (Structured Query Language) and its application in MySQL. We will cover the following topics:

- Understanding the concept of a database and its significance
- Exploring relational databases and their role in data organization
- Defining SQL and its purpose in database management
- Introducing MySQL as a widely used relational database management system
- Learning how to create databases within the MySQL environment
- Distinguishing between Data Definition Language (DDL) and Data Manipulation Language (DML) and their respective uses
- Mastering the skills to create and alter tables using SQL
- Retrieving data from a table using the SELECT statement
- Performing data manipulation operations such as INSERT, UPDATE, and DELETE
- Exploring the concept of subqueries and their role in complex SQL queries
- Utilizing MySQL functions to enhance query capabilities

## More Info
### Comments for your SQL file (my_script.sql):

```sql
-- Retrieve the details of the first three students in Batch ID=3
-- This query is designed to showcase the excellence of Batch 3!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

### Installing MySQL 8.0 on Ubuntu 20.04 LTS
To set up MySQL 8.0 on Ubuntu 20.04, follow these steps:

1. Update the package index:
```bash
$ sudo apt update
```

2. Install the MySQL server:
```bash
$ sudo apt install mysql-server
```

3. Check the installed MySQL version:
```bash
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

### Connecting to your MySQL server
To connect to your MySQL server, follow these steps:

1. Access the MySQL monitor:
```bash
$ sudo mysql
```

2. You will be greeted with the MySQL monitor prompt:
```sql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)
```

3. To exit the MySQL monitor, use the following command:
```sql
mysql> quit
Bye
```

### Using "container-on-demand" to run MySQL
If you prefer a containerized environment for MySQL, consider the following steps:

1. Request a container with Ubuntu 20.04.
2. Connect to the container via SSH or the Web terminal.
3. Start MySQL within the container:
```bash
$ service mysql start
 * Starting MySQL database server mysqld
```

4. To list databases within the container, run the following command:
```bash
$ cat 0-list_databases.sql | mysql -uroot -p
```

## License
This project is licensed under the [MIT License](link-to-license).

Author: <LynneDC> <roselinedc1308@gmail.com>

