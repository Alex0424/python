import re
Regex_Pattern = r"^\d+[A-Z]+[a-z]+$"

def input():
    return "999987AJSHDHDHdufh"

print(str(bool(re.search(Regex_Pattern, input()))).lower())
