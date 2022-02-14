# TEXT ENCRIPTION SERVER by Precious Nwaoha
# Open Source Code Python library managed by IT Students ROAR NIGERIA HUB

#About: This runs a server that has different commands which you can use to encript and decript texts anonymously

import random # get the random module for python
import re # get the regex module for python

global storage # create a global storage variable for commands and encriptions storage
storage = {
    "commandList": {
        "enc": {
            "description": "encripts a Text",
            "syntax": ["enc", "enc()", "enc(\"[Your-Text]\")", "enc(\"[Your-Text]\", [No Of Encriptions])"],
            "alts": ["ENC", "encript", "Encript", "ENCRIPT"]
        },
        "dec": {
            "description": "decripts encripted Text",
            "syntax": ["dec", "dec()", "dec(\"[Encription ID]\")", "dec([Encription ID])"],
            "alts": ["DEC", "decript", "Decript", "DECRIPT" ]
        },
        "exit": {
            "description": "exit server",
            "syntax": ["exit", "exit()"],
            "alts": ["x", "X", "Exit", "EXIT"]
        },
        "help": {
            "description": "see how to use",
            "syntax": ["help", "help()"],
            "alts": ["h", "H", "HELP", "?"]
        },
        "del": {
            "description": "deletes an encrption",
            "syntax": ["del", "del()", "del([Encription ID])"],
            "alts": ["delele", "DEL", "DELETE"]
        },
        "get": {
            "description": "gets encripted Text from ID",
            "syntax": ["get", "get()", "get([Encription ID])"],
            "alts": ["GET", "g", "G"]
        },
        "cmdl": {
            "description": "show Command List",
            "syntax": ["cmdl", "cmdl()"],
            "alts": ["CMDL", "CommandList"],
        },
    },
    "algos": ["rotShift", "reverseStr", "strToNum", "mapLetter"], #list of algorithms used in encription
    "idData": {}, # where each encription ID will be stored
    "encripted": {} # where each encription outputs will be stored ---showencriptedandstore()---
}


def showencriptedandstore(id, encriptedstr): #shows the encription id and encripted text and stores in storage["encripted"]
    tempresult = """\n\tEncription ID: {}\n\tEncripted String: "{}"\n(---COPY your Encription ID and keep it SAVE---)\n"""
    result = tempresult.format(id, encriptedstr)
    storage["encripted"][id] = result
    print(result)

def showcommandlist(): # shows available commands in the server from ---storage["commandList"]
    print("\tCOMMAND LIST:")
    for key in storage["commandList"]:
        tempStr = "\t\t \"{}\": ({})\n\t\t\t\tSyntax: {}\n\t\t\t\talternatives: {}\n"
        print(tempStr.format(key, storage["commandList"][key]["description"], storage["commandList"][key]["syntax"], storage["commandList"][key]["alts"]))

# id functions
def addId(name, encriptionAlgoData): # adds an encrition ID to and encription data to ---storage["idData"]---
    if name in storage["idData"]: # if the encription type already exits in storage
        lastIdNo = storage["idData"][name]["noOfIds"] + 1
        idText = name + "% s" % lastIdNo
        storage["idData"][name]["ids"][idText] = {}
        storage["idData"][name]["ids"][idText]["encriptionAlgoData"] = encriptionAlgoData
        storage["idData"][name]["noOfIds"] = lastIdNo
    else: # if the encription type does not exist in storage
        storage["idData"][name] = {"ids": {}, "noOfIds": 0}
        idText = name + "1"
        storage["idData"][name]["ids"][idText] = {}
        storage["idData"][name]["ids"][idText]["encriptionAlgoData"] = encriptionAlgoData
        storage["idData"][name]["noOfIds"] = 1
    return idText

def checkID(id): # checks if an encription with the id provided exists in storage
    name = re.sub("\d+", "", id)
    if name in storage["idData"]: # if encription type exists
        idslocation = storage["idData"][name]["ids"]
        if id in idslocation: # if encription ID exists
            return True
        else: # if it does'nt exists
            return  False
    else: # if the encription type does'nt exist
        return False

def deleteID(id): # deletes an encription id from storage
    deleted = False
    name = re.sub("\d+", "", id)
    idsinname = storage["idData"][name]["ids"]
    if id in idsinname: # if the id exists
        outputtext = "\t{} deleted"
        del idsinname[id] # delete id
        del storage["encripted"][id]
        print(outputtext.format(id))
        return
    print("\tNo such ID found") # else print "no such id found"

