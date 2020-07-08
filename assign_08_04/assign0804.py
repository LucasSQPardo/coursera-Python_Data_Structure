name = input('File name: ')
if '.' not in name:
    name = name+'.txt'

fileh = open(name)
differentWords = []

for line in fileh:
    line = line.rstrip()
    #differentWords.append(line.split())    #since we are acessing each string, this would make a list of a list(the words of each string
    #differentWords = differentWords + line.split() #this on the other hand, will get each possible element we split and add to the current list for every line we go through
    wordsFromString=line.split() 
    for word in wordsFromString:
        if word in differentWords:
            continue
        differentWords.append(word)

print(differentWords)