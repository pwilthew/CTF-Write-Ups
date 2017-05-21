# CSAW 2016 Quals
# Regexpire
##### Patricia Wilthew -- USF Whitehatter's Computer Security Club
##### misc -- 100 points
## Description

I thought I found a perfect match but she ended up being my regEx girlfriend.

Note: You can't use newlines inside your match.

`nc misc.chal.csaw.io 8001`

## Solution
The server prints
~~~
Can you match these regexes?
5lfb*(clementine|chair)+[1-9]{8}[eHf]*eK{2}K{2}
~~~
And it gives us some seconds to create a phrase that belongs to that regular expression *

* Read about regular expressions -> https://msdn.microsoft.com/en-us/library/ae5bf541(v=vs.100).aspx
A possible phrase (or matching phrase) that belongs to that regular expression would be: 5lfbbbclementinechairclementine11111111eHfeKKKK

The problem is that it gives us 10 seconds to come up with a phrase, and as soon as we enter it (which is nearly impossible as we have only 10 seconds), it's gonna ask us to match another regular expression... 
Therefore, we have to write a code that given a regular expression, would generate any phrase that matches it.
I did some research and found a pip library called 'rstr' that has a method called 'xeger' that would do what we need it to do.

~~~python
code
~~~
The program will run for a while, then it will print the flag
~~~
code output
~~~
