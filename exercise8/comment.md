# Printing, Printing

**Study Drills**

- 1

Do your checks, write down your mistakes, and try not to make the same mistakes on the next exercise.

- 2

Notice that the last line of output uses both single-quotes and double-quotes for individual pieces. Why do you think that is?

Because the last used didn't, if use single-quotes, you must use didn''t for trans it

- Question 1

Should I use %s or %r for formatting?

You should use %s and only use %r for getting debugging information about something. The %r will give you the "raw programmer's" version of variable, also known as the "representation."

- Question 2

Why do I have to put quotes around "one" but not around True or False?

Python recognizes True and False as keywords representing the concept of true and false. If you put quotes around them then they are turned into strings and won't work. You'll learn more about how these work in Exercise 27.

- Question 3

I tried putting Chinese (or some other non-ASCII characters) into these strings, but %r prints out weird symbols.

Use %s to print that instead and it'll work.


- Question 4

Why does %r sometimes print things with single-quotes when I wrote them with double-quotes?

Python is going to print the strings in the most efficient way it can, not replicate exactly the way you wrote them. This is perfectly fine since %r is used for debugging and inspection, so it's not necessary that it be pretty.


- Question 5

Why doesn't this work in Python 3?

Don't use Python 3. Use Python 2.7 or better, although Python 2.6 might work fine.


- Question 6
Can I use IDLE to run this?

No, you should learn to use the command line. It is essential to learning programming and is a good place to start if you want to learn about programming. IDLE will fail for you when you get further in the book.