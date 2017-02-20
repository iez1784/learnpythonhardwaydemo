#!/usr/bin/ python
# -*-coding:utf-8 -*-

print "How old are you?",
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)


"""
D:\gitlab\learnpythonhardwaydemo\exercise11>python "Asking Questions.py"
How old are you? 38
How tall are you? 6'2"
How much do you weigh? 180lbs
So, you're '38' old, '6\'2"' tall and '180lbs' heavy.
"""

print "What is your name?",
name = raw_input()

print "Boy or gril?",
gender = raw_input()


print "So, you're %r, %r" % (name, gender)