import re
Regex_Pattern = r'^[a-zA-Z]*s$'

def input():
    return "Kites"

print(str(bool(re.search(Regex_Pattern, input()))).lower())