def getID(id): #  get encripted text from id
    if checkID(id): # if encription with ID exists in storage
        print(storage["encripted"][id])
    else: # if encription does'nt exist in storage
        print("\n\tError: Encription ID does not exist")


# ENCRIPTION ALGORITHMS
# 1. rotShift shifts letters of the alphabet by some specified step value
def rotShift(str, step=0, fromEncript=False):
    if step == 0: # if step is the default value
        step = random.randint(1, 25) # change step to a random value from 1 to 25
    alphabetsSmall = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
    alphabetsCaps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"," Y", "Z" ]
    newStr = "" # define new text as nothing
    for x in str: # go through each letter in the provided text
        if x in alphabetsSmall: # if x is a letter and a small letter
            idx = alphabetsSmall.index(x) # get location of letter in ---alphabetsSmall---
            if (idx + step) > 25: # if the ---location + step--- falls beyond 26 (0 to 25)
                val = idx + step - 26
                newStr = newStr + alphabetsSmall[val]
            elif (idx + step) < 0: # if step is negative and ---location - step--- is less than 0
                val = idx + step + 26
                newStr = newStr + alphabetsSmall[val]
            else: # if ---location + step--- is between 0 to 25 inclusive
                newStr = newStr + alphabetsSmall[idx + step]
        elif x in alphabetsCaps: # if x is a letter and a CAPITAL letter
            idx = alphabetsCaps.index(x)
            if (idx + step) > 25: # if the ---location + step--- falls beyond 26 (0 to 25)
                val = idx + step - 26
                newStr = newStr + alphabetsCaps[val]
            elif (idx + step) < 0: # if step is negative and ---location - step--- is less than 0
                val = idx + step + 26
                newStr = newStr + alphabetsSmall[val]
            else: # if ---location + step--- is between 0 to 25 inclusive
                newStr = newStr + alphabetsCaps[idx + step]
        else: # if x is not a letter
            newStr = newStr + x
    if fromEncript == False: # if this function was not called from the encript() function
        stringID = addId("rotShift", {"algoName": "rotShift", "decriptData": [newStr, step]}) # add and Encription ID and store the data
        showencriptedandstore(stringID, newStr) # print the encritption id and mark as encripted
    return newStr

def decriptRotShift(str, step): # This just reverses the rotShift() fucntion
    alphabetsSmall = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "w", "x", "y", "z"]
    alphabetsCaps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                     "U", "V", "W", "X", " Y", "Z"]
    realStr = ""
    for x in str:
        if x in alphabetsSmall:
            idx = alphabetsSmall.index(x)
            if (idx - step) < 0:
                val = idx - step + 26
                realStr = realStr + alphabetsSmall[val]
            elif (idx - step) > 25:
                val = idx - step - 26
                realStr = realStr + alphabetsSmall[val]
            else:
                realStr = realStr + alphabetsSmall[idx - step]
        elif x in alphabetsCaps:
            idx = alphabetsCaps.index(x)
            if (idx - step) < 0:
                val = idx + step - 26
                realStr = realStr + alphabetsCaps[val]
            elif (idx - step) > 25:
                val = idx - step - 26
                realStr = realStr + alphabetsSmall[val]
            else:
                realStr = realStr + alphabetsCaps[idx - step]
        else:
            realStr = realStr + x
    return realStr

# 2. reverseStr reverses a Text like reading it backwards
# It takes in the Text to encript, an optional boolean to know if it's doing a decript, and an optional boolean to know if its called from the encript() function
# note also that it is it's own decript function
def reverseStr(str, decript=False, fromEncript=False):
    backCount = len(str) - 1 # stores location of last character in the provided text ---str---
    newStr = ""
    for x in str: # loops through the characters of the provided text ---str--
        newStr = newStr + str[backCount] # adds the character on the last location to ---newStr--
        backCount = backCount - 1 # change last location to the next-to-last location

    if fromEncript == False and decript == False: # if this function was not called from the encript() function and its not a decript
        stringID = addId("reverseStr", {"algoName": "reverseStr", "decriptData": [newStr]}) # adds an Encription ID and store the data
        showencriptedandstore(stringID, newStr) # print the encritption id and mark as encripted
    return newStr

