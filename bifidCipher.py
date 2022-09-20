"""
Palacios Rodriguez Diego Octavio
Bifid Cypher
"""
import re
from typing import final


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
        newMessage += matrix[x][y]
        print(newMessage)
        if not finalCoordsCopy: break

    return(newMessage)
    



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
        cypher(message.lower(), matrix)
        break




