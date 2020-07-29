def getASulfixToName():
    name = input('Name of the file:')
    if '.' not in name:
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
    wordsInFile = []
    for line in fhandle:
        line = line.strip()
        wordsInFile.append(line.split())
    return wordsInFile

def countWordsInFile(wordsList):
    wordsCounted = dict()
    for element in wordsList:
        wordsCounted[element] = wordsCounted.get(element, 0) + 1
    return wordsCounted

def main():
    name = getASulfixToName()
    wordsInFile = list()
    wordsInFile = handleFilesToList(name)
    print(wordsInFile)
    nad = dict()
    

if __name__ == '__main__':
    main()
