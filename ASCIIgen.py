import random
from os import path
import getopt, sys

opts, args = getopt.getopt(sys.argv[1:], "y")
hasprefix = "n"

for o, a in opts:
    if o == "-y":
        hasprefix = "y"

if hasprefix != "y":
    hasprefix = input("Prefix? Y/N").lower()

# Randomly Generate a Name

randomwords = []

if path.exists("words.txt"):    
    while len(randomwords) <= 200:
        pickword = random.choice(open("words.txt").readlines())
        # print(pickword)
        randomwords.append(pickword.strip('\n'))
else:
    randomwords.append(str(input("Custom Name? ")))

def prefixgen(prefixlength, basename):
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    shipname = str(basename)
    preflength = abs(int(prefixlength))

    prefix = []
    for item in range(preflength):
        prefix.append(alphabet.split()[random.randrange(0, 25)])
    return str("%s %s" % ("".join(prefix).upper(), shipname))

def namegen(namelength, wordlist):
    namelist = []
    if len(wordlist) > 1:
        while len(namelist) < namelength:
            namelist.append(wordlist[random.randrange(0, len(wordlist))])
        return " ".join(namelist)
    else:
        return wordlist[0]

#Change number of words in the name and number of letters in the prefix here.
finalname = namegen(2, randomwords)
if hasprefix == "y":
    print(prefixgen(3, finalname))
else:
    print(finalname)



