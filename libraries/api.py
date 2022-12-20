# APIs, download data, interact data with a service
# As if my code is an internet browser itself
# requests package, itunes example from apple
import requests
import sys
import json

limit = 50

if len(sys.argv) != 2:
    # breaks out of entire program, not loops
    sys.exit()

# allow user to specify term keyword
response = requests.get(f"https://itunes.apple.com/search?entity=song&limit={limit}&term=" + sys.argv[1])

# json.dump, makes json more readable
o = response.json()
for result in o["results"]:
    print(result["trackName"])

# if file is being imported as a module, do NOT run main
# __name__ is a special variabe in python, which sets the program name to __main__
# when file is imported, __name__ will not be called
if __name__ == "__main__":
    main()

# Notes
"""
- JSON, language agnostic format for exchanging data
- API: a mechanism to interact with a server and integrate the results into my own program
- when my files are imported as modules/packages, functions are also being run
-
"""