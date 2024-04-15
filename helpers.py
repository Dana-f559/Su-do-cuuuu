import re
def checkInput(text: str) -> bool:

    # set the charachter to search only for number or .
    letter = r"(\d|\.)"

    # try to find all matches
    matches = re.search(r"^(?:\d|\.){9}$", text)

    # if matches then return true, that the input is correct
    if matches:
        return True

    # else return false
    return False

#This is to replace the . with -1 in the list
def DotToMinusOne(temp: str) -> list:

    #Making the input as a list
    temp = list(temp)
    #Iterating over that list for each of the number
    for value in range(len(temp)):
        #If it is . then making it -1
        if temp[value] == ".":
            temp[value] = "-1"
    
    #This is make the values from str to int
    return list(map(int,temp))