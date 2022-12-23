import re
name = input("What's your name? ").strip()

# doing it using if condition, but barely exhaustive
if "," in name:
    last, first = name.split(", ")
    name =  f"{first} {last}"
print(f"hello, {name}")

# Create groups using paraenthesis
# :=, walrus operator, assign and ask a boolean question
if matches := re.search(r"^(.+), (.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

### Extract username from twitter URL ###
# string method: replace, removeprefix
# re.sub(pattern, repl, string, count=0, flags=0)
# regex groups can be nested, take baby incremental steps testing regex
url = input("URL: ")
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")

# using re.search instead of re.sub
if match := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9]+)", url, re.IGNORECASE):
# match is has string, which is truthy
# each () is one group, unless (?:...), then print(matches.group(1))
# re.split, re.findall
    print(f"Username:", matches.group(2))