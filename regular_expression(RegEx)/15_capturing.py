import re
Regex_Pattern = r'(ok){3}(ok)*'

def input():
    return "okokok! cya"

print(str(bool(re.search(Regex_Pattern, input()))).lower())