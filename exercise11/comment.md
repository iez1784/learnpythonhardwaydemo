# Asking Questions?

**Study Drills**

- 1

Go online and find out what Python's raw_input does.
[Python raw_input](https://docs.python.org/2/library/functions.html#raw_input)

- 2

Can you find other ways to use it? Try some of the samples you find.


-3

Write another "form" like this to ask some other questions.

-4

Related to escape sequences, try to find out why the last line has '6\'2"' with that \' sequence. See how the single-quote needs to be escaped because otherwise it would end the string?


- Question 1

How do I get a number from someone so I can do math?

That's a little advanced, but try x = int(raw_input()) which gets the number as a string from raw_input() then converts it to an integer using int().

- Question 2

I put my height into raw input like this raw_input("6'2") but it doesn't work.

You don't put your height in there, you type it directly into your Terminal. First thing is, go back and make the code exactly like mine. Next, run the script, and when it pauses, type your height in at your keyboard. That's all there is to it.

- Question 3

Why do you have a newline on line 8 instead of putting it on one line?

That's so that the line is less than 80 characters long, which is a style that Python programmers like. You could put it on one line if you like.

- Question 4

What's the difference between input() and raw_input()?

The input() function will try to convert things you enter as if they were Python code, but it has security problems so you should avoid it.


- Question 5

When my strings print out there's a u in front of them, as in u'35'.

That's how Python tells you that the string is Unicode. Use a %s format instead and you'll see it printed like normal.