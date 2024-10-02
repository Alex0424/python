# Episode 3: English, you can it or?

Commander Lambda wanted to know which one of his minions that had the best knowledge of the english language and who had the best communication skills. He collected all chatt logs from his minions in his lair and have asked you to make a script that do some basic analysis on the text files he have collected. We don't really know why Commander Lambda wants this information, but i am sure he has his reasons... As a minion we do not ask questions


Mission Briefing:

To verify each text file so that Lambda can decide who needs to work on their writing skills, you need to write a program for him that will read the entire contents of each file & calculate a few different metrics.

Write a function `def solution(filename)` that will open the given filename, read all the content from this file and start to process all content and figure out the following things below

1. What is the shortest word used in the text? If there is more then 1 different word with the same lenght, print all of them
2. Count each occurence of each different letter, number, symbol in the entire text file and print them out. Lower case and upper case letters count as different letters. Print each letter/symbol on a new line with the counter saying how many times. Important here that you sort everything in alphabeitcal order.
3. The longest word used in the text. If there is multiple words with the same lenght, then print all of them
4. How many words and how many lines the submission was. Remember that blank lines counts as one line and should not be skipped/ignored

These things should be printed out to stdout in a nice, clean & readable fashion. Remember the zen of python, readability counts

Also, all of this data should also be put into a dict object and returned from your function so commander Lambda can look at the data himself. You are free to design your return data and your prints however you like, as long as commander Lambda can easily understand the output and the data he will be recieving back. The example solutions below is just examples and not the required format for the prints you need to make

IMPORTANT The verification.py script is intentionally broken due to this. You need to update that script once you have decided how your returned data structure will look like. Sometimes code you work with and recieve is broken and you need to be able to fix misstakes that other people have done


## Solution

To provide a Python solution, edit solution.py so that your code works with the following test scenarios

NOTE: When calling your function it should return a well formated output within the function call that prints all relevant data to the terminal. It is not acceptible to just print the data dict. This below is just an example and not the full expected output. You need to fill in the blanks it should be dynamic enough to work on any input data.



Input:
    solution.solution("minion-1.txt")
Text output:
    Shortest word: ...

    a: 1
    b: 5
    c: 18
    ...
    z: 0
    A: 7
    ...
    !: 9
    -: 5
    .: 3
    
    Longest word: Pneumonoultramicroscopicsilicovolcanoconiosis

    Number of words: 3781

    Number of lines: 25
Returns:
    The function should return a dict objeect with all relevant data in it

    {...}

Input:
    solution.solution("minion-2.txt)
Text output:
    Shortest word: ...

    a: 1
    b: 5
    c: 18
    ...
    z: 0
    A: 7
    ...
    !: 9
    -: 5
    .: 3
    
    Longest word: Pneumonoultramicroscopicsilicovolcanoconiosis

    Number of words: 1753

    Number of lines: 19
Returns:
    The function should return a dict objeect with all relevant data in it

    {...}


Input:
    solution.solution("minion-3.txt)
Text output:
    Shortest word: ...

    a: 4
    b: 8
    c: 13
    ...
    z: 1
    A: 5
    ...
    !: 2
    -: 4
    .: 8
    
    Longest word: Pneumonoultramicroscopicsilicovolcanoconiosis

    Number of words: 2938

    Number of lines: 18
Returns:
    The function should return a dict objeect with all relevant data in it

    {...}


## Task

To provide a Python solution, edit the file solution.py until your code passes the test case:s below, the assignment above and the additional constraints below.


## Verification script

To test your code you can run the helper verification script by running

```python
python3 verification.py
```

If this script do not throw an error, the script succeeds and the test cases within it works.


## Hints and help

Designing a good data structure is difficult. Focus on figure out this part first. How you want to represent the return data in as simple form as possible. Only process 

Blank lines in the file counts as a line in the calculation for how many lines a file contains

You must update and fix the intentionally broken solution.py and verification.py scripts so that the code in those files can both be run. If the verification.py script do not work, this assignment will not pass

You can parse the text files in many different ways to extract out the information. It won't be graded on, but always try to make the parsing as efficient as possible and try to avoid unnessesary steps and repetitions. For instance if you can parse out required metrics you need by only doing one pass of the entire input data, that is better then to read up, parse of everything many different times for each data you want to parse out

It is important that you write the solution to the best of your skill and how you think using python to solve this problem


## Constraints and additional requirements

You MUST create one additional test .txt file and include it in the submission of the solution. Name it `minion-4.txt`. You decide the contents yourself. The verification.py file must use this file.

You can create as many new test files as you like. But you must provide the minion-1.txt, minion-2.txt & minion-3.txt files as you recived them unmodified.

You must update the docstring for the function "def solution(...)" with a short description of how your solution works

You code must contain a few lines of relevant and informative code-comments

The code in the solution function you write consist of more then 25 lines of code

 - The code you are provided with IS NOT included in these 25 lines of code
 - Code comments IS NOT included in these 25 lines of code
 - The updated docstring IS NOT included to these 25 lines of code

There should be no upper limit to how large a textfile can be. But additional test files will not be bigger then 100.000 characters of text
