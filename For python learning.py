import GameStats
import re
#ToDo: make an email extraction code

verdict="madness" if 2+2!=4 else "reality"
for i in range(9):
    print(i)
else:
    print("unbroken")
for k in range(5):
    try:
        k/9
    except ZeroDivisionError:
        print(k)
    else:
        print("no mistakes")
print(verdict)
btry=r"\b(cat)\b"
match = re.search(btry, "The!cat!sat!")
if match:
    print ("Match sequence")
sequence=r"(double )\1(trouble)"
matchseq = re.match(sequence,"double double trouble")
if matchseq:
    print(matchseq.group())
groups=r"(?P<first>first )(?:second )(third )(forth (GuessWhat ))(six(th|z) )"
match=re.match(groups,"first second third forth GuessWhat sixz ")
if match:
    print(match.group(5))
    print("string's length: {} groups".format(len(match.groups())))
lotsO_repetitions="this (repeats )*a lot"
if re.match(lotsO_repetitions,"this repeats repeats repeats repeats a lot"):
    print("repeats")
string=r"^this must be \r\a\w$"
stringClass=r"[hi]"
pattern=r"thisIs............pattern"
if re.match(pattern,"thisIs an amazing pattern"):
    print("got it")
if re.search(stringClass,"thisIsSpartabitch pattern"):
    print("got it 2")
unipattern=r"[A-Za-z][A-Za-z]"
if re.match(unipattern,input("Ok/No/own-two-letters\n")):
    print("gotcha 3")
dontShout=r"[^a-z]"
if re.search(dontShout,input("quiet,pls\n")):
    print("I SAID QUIET!!!!")
print(re.sub("pattern","python",pattern))
print(string)
mail = input("Please, enter your e-mail \n")
mailPattern=r"([\w]+)(@mail.)([\w]+)"
iterator=re.match(mail,mailPattern)
while not iterator:
    print("Incorrect e-mail form")
    mail = input("Please, reenter your e-mail \n")
    if iterator:
        print("trying to break")
        break
print("Thanks for submitting")
# * = 0 or more repetitions
# + = 1 or more repetitions
# ? = 1 or less repetitions
# {x,y} or {,} = from x to y or from 0 to infinite repetitions
#\d, \s, and \w match digits, whitespace, and word characters respectively.
#\A, \Z, and \b match the beginning,the empty string between \w and \W characters or \w characters and the beginning or end of the string.
# and end of a string, respectively.
