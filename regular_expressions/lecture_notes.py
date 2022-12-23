import re
# Examples w/o regular expressions, showing limitation
# stripping whitespaces
email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("valid")
else:
    print("Invalid")

# split return list output
username, domain = email.split("@")

# string is truthy value
if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

#### USING REGEX #####
# use r"" to read backslash as escape, raw string
# exact match, with ^ "regex" $
# [^] is complement, everything EXCEPT the character in the brackets
# [a-z]: hyphen "-" means range, can have mulitple range
# (edu|gov|gmail|), (\w|\s) or statements ccombining regex
# use additional argument to ignore case
# can group together and repetition in group
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# Notes
"""
- regex searches for pattern in our code
- symbols/vocabularies for repetition in regex: 
    - . any character except a newline
    - * 0 or more reptitions
    - + 1 or more repitions
    - ? 0 or 1 reptition
    - {m} m repetitions
    - {m,n} m-n repitions
    - ^ matches the start of the string
    - $ matches the end of the string or just before the newline at the end of the string
    - [] set of characters
    - [^] complementing the set
    - \w alphanumeric, word character
    - \d decimal digit
    - \D not a decimal digit
    - \s whitespace character
    - \S not a white space character
    - \W not a word character
    - A|B either A or B
    - (...) a group
    - (?:...) non-capturing version
    - re.IGNORECASE, re.MULTILINE, re.DOTALL additional arugment to re.search
- good habit to use raw string for all regular expression
- Built in shortcuts for common expression: [a-zA-Z0-9_] == "\w' (include underscore!)
- packages that include pre defined regular expression
"""