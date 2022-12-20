import sys
import random
from pyfiglet import Figlet
figlet = Figlet()


if len(sys.argv) > 2:
    if (sys.argv[1] == '-f' or sys.argv[1] == '--font') & (sys.argv[2] in figlet.getFonts()):
        pass
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

str_display = input("Input: ")
if len(sys.argv) == 1:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)
    print(figlet.renderText(str_display))
else:
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(str_display))