# 3. strToNum will create a list of ordered numbers from a provided starting number, and map the list to another list of letters of the same ---len()--
# It takes the Text to encript, a starting num, and an optional boolean to know if it's called from ---encript()---
def strToNum(str, startnum=(random.randint(1, 1000)), fromEncript=False):
    numArr = list(range(startnum, startnum+52)) # create list of numbers from ---startnum-- to ---startnum+52--- (cos there are 52 letters a-z-A-Z)
    letterArr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"," Y", "Z"]
    newStrData = []
    count = 0
    for x in str: # loop through each charater in provided text ---str---
        if x in letterArr:
            idx = letterArr.index(x) # get location of x in ---letterArr---
            numAlt = numArr[idx] # alternate character for x should be the number in the same location but in numArr
            numOfLetter = "% s" % numAlt
            count = count + 1
            xDict = { # create a dictionary
                "num": numOfLetter,
                "numAlt": numAlt,
                "noOfdigits": len(numOfLetter),
                "count": count
            }
            newStrData.append(xDict)
        else: # if character is not an alphabet
            count = count + 1
            xDict = {
                "num": x,
                "noOfdigits": 1,
                "count": count
            }
            newStrData.append(xDict)
    newStr = ""
    for dict in newStrData:
        newStr = newStr + dict["num"]
    if fromEncript == False:
        stringID = addId("strToNum", {"algoName": "strToNum", "decriptData": [newStrData, startnum]})
        showencriptedandstore(stringID, newStr)
        return  newStr
    else:
        return newStrData

def decriptStrToNum(data, startnum):
    numArr = list(range(startnum, startnum+52))
    letterArr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"," Y", "Z"]
    realStr = ""
    for x in data:
        if "numAlt" in x:
            num = (x["numAlt"])
            idx = numArr.index(num)
            letterOfNum = letterArr[idx]
            realStr = realStr + letterOfNum
        else:
            realStr = realStr + x["num"]
    return realStr

def mapLetter(str, map={}, fromEncript=False):
    newStrData = []
    count = 0
    for x in str:
        if x in map:
            count = count + 1
            newLetter = "% s" % map[x]
            xDict = {
                "newLetter": newLetter,
                "oldLetter": x,
                "noOfLetters": len(newLetter),
                "count": count
            }
            newStrData.append(xDict)
        else:
            count = count + 1
            xDict = {
                "newLetter": x,
                "oldLetter": x,
                "noOfLetters": 1,
                "count": count
            }
            newStrData.append(xDict)
    newStr = ""
    for dict in newStrData:
        newStr = newStr + dict["newLetter"]
    if fromEncript == False :
        stringID = addId("mapLetter", {"algoName": "mapLetter", "decriptData": [newStrData]})
        showencriptedandstore(stringID, newStr)
        return newStr
    else:
        return newStrData

def decriptMapLetter(data):
    realStr = ""
    for dict in data:
        realStr = realStr + dict["oldLetter"]
    return realStr


def encript(str, num=4,):
    newStr = str
    randomAlgos = []
    algos = storage["algos"]
    for x in range(num):
        tempNum = random.randint(0, len(algos) - 1)
        randomAlgos.append(algos[tempNum])
    decriptData = []
    for y in randomAlgos:
        if y == "rotShift":
            step = random.randint(1, 25)
            newStr = rotShift(newStr, step, True)
            decriptData.append([newStr, step])
        elif y == "reverseStr":
            newStr = reverseStr(newStr, False, True)
            decriptData.append([newStr])
        elif y == "strToNum":
            startNum = random.randint(0, 1000)
            newStrData = strToNum(newStr, startNum, True)
            decriptData.append([newStrData, startNum])
        elif y == "mapLetter":
            alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"," Y", "Z"]
            randomAlphabetsOrder = random.sample(alphabets, len(alphabets))
            alphabetsMap = {}
            for z in alphabets:
                idx = alphabets.index(z)
                alphabetsMap[z] = randomAlphabetsOrder[idx]
            newStrData = mapLetter(newStr, alphabetsMap, True)
            decriptData.append([newStrData, alphabetsMap])

    stringID = addId("encription", {"algoNames": randomAlgos, "decriptDatas": decriptData})
    showencriptedandstore(stringID, newStr)
    return newStr

def reverseEncript(algonames, decriptdatas):
    for algo in algonames:
        idx= algonames.index(algo)
        data = decriptdatas[idx]
        if algo == "rotShift":
            return decriptRotShift(data[0], data[1])
        elif algo == "reverseStr":
            return reverseStr(data[0], True, True)
        elif algo == "strToNum":
            return decriptStrToNum(data[0], data[1])
        elif algo == "mapLetter":
            return decriptMapLetter(data[0])
        else:
            return "Invalid Decription"

