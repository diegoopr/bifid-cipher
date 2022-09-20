"""
Palacios Rodriguez Diego Octavio
Bifid Cypher
"""
import re



def checkRepeat(secretKey):
    nonRepeated = ""
    
    for char in secretKey:
        if nonRepeated == "":
            nonRepeated += char
            continue
            
        if char in nonRepeated:
            continue
        else:
            nonRepeated += char
    print(nonRepeated)
    return(nonRepeated)
        

def fillMatrix(nonRepeated):
    nonRepeated.replace("j", "i")
    alphabet = "abcdefghiklmnopqrstuvwxyz" #no J
    row = 0
    col = 0
    matrix = [[0 for i in range(5)] for j in range(5)]

    for letter in nonRepeated:
        if col == 5:
            row += 1
            col = 0
        
        matrix[row][col] = letter
        col += 1

    for letter in alphabet:
        if col == 5:
            row += 1
            col = 0

        if letter in nonRepeated:
            continue
        else:
            matrix[row][col] = letter
            col += 1

    return(matrix)
    """
    for i in range(5):
        print("=============================")
        for j in range(5):
            print( "| ", matrix[i][j],  " |")
    print("=============================")
    """


def cypher(message, matrix):
    finalCoords = getCoords(message, matrix)
    cyphered = getNewMessage(finalCoords, matrix)
    print(cyphered)


def getNewMessage(finalCoords, matrix):
    #coordsInPairs = list(zip(finalCoords, finalCoords[1:] + finalCoords[:1]))
    #print(coordsInPairs)
    
    newMessage = ""
    length = len(finalCoords)
    finalCoordsCopy = finalCoords
    
    for i in range(int(length / 2) + 1):
        x = finalCoordsCopy.pop(0)
        y = finalCoordsCopy.pop(0)
        
        print(x, y)
        newMessage += matrix[x][y] #it should be x and y instead of y and x, but for the intent of the homework it'll be y and x.
        print(newMessage)
        if not finalCoordsCopy: break

    return(newMessage)
    
def getOldMessage(fullOldCoords, matrix):
    oldMessage = ""
    length = len(fullOldCoords)
    fullOldCoordsCopy = fullOldCoords

    for i in range(int(length / 2) + 1):
        x = int(fullOldCoordsCopy.pop(0))
        y = int(fullOldCoordsCopy.pop(0))

        print(x, y) #comment this line to avoid revealing the cipher
        oldMessage += matrix[x][y]
        print(oldMessage) #comment this line to avoid revealing the cipher
        if not fullOldCoordsCopy: break
    return(oldMessage)


def getCoords(message, matrix):
    coordsRow = list()
    coordsCol = list()
    for letters in message:

        for i in range(5):
            for j in range (5):
                if matrix[i][j] == letters:
                    coordsRow.append(i)
                    coordsCol.append(j)
                    continue
    
    print(coordsRow)
    print(coordsCol)
    #length = len(coordsRow) #given that a coordinate is conformed by two numbers, len(coordsRow) must be == to len(coordsCol)

    finalCoords = list()
    for letters in coordsRow:
        finalCoords.append(letters)
    
    for letters in coordsCol:
        finalCoords.append(letters)

    print(finalCoords)
    return(finalCoords)


def decypher(cyphered, matrix):
    print(getOldMessage(getOldCoords(getCoords(cyphered, matrix)), matrix))
    

def getOldCoords(coords):
    oldCoords = ''.join(str(coords))

    firstHalf = oldCoords[:len(oldCoords)//2]
    secondHalf = oldCoords[len(oldCoords)//2:]
    print(firstHalf)
    print(secondHalf)

    fH = "".join(c for c in firstHalf if c.isdecimal())
    print(fH)
    sH = "".join(c for c in secondHalf if c.isdecimal())
    print(sH)

    firstHalf = list(fH)
    secondHalf = list(sH)

    stepOneCoords = list()
    
    for coord in fH:
        x = firstHalf.pop(0)
        y = secondHalf.pop(0)
        stepOneCoords.append(x)
        stepOneCoords.append(y)

    print(stepOneCoords)
    print("hasta aqui todo OKKKKKKK")

    stepTwoCoords = ''.join(str(stepOneCoords))
    firstHalf = stepTwoCoords[:len(stepTwoCoords)//2]
    secondHalf = stepTwoCoords[len(stepTwoCoords)//2:]
    
    fH = "".join(c for c in firstHalf if c.isdecimal())
    print(fH)
    sH = "".join(c for c in secondHalf if c.isdecimal())
    print(sH)

    firstHalf = list(fH)
    secondHalf = list(sH)

    fullOldCoords = list()
    
    for coord in fH:
        x = firstHalf.pop(0)
        y = secondHalf.pop(0)
        fullOldCoords.append(x)
        fullOldCoords.append(y)

    return fullOldCoords




print("Welcome to Bifid Cipher.")


while(True):
    try:
        print("1. Encrypt a message.")
        print("2. Decrypt a message.")
        option = int( input("Type the number of option you want to select, or any other number to exit:\n>>"))
    except:
        print("Please, type a valid input.")
        continue
    


    if option == 1:
        while(True):
            secretKey = input("Please type your secret key.\nYour key should only contain letters in the English alphabet: \n>>")
            if (re.search("Ññ[0-9]", secretKey)):
                print("Please type a message that contains ONLY characters in the English alphabet.")
            else: 
                matrix = fillMatrix(checkRepeat(secretKey.lower()))
                print(matrix)
                break
        
        while(True):
            message = input("\nPlease type the message you wish to cypher.\nYour message should only contain letters in the English alphabet: \n>>")
            if (re.search("Ññ[0-9]", message)):
                print("Please type a message that contains ONLY characters in the English alphabet.")
            else:
                message.strip()
                cypher(message.lower(), matrix)
                break
    



    elif option == 2:
        while(True):
            secretKey = input("\nPlease type the secret key needed to decypher the message.\nYour key should only contain letters in the English alphabet: \n>>")
            if (re.search("Ññ[0-9]", secretKey)):
                print("Please type a message that contains ONLY characters in the English alphabet.")
            else: 
                matrix = fillMatrix(checkRepeat(secretKey.lower()))
                print(matrix)
                break
        
        while(True):
            cyphered = input("\nPlease type the message you wish to decrypt.\nYour message should only contain letters in the English alphabet: \n>>")
            if (re.search("Ññ[0-9]", cyphered)):
                print("Please type a message that contains ONLY characters in the English alphabet.")
            else:
                decypher(cyphered.lower(), matrix)
                break
    
    else:
        break

print("Bye (: ")




    







