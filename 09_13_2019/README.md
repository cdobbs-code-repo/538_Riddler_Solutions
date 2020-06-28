# Riddler-9-13-19

This is the Python code I used to solve the Riddler Classic on FiveThirtyEight.com for 9/13/19 (https://fivethirtyeight.com/features/can-you-help-dakota-jones-raid-the-lost-arc/). The problem was finding the longest string of letters composed of U.S. state and territory abbreviations without repeats. So 'WACA' doesn't work because 'AC' is not an allowed abbreviation, 'LARILA' doesn't work because 'LA' is repeated, and 'WALARID' does work because each two letters pairs that touch ('WA', 'AL', 'LA', 'AR', ...) are U.S. state and territory abbreviations without repeats.

Ultimately, the longest possible strings were 29 characters long. There were 31,200 possible solutions.

To solve this problem in script.py, I iterated through all of the possibilities with a recursive function keeping track of the depth (which equalled the string length) by updating a global max variable. To keep things simple, I basically ran the program twice- once to get the maximum string length, again to print out all strings that were of that length.

I have included a few additional files in this repository. output.txt is all of the 29 character strings without spaces or newlines. I absent-mindedly printed the output this way, but since script.py took over an hour to run on my computer, I just kept the output file and wrote another script called newout.py that inserted the appropriate newline characters in a file similarly titled newout.txt. Finally, I added a get_freq.py script that sifts through newout.txt to bin prefix or suffix frequencies (current edit only bins suffixes, but Find->Replace->"[-3:]" to "[0:4]" and this quickly bins prefixes). 

Using get_freq.py, I found some interesting patterns. For instance, 100% of the solutions start with the letter 'M' and end in 'L' or 'D', 38.46% of the solutions start with the letters 'MPWV', and 48% of the solutions have a second to last letter of 'I'.
