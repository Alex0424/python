# \d = digit
# \D = non-digit
import re

Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d" # Match 3 digits

def input():
    return "06-11-2025"

print(str(bool(re.search(Regex_Pattern, input()))).lower())