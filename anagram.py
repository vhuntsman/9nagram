import ast

# ==============================================
#   Building Hash Table for fast look-up
# ==============================================
def buildHashTable(handle, hashtable, primedict):
    for line in handle:
        hashval = 1
        for char in line.strip().lower():
            hashval *= primedict.get(char)
        key = str(hashval)
        if key in hashtable:
            hashtable[key].append(line.strip())
        else:
            hashtable[key] = [line.strip()]
# ==============================================
#   Hash word into a single integer
# ==============================================
def hashKey(strDut, primedict):
    hashval = 1
    for char in strDut.lower():
        hashval *= primedict.get(char)
    return str(hashval)
# ----------------------------------------------
#   Main Program Starts
# ----------------------------------------------
# Load LetterPrimeMap
fPrimeMap = open("LetterPrimeMap.txt","r")
primeMap = ast.literal_eval(fPrimeMap.read())
fPrimeMap.close()
# Open dict containing all 9-letter words
fDict = open("9dict.txt", "r")
# Build hash table
hashtable = dict()
buildHashTable(fDict, hashtable, primeMap)
fDict.close()
# Get user input string
testString = raw_input("Enter 9-word anagram: ")
if testString.isalpha():
    testString = testString[:9] # Limit length to 9
    # Hash input string and find matching values in hash table
    dutHash = hashKey(testString, primeMap)
    listValues = hashtable.get(dutHash)
    # Print result
    print (listValues)
else:
    print ("Input is not a valid. Restart program to try again.")