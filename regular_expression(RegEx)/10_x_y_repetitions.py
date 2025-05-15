import re

Regex_Pattern = r"^\d{1,2}[a-zA-Z]{3,}[.]{0,3}$"

def input():
    return "3threeormorealphabets..."

print(str(bool(re.search(Regex_Pattern, input()))).lower())