# \s = whitespace
# \S = non whitespace
import re

Regex_Pattern = r"\S\S\s\S\S\s\S\S"

def input():
    return "ab 34 ef"

print(str(bool(re.search(Regex_Pattern, input()))).lower())