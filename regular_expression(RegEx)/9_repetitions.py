import re

Regex_Pattern = r"^[a-zA-Z02468]{40}[13579\s]{5}$"

def input():
    return "2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57"

print(str(bool(re.search(Regex_Pattern, input()))).lower())