# Asking Questions?

**Study Drills**

- 1

In Terminal where you normally run python to run your scripts, type pydoc raw_input. Read what it says. If you're on Windows try python -m pydoc raw_input instead.

D:\gitlab\learnpythonhardwaydemo\exercise12>python -m pydoc raw_input
Help on built-in function raw_input in module __builtin__:

raw_input(...)
    raw_input([prompt]) -> string

    Read a string from standard input.  The trailing newline is stripped.
    If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
    On Unix, GNU readline is used if enabled.  The prompt string, if given,
    is printed without a trailing newline before reading.

- 2

Get out of pydoc by typing q to quit.


-3

Look online for what the pydoc command does.
[Python pydoc](https://docs.python.org/2/library/pydoc.html)

-4

Use pydoc to also read about open, file, os, and sys. It's alright if you do not understand those; just read through and take notes about interesting things.


- Question 1

How come I get SyntaxError: invalid syntax whenever I run pydoc?

You aren't running pydoc from the command line; you're probably running it from inside python. Exit out of python first.

- Question 2

Why does my pydoc not pause like yours does?

Sometimes if the help document is short enough to fit on one screen then pydoc will just print it.

- Question 3

When I run pydoc I get more is not recognized as an internal.

Some versions of Windows do not have that command, which means pydoc is broken for you. You can skip this Study Drill and just search online for Python documentation when you need it.

- Question 4

Why would I use %r over %s?

Remember %r is for debugging and is "raw representation" while %s is for display. I will not answer this question again so you must memorize this fact. This is the #1 thing people ask repeatedly, and asking the same question over and over means you aren't taking the time to memorize what you should. Stop now, and finally memorize this fact.


- Question 5

Why can't I do print "How old are you?" , raw_input()?

You'd think that'd work, but Python doesn't recognize that as valid. The only answer I can really give is, you just can't.