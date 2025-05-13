# Needs to start with a digit, followed by 4 alphanumeric characters, and end with a dot
import re

Regex_Pattern = r"^\d\w\w\w\w.$"

def input():
    return "0qwer."

print(str(bool(re.search(Regex_Pattern, input()))).lower())