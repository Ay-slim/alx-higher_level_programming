# Python hello world (files and their functions)
gp: A shell script to automate adding, commiting, and pushing files to the remote git repo

0-run: Bash shell script to run a python file via an env variable

1-run_inline: Runs a chunk of python code inline via an env variable

2-print.py: Prints a simple message in python

3-print_number.py: Prints a number

4-print_float.py: Prints pi to 2 decimal places

5-print_string.py: Prints a string

6-concat.py: Concatenates strings

7-edges.py: Split a spring

8-concat_edges.py: Complete this source code to print object-oriented programming with Python, followed by a new line.

You can find the source code here
You are not allowed to use any loops or conditional statements
Your program should be exactly 5 lines long
You are not allowed to create new variables
You are not allowed to use string literals

9-easter_egg.py: Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)

10-check_cycle.c: Technical interview preparation:

You are not allowed to google anything
Whiteboard first
This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.
Write a function in C that checks if a singly linked list has a cycle in it.

Prototype: int check_cycle(listint_t *list);
Return: 0 if there is no cycle, 1 if there is a cycle
Requirements:

Only these functions are allowed: write, printf, putchar, puts, malloc, free

100-write.py: Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

Use the function write from the sys module
You are not allowed to use print
Your script should print to stderr
Your script should exit with the status code 1

101-compile: Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE

The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)

102-magic_calculation.py: Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
Tip: Python bytecode
