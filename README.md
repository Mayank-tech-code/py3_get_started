# Getting started with python 3 - A minimalistic guide

# Pre-requisites
```
Python (Code tested using 3.8.2)
https://www.python.org/downloads/

Editor: Visual Studio Code. It is free and supports debugging.
https://code.visualstudio.com/download

Python plugin for visual studio guidelines
https://code.visualstudio.com/docs/python/python-tutorial

Postgres installation
https://www.postgresql.org/download/windows/ 

PGAdmin installation
https://www.postgresql.org/ftp/pgadmin/pgadmin4/v4.22/windows/

Default install location of python on windows 10
C:\Users\<USER_NAME>\AppData\Local\Programs\Python\<PYTHON_VERSION>

Default pip location on windows 10 to be added to path environment variable
C:\Users\<USER_NAME>\AppData\Local\Programs\Python\<PYTHON_VERSION>\Scripts
```

# Hello World
First python program
```
hello_world.py
```

# Basic Data Types
Demonstrates string, int and decimal data
```
basic_data_types.py
```

# Control Statement
Shows how a decision is made
```
control_statement.py
```

# Loops
Shows why loop (Used when the number of steps is not known in advance)
```
while_loop.py
```
Shows nested statements and indentation

```
nested_while.py
```


Shows for loop (Used when the number of steps is known in advance)
```
for_loop.py
```

# Lists
Demonstrates the list collection (e.g. used to represent say a collection of players in a cricket team)
```
lists.py
```

# Dictionary
Demonstrates the dictionary collection (e.g. think about a shopping mall that gives a token and keeps your bag). Also demonstrates how to use object as a key.
```
dictionary.py
dictionary_object_as_key.py
```

# Function
Demonstrates functions in python (e.g. think about different services like college, hospital, bank etc. they provide specific services or functions that we used.)
```
functions.py
```

# Recursion
For fun
```
recursion.py
```

# Class, Inheritance and Modules
Demonstrates class, inheritance and how they are placed in the separate module and then used in another file.
```
class_module.py
using_class.py
```

# Files
Demonstrates open file, write to it, close the file, open it again, read its contents and close it.
```
file_usage.py
```

# Relational database (postgres)

```
pip install psycopg2

Create a database using pgadmin 4

CREATE TABLE COLLEGE(
   ID SERIAL PRIMARY KEY,
   NAME VARCHAR(50) NOT NULL,
   ADDRESS VARCHAR(50)
);

CREATE TABLE STUDENT(
   ID SERIAL PRIMARY KEY,
   NAME VARCHAR(50) NOT NULL,
   COLLEGE_ID int references COLLEGE(ID)
);

database.py
```

# Linear Regression
Demonstrates pandas to read csv, scikit-learn for linear regression and matplotlib for visualization
Credits: https://towardsdatascience.com/linear-regression-in-6-lines-of-python-5e1d0cd05b8d

```
pip install pandas
pip install matplotlib
pip install scikit-learn

linear_regression.py
```

# Exception
Demonstrates exception for divide by zero and opening of a non-existing file.
```
exception.py
exception2.py
```


# Matchsticks game
Demonstrates a simple turn based 21 matchsticks game. 

```
matchsticks.py
```
# Simple Web Application

```
pip install flask
```
