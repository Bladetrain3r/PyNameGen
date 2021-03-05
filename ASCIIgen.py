import random
from os import path
import getopt, sys

opts, args = getopt.getopt(sys.argv[1:], "ynp:", "--prefix")
hasprefix = ""
customprefix = ""
optlist = {"-y": "yes", "-n": "no", "-p": "custom"}

for o, a in opts:
    if o == "-y":
        hasprefix = "yes"
    elif o == "-n":
        hasprefix = "no"
    elif o in ("-p", "--prefix"):
        hasprefix = "custom"
        customprefix = a
    else:
        assert False, "Unhandled Option"


if hasprefix == "":
    checkprefix = input("Random Prefix? Y/N ").lower()
    hasprefix = optlist["-" + checkprefix]
    if hasprefix == "no":
        confirmcustom = str(input("Custom Name? Y/N ")).lower()
        if confirmcustom == "y":
            customprefix = input("Prefix? ").upper()

# Randomly Generate a Name
randomwords = []

if path.exists("words.txt"):    
    while len(randomwords) <= 5:
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
        prefix.append(random.choice(alphabet.split()))
    return str("%s %s" % ("".join(prefix).upper(), shipname))

def namegen(namelength, wordlist):
    namelist = []
    if len(wordlist) > 1:
        while len(namelist) < namelength:
            namelist.append(random.choice(wordlist))
        return " ".join(namelist)
    else:
        return wordlist[0]

#Change number of words in the name and number of letters in the prefix here.
finalname = namegen(2, randomwords)
if hasprefix == "yes":
    print(prefixgen(3, finalname))
elif hasprefix == "custom":
    print("%s %s" % (customprefix, finalname))
else:
    print(finalname)



