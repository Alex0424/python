import re

Regex_Pattern = r"^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^.,]$"

def input():
    return "think?"

print(str(bool(re.search(Regex_Pattern, input()))).lower())