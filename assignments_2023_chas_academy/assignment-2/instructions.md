# Episode 2: Evil lair elevator maintenance

You've been assigned the onerous task of elevator maintenance -- ugh! It wouldn't be so bad, except that all the elevator documentation has been lying in a disorganized pile at the bottom of a filing cabinet for years, and you don't even know what elevator version numbers you'll be working on. 


Mission Briefing:

Elevator versions are represented by a series of numbers, divided up into major, minor and revision integers. New versions of an elevator increase the major number, e.g. 1, 2, 3, and so on. When new features are added to an elevator without being a complete new version, a second number named "minor" can be used to represent those new additions, e.g. 1.0, 1.1, 1.2, etc. Small fixes or maintenance work can be represented by a third number named "revision", e.g. 1.1.1, 1.1.2, 1.2.0, and so on. The number zero can be used as a major for pre-release versions of elevators, e.g. 0.1, 0.5, 0.9.2, etc (Commander Lambda is careful to always beta test her new technology, with her loyal henchmen as subjects!).

Given a list of elevator versions represented as strings, write a function solution(l) that returns the same list sorted in ascending order by major, minor, and revision number so that you can identify the current elevator version. The versions in list l will always contain major numbers, but minor and revision numbers are optional. If the version contains a revision number, then it will also have a minor number.

For example, given the list l as ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"], the function solution(input_list) would return the list ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]. If two or more versions are equivalent but one version contains more numbers than the others, then these versions must be sorted ascending based on how many numbers they have, e.g ["1", "1.0", "1.0.0"]. The number of elements in the list l will be at least 1 and will not exceed 100.

Commander Lambda also DEMANDS that you add comments to your code describing some of the steps you make where it is not obvious what you intend the code to do.


## Task

To provide a Python solution, edit the file solution.py until your code passes the test case:s below, the assignment above and the additional constraints below.


## Test cases

Your code MUST pass at least the following two test cases.

It is recommended that you add your own test cases to verification.py script to further ensure your algorithm works as expected based on the text above

Input:
    solution.solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
Returns:
    FEL ["0.1, 1.1.1, 1.2, 1.2.1, 1.11, 2, 2.0, 2.0.0"]
    RÄTT ["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"]

Input:
    solution.solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
Returns:
    FEL ["1.0, 1.0.2, 1.0.12, 1.1.2, 1.3.3"]
    RÄTT ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]
    

## Verification script

To test your code you can run the helper verification script by running

```python
python3 verification.py
```

If this script do not throw an error, the script succeeds and the test cases within it works.


## Hints and help

This problem consists of several hidden and easily stumbled upon traps and corner-cases. It is important then to implement you'r own test cases to ensure and validate that you'r code works according to this specification and this problem set.

It is important that you write the solution to the best of your skill and how you think using python to solve this problem


## Constraints and additional requirements

You are not allowed to use a pre-built module from the python standard library or externally writen by someone else to perform the comparison part of this problem. You must code and provide your own solution for this problem.

Validating your data input is important. If one value in the input_list is not a string, your code should throw a ValueError exception.

You must update the docstring for the function "def solution(...)" with a short description of how your solution works

You code must contain a few lines of relevant and informative code-comments

The code in the solution function you write consist of more then 15 lines of code

 - The code you are provided with IS NOT included in these 15 lines of code
 - Code comments IS NOT included in these 15 lines of code
 - The updated docstring IS NOT included to these 15 lines of code

Your function will be timetested against 100 elements. If it takes far to long to execute that input, the code might not pass

The input will never be more then 3 elements "x.y.z" but if your code works in a generic fashion with any number of elements in each string value, that is just a plus and NOT REQUIRED to implement. Your solution MUST work with 1 to 3 items.
