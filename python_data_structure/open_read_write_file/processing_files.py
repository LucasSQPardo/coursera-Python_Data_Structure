def lengthOfFile(fileVectorVar):
    length = len(fileVectorVar)
    return length

def foundSomething(fileVariable):
    searchTerm = input("Keyword: ")
    for lines in fileVariable:
        if searchTerm in lines:
            print(lines.strip())
    return

def readIt(fileVariable):
    for line in fileVariable:
        print(line)
    return


def main():
    fileName = input('Put the name of the file you want to open: ')
    if '.' not in fileName:
        print('since you did not specified wich extension you want to open, the .txt will be added for default')
        fileName = fileName+'.txt'

    try:
        fHand = open(fileName)
    except:
        print(f'there was no file: {fileName} ')
        quit()
    #readIt(fHand) #call the function that will print it as strings
    #fileVectorVar = fHand.read() #this is a single vector with all the characters of the file, pretty usefull to know the length of the file or to print certain numbers of characters
    
    foundSomething(fHand)
    
if __name__ == "__main__":
    main()

