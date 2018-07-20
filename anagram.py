import string
import ast

def buildHashTable(handle, hashtable):
    values = dict()
    for index, letter in enumerate(string.ascii_lowercase):
        values[letter] = index + 1
    for line in handle:
        hashval = 0
        for char in line.strip().lower():
            hashval+=values[char]
        key = str(hashval)
        if key in hashtable:
            hashtable[key].append(line.strip())
        else:
            hashtable[key] = [line.strip()]

def hashKey(strDut):
    values = dict()
    for index, letter in enumerate(string.ascii_lowercase):
        values[letter] = index + 1
    hashval = 0
    for char in strDut.lower():
        hashval += values[char]
    return str(hashval)

def permutate(stringData):
    listdata = list(stringData)
    found = False
    global anastack
    global anagram
    for i, char in enumerate(listdata):
        if len(listdata) == 1:
            anagram = ''.join(anastack) + char
            anagrams.append(anagram)
        else:
            templist = list(listdata)
            del templist[i]
            anastack.append(char)
            result = permutate(''.join(templist))
        if i == (len(listdata) - 1):
            if (len(anastack) != 0):
                anastack.pop()

#fDict = open("9dict.txt", "r")

hashtable = dict()
#buildHashTable(fDict, hashtable)

fHashTable = open("9dictHashTable.txt", "r")
hashtable = ast.literal_eval(fHashTable.read())
fHashTable.close()

anagrams = []
anagram = ""
anastack = []

DUT = "YCEIXTANL"

dutHash = hashKey(DUT)
listValues = hashtable[dutHash]

#permutate(DUT)

foundGram = []

# for anagram in anagrams:
#     if anagram.lower() in listValues:
#         if anagram not in foundGram:
#             foundGram.append(anagram)

for listValue in listValues:
    if sorted(listValue.lower()) == sorted(DUT.lower()):
        foundGram.append(listValue.upper())

for found in foundGram:
    print found

#fDict.close()
