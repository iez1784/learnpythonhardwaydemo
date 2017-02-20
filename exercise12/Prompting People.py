#!/usr/bin/ python
# -*-coding:utf-8 -*-

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

"""
D:\gitlab\learnpythonhardwaydemo\exercise12>python "Prompting People.py"
How old are you? 38
How tall are you? 6'2"
How much do you weight? 180lbs
So, you're '38' old, '6\'2"' tall and '180lbs' heavy.
"""


"""
D:\gitlab\learnpythonhardwaydemo\exercise12>python -m pydoc raw_input
Help on built-in function raw_input in module __builtin__:

raw_input(...)
    raw_input([prompt]) -> string

    Read a string from standard input.  The trailing newline is stripped.
    If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
    On Unix, GNU readline is used if enabled.  The prompt string, if given,
    is printed without a trailing newline before reading.
"""