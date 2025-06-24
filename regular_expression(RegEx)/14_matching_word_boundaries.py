import re
Regex_Pattern = r'\b[aeiouAEIOU]+[a-zA-Z]*\b'

def input():
    return "Found any match?"

print(str(bool(re.search(Regex_Pattern, input()))).lower())