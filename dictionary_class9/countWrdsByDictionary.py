def getASulfixToName():
    name = input('Name of the file and relative path:')
    if '.txt' not in name:
        name = name+'.txt'
        print('Since you did not mention wich extension yu want, a .txt will be added as default')   
    try:
        fhandle = open(name)
        return name
    except:
        print(f'there is no file named {name}, verify and try again')
        return getASulfixToName()


def handleFilesToList(name):
    fhandle = open(name)
    singleString = fhandle.read() #i made it bacause reading each line will make a list of list (each line will be a list, and each word of the line will be a element of the line list), which will bug countWordsInFile(wordsList)
    singleString = singleString.rstrip()
    wordsInFile = singleString.split()
    return wordsInFile

def countWordsInFile(wordsList):
    wordsCounted = dict()
    for element in wordsList:
        wordsCounted[element] = wordsCounted.get(element, 0) + 1
    return wordsCounted

def getMostWrittenWord(countedWords):
    key = None
    value = None
    for k,v in countedWords.items():
        if (value == None) or (v > value):
            key = k
            value = v
    print(f'Most seen KEY: {key}\nNumber of times written: {value}')
    return

def main():
    name = getASulfixToName()
    wordsInFile = list()
    wordsInFile = handleFilesToList(name)
    countedWords = dict()
    countedWords = countWordsInFile(wordsInFile)
    getMostWrittenWord(countedWords)

if __name__ == '__main__':
    main()
