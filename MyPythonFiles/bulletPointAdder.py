#! /user/bin/env python3

"""
Problem:
When editing a Wikipedia article,
you can create a bulleted list by putting each list item on its own line
and placing a star in front. But say you have a really large list
that you want to add bullet points to. You could just type those stars
at the beginning of each line, one by one.
Or you could automate this task with a short Python script.
---------------------------------------------------------------
Solution:
The bulletPointAdder.py script will get the text from the clipboard,
add a star and space to the beginning of each line,
and then paste this new text to the clipboard.
---------------------------------------------------------------
Example:
For example, if I copied the following text
(for the Wikipedia article “List of Lists of Lists”) to the clipboard:

Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
and then ran the bulletPointAdder.py program,
the clipboard would then contain the following:

* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation
* Lists of cultivars
This star-prefixed text is ready to be pasted into
a Wikipedia article as a bulleted list.
----------------------------------------------------
User Experience:
1. Copy a text that includes a list without bullet point
2. Paste it and the text has bullet point
--------------------------------------------------------
Computer instruction:
1. paste text from the clipboard
2. Do something to it (adds bullet points to the list)
3. Copy the new text to the clipboard
--------------------------------------------------------
Python instructions:
1. paste text from the clipboard : {pyperclip library; pyperclip.paste()}
2. Seperate lines and add stars: {text.split('\n'); for loop through all indenxess of the list}
3. Join the modified lines: {'\n'.join(lines)}
4. Copy the new text to the clipboard: {pyperclip library; pyperclip.copy()}
"""
#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each
# line of text on the clipboard

import pyperclip
text = pyperclip.paste() #paste text from the clipboard and store it text
"""
Note: The call to pyperclip.paste() returns all the text on
the clipboard as one big string. If we used the “List of Lists of Lists” example,
the string stored in text would look like this:

'Lists of animals\nLists of aquarium life\nLists of biologists by author
abbreviation\nLists of cultivars'

Question: How to add start to the start of each line in the list?

The \n newline characters in the above string cause it to be displayed
with multiple lines when it is printed or pasted from the clipboard.
There are many “lines” in this one string value. You want to add a star
to the start of each of these lines.

You could write code that searches for each \n newline character
in the string and then adds the star just after that. But it would
be easier to use the split() method to return a list of strings,
one for each line in the original string,
and then add the star to the front of each string in the list.
"""


# TODOD: Seperate lines and add starts.
# Seperate lines and add stars.
lines = text.split('\n') # use split method to return a list of strings, one for each line
for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # adds star to each string in "lines" list
text = '\n'.join(lines)

pyperclip.copy(text) #copy the revised text to clipboard


