import re

Regex_Pattern = r"^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^.,]$"  # '^' inside the '[]' will exclude that letter

def input():
    return "think?"

print(str(bool(re.search(Regex_Pattern, input()))).lower())