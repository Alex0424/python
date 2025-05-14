# Checks if the input string matches a specific 6-character pattern using regular expressions.
import re

Regex_Pattern = r"[123][120][xs0][30Aa][xsu][.,]"

def input():
    return "1203x."

print(str(bool(re.search(Regex_Pattern, input()))).lower())