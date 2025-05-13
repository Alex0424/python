# \w matches any alphanumeric character (equivalent to [a-zA-Z0-9_] + unicode(é, ç, Д, 你)
# \W matches any non-alphanumeric character (not equivalent to [^a-zA-Z0-9_] + unicode(é, ç, Д, 你)
import re

Regex_Pattern = r"\w\w\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w" # Match 3 words 

def input():
    return "_www.hackerrank.com"

print(str(bool(re.search(Regex_Pattern, input()))).lower())