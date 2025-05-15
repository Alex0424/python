import re

Regex_Pattern = r"^[a-z][1-9][^a-z][^A-Z][A-Z]"

def input():
    return "h4CkR"

print(str(bool(re.search(Regex_Pattern, input()))).lower())