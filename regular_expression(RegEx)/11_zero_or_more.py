import re

Regex_Pattern = r"^\d{2}\d*[a-z]*[A-Z]*$" # * will match the character 0 or more times

def input():
    return "14qwertyuiASDFGHJ"

print(str(bool(re.search(Regex_Pattern, input()))).lower())