# Episode 1: I Love Lance & Janice

You've caught two of your fellow minions passing coded notes back and forth -- while they're on duty, no less! Worse, you're pretty sure it's not job-related -- they're both huge fans of the space soap opera ""Lance & Janice"". You know how much Commander Lambda hates waste, so if you can prove that these minions are wasting time passing non-job-related notes, it'll put you that much closer to a promotion. 


Mission Briefing:

Fortunately for you, the minions aren't exactly advanced cryptographers. In their code, every lowercase letter [a..z] is replaced with the corresponding one in [z..a], while every other character (including uppercase letters and punctuation) is left untouched.  That is, 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.  For instance, the word "vmxibkgrlm, when decoded, would become "encryption.

In the provided file named solution.py, there is a defined function called "def solution(s)". This function do not work and it is within this function you should write your own code. The function is expected to return the deciphered string object back to the function caller. You need to fullfill these things in order to show commander lambda proof that these minions are talking about "Lance & Janice" instead of doing their jobs.


## Task

To provide a Python solution, edit the file solution.py until your code passes the test case:s below, the assignment above and the additional constraints below.


## Test cases

Your code MUST pass the following test cases, but you are encouraged to expand the tests to ensure you cover all possible scenarios.

Code input: 
    solution.solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
Returns:
    "did you see last night's episode?"

Code input:
    solution.solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
Returns:
    "Yeah! I can't believe Lance lost his job at the colony!!""


## Verification script

To test your code you can run the helper verification script by running

```python
python3 verification.py
```

If this script do not throw an error, the script succeeds and the test cases within it works.


## Hints and help

If you import the python standard library module "string" you can find the entire alphabet in that module as a variable on that module. Look up the string module on python.org to find more details, or reference the slides for the examples given there.

It is important that you write the solution to the best of your skill and how you think using python to solve this problem

In order to ensure that your code works in all case:s, you should probably add a few more test cases to further increase your confidence that your solution works

It is important here to be exact about all small details and corner-cases. There is a couple of traps that is easily stumbled upon in this assignment. Read the assignment carefully and write down what is required and not.

Break down the problem to smaller steps and solve one problem at a time



## Constraints and additional requirements

You must update the docstring for the function "def solution(input_string)" with a short description of how your solution works. Good code is well documented.

You code must contain a few lines of relevant and informative code-comments, this is not the same as the docstring. Code comments should be informative and comments that just repeat what the next line of code does will not be accepted as a solution. It should provide additional value

The code in the solution function you write, MUST consist of more then 10 lines of code.

 - The code you are provided with from the teacher IS NOT included in these 10 lines of code
 - Code comments IS NOT included in these 10 lines of code
 - The updated docstring IS NOT included to these 10 lines of code

List/dict comprehensions IS NOT allowed to be part of this solution

Keep the solution simple and straight forward to read and understand. This assignment should not be optimized to be as small as possible
