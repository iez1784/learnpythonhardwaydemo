# What Was That?

**Study Drills**

- 1

Memorize all the escape sequences by putting them on flash cards.

- 2

Use ''' (triple-single-quote) instead. Can you see why you might use that instead of """?

the function as the same as use """

-3

Combine escape sequences and format strings to create a more complex format.

-4

Remember the %r format? Combine %r with double-quote and single-quote escapes and print them out. Compare %r with %s. Notice how %r prints it the way you'd write it in your file, but %s prints it the way you'd like to see it?


- Question 1

What if I wanted to start the months on a new line?

You simply start the string with \n like this:

"\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

- Question 2

I still haven't completely figured out the last exercise. Should I continue?

Yes, keep going. Instead of stopping, take notes listing things you don't understand for each exercise. Periodically go through your notes and see if you can figure these things out after you've completed more exercises. Sometimes though you may need to go back a few exercises and do them again.

- Question 3

What makes \\ special compared to the other ones?

It's simply the way you would write out one backslash (\) character. Think about why you would need this.


- Question 4

When I write // or /n it doesn't work.

That's because you are using a forward-slash / and not a backslash \. They are different characters that do very different things.


- Question 5

When I use a %r format none of the escape sequences work.

That's because %r is printing out the raw representation of what you typed, which is going to include the original escape sequences. Use %s instead. Always remember this: %r is for debugging, %s is for displaying.


- Question 6
I don't get Study Drill 3. What do you mean by "combine" escape sequences and formats?

One concept I need you to understand is that each of these exercises can be combined to solve problems. Take what you know about format strings and write some new code that uses format strings and the escape sequences from this exercise.

- Question 7
What's better, ''' or """?

It's entirely based on style. Go with the ''' (triple-single-quote) style for now but be ready to use either depending on what feels best or what everyone else is doing.