def decript(id):
    realStr = "null"
    name = re.sub("\d", "", id)
    if name in storage["idData"]:
        idslocation = storage["idData"][name]["ids"]
        if id in idslocation:
            data = storage["idData"][name]["ids"][id]["encriptionAlgoData"]
            if name == "encription":
                algoNames = data["algoNames"]
                decriptDatas = data["decriptDatas"]
                realStr = reverseEncript(algoNames, decriptDatas)
            else:
                algoName = data["algoName"]
                decriptData = data["decriptData"]

                if algoName == "rotShift":
                    realStr = decriptRotShift(decriptData[0], decriptData[1])  # str and step
                elif algoName == "reverseStr":
                    realStr = reverseStr(decriptData[0], decript=True)
                elif algoName == "strToNum":
                    realStr = decriptStrToNum(decriptData[0], decriptData[1])  # str and starting number
                elif algoName == "mapLetter":
                    realStr = decriptMapLetter(decriptData[0])
                else:
                    print("Unidentified Encryption")
            output = "\n\tOriginal String: {}\n"
            print(output.format(realStr))
        else:
            output = "\n\tEncription ID: \"{}\" does not exist"
            print(output.format(id))
            return
    else:
        output = "\n\tEncription ID: \"{}\" does not exist"
        print(output.format(id))
        return
    return realStr

def interact():
    exit = False
    while exit == False:
        inputedquery = "% s" % input("\nEnter Command: ")
        query = inputedquery.strip()
        if re.search("(^\s*exit\s*)|(^\s*Exit\s*)|(^\s*EXIT\s*)|(^\s*x\s*)|(^\s*X\s*)", query):
            exit = True
        elif re.search("(cmdl)|(CMDL)|(CommandList)|(cmdl\(\))", query):
            showcommandlist()
        elif re.search("(^\s*help\s*$)|(^\s*h\s*$)|(^\s*\?\s*$)", query):
            print("\tHELP: Start with the \"cmdl\" Command to view Command List")
        elif re.search("(^\s*get\s*$)|(^\s*GET\s*$)|(^\s*g\s*$)|(^\s*get\(\s*.*\s*\)\s*$)|(^\s*GET\(\s*.*\s*\)\s*$)|(^\s*g\(\s*.*\s*\)\s*$)", query):
            if re.search("(^\s*get\s*$)|(^\s*GET\s*$)|(^\s*g\s*$)|(^\s*get\(\s*\)\s*$)|(^\s*GET\(\s*\)\s*$)|(^\s*g\(\s*\)\s*$)", query):
                id = "% s" % input("Encription ID: ")
                getID(id)
            elif re.search("(^\s*get\(\s*.+\s*\)\s*)|(^\s*GET\(\s*.+\s*\)\s*)|(^\s*g\(\s*.+\s*\)\s*)", query):
                idtemp = re.sub("(\s*get\(('|\")?\s*)|(\s*GET\(('|\")?\s*)|(\s*g\(('|\")?\s*)", "", query)
                id = re.sub("(('|\")?\s*\)\s*)", "", idtemp)
                getID(id)
            else:
                print("Error: Invalid get Syntax")
        elif re.search("(^\s*del\s*)|(^\s*DEL\s*)|(^\s*delete\s*)|(^\s*DELETE\s*)|(^\s*del\(\s*.*\s*\)\s*)", query):
            if  re.search("(^\s*del\s*$)|(^\s*DEL\s*$)|(^\s*delete\s*$)|(^\s*DELETE\s*$)|(^\s*del\(\s*\)\s*$)|(^\s*DEL\(\s*\)\s*$)|(^\s*delete\(\s*\)\s*$)|(^\s*DELETE\(\s*\)\s*$)", query):
                id = "% s" % input("Encription ID: ")
                deleteID(id)
            elif re.search("(^\s*del\(\s*('|\")?.+('|\")?\s*\)\s*$)", query):
                idtemp = re.sub("(^\s*del\(\s*('|\")?)", "", query)
                id = re.sub("(('|\")?\s*\)\s*$)", "", idtemp)
                deleteID(id)
            else:
                print("Error: Invalid Del Syntax")
        elif re.search("(^\s*enc\(.*\)\s*|^\s*ENC\(.*\)\s*)|(^\s*Encript\(.*\)|^\s*encript\(.*\))|(^\s*Encript\s*|^\s*encript\s*|^\s*enc\s*|^\s*ENC\s*)", query):
            if re.search("(^\s*Encript\(\s*\)\s*$)|(^\s*encript\(\s*\)\s*$)|(^\s*ENC\(\s*\)\s*$)|(^\s*enc\(\s*\)\s*$)|(^\s*Encript\s*$)|(^\s*encript\s*$)|(^\s*ENC\s*$)|(^\s*enc\s*$)", query):
                arg1 = "% s" % input("Paste Text here and Enter: ")
                validInt = False
                while validInt == False:
                    arg2 = input("Choose no of encyption cycles [integer]: ")
                    if re.search("^\d+$", arg2):
                        arg2 = int(arg2)
                        if isinstance(arg2, int):
                            validInt = True
                        else:
                            print("\tError: no of encription cycles must to be a number, enter num")
                    else:
                        print("\tError: no of encription cycles must to be a number, enter num")
                encript(arg1, arg2)
            elif re.search("(^\s*Encript\(('|\").+('|\"),?\s*\)\s*$)|(^\s*encript\(('|\").+('|\"),?\s*\)\s*$)|(^\s*ENC\(('|\").+('|\"),?\s*\)\s*$)|(^\s*enc\(('|\").+('|\"),?\s*\)\s*$)", query):
                strtemp = re.sub("(\s*Encript\(\s*('|\"))|(\s*encript\(\s*('|\"))|(\s*ENC\(\s*('|\"))|(\s*enc\(\s*('|\"))", "", query)
                str = re.sub("(('|\"),?\s*\)\s*)", "", strtemp)
                encript(str)
            elif re.search("(^\s*Encript\(('|\").+('|\")((\s*)|(,\s*))\d+(,\s*|\s*)\)\s*$)|(^\s*encript\(('|\").+('|\")((\s*)|(,\s*))\d+(,\s*|\s*)\)\s*$)|(^\s*ENC\(('|\").+('|\")((\s*)|(,\s*))\d+(,\s*|\s*)\)\s*$)|(^\s*enc\(('|\").+('|\")((\s*)|(,\s*))\d+(,\s*|\s*)\)\s*$)", query):
                strtemp = re.sub("(\s*Encript\(\s*('|\"))|(\s*encript\(\s*('|\"))|(\s*ENC\(\s*('|\"))|(\s*enc\(\s*('|\"))", "", query)
                str = re.sub("(('|\")\s*,?\s*\d+,?\s*\)\s*)", "", strtemp)
                numtemp = re.sub("(\s*Encript\(\s*('|\").+('|\")\s*,?\s*)|(\s*encript\(\s*('|\").+('|\")\s*,?\s*)|(\s*ENC\(\s*('|\").+('|\")\s*,?\s*)|(\s*enc\(\s*('|\").+('|\")\s*,?\s*)", "", query)
                num = re.sub("((,\s*|\s*)\)\s*$)", "", numtemp)
                num = int(num)
                encript(str, num)
            else:
                print("\n\tError: Invalid Encript Command")
        elif re.search("(^\s*Decript\(.*\)|^\s*decript\(.*\))|(^\s*DEC\(.*\)\s*|^\s*dec\(.*\)\s*)|(^\s*Decript\s*|^\s*decript\s*|^\s*DEC\s*|^\s*dec\s*)", query):
            if re.search("(^\s*Decript\(\s*\)\s*$)|(^\s*decript\(\s*\)\s*$)|(^\s*DEC\(\s*\)\s*$)|(^\s*dec\(\s*\)\s*$)|(^\s*Decript\s*$)|(^\s*decript\s*$)|(^\s*DEC\s*$)|(^\s*dec\s*$)", query):
                id = "% s" % input("Enter Encription ID: ")
                decript(id)
            elif re.search("(\s*Decript\(\s*('|\")?.+('|\")?\s*\)\s*)|(\s*decript\(\s*('|\")?.+('|\")?\s*\)\s*)|(\s*DEC\(\s*('|\")?.+('|\")?\s*\)\s*)|(\s*dec\(\s*('|\")?.+('|\")?\s*\)\s*)", query):
                idtemp = re.sub("(\s*Decript\(\s*('|\")?)|(\s*decript\(\s*('|\")?)|(\s*DEC\(\s*('|\")?)|(\s*dec\(\s*('|\")?)", "", query)
                id = re.sub("(('|\")?\s*,?\s*\))", "", idtemp)
                decript(id)
            else:
                print("\n\tError: Invalid Decript Command")
        else:
            print("\n\tError: Invalid Command")

def startServer():
    print("\n\t\t.$#.WELCOME TO THE TEXT ENCRIPTION SERVER.@!%")
    print("\t\twhere \"784rbugoat fe87fe\" means \"Hello World\"\n")
    print("Need Help?, Enter \"help\" or \"h\"")
    interact()

startServer()