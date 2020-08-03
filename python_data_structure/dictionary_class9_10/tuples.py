bigString = 'this is a big sentence that i have no idea what to say but its ok, i have to do it anyway so i will just add random things like: there is a chicken in the house running with a dog in its mouth and a dog with a skirt. Such a voyeur, he has no shame using skirt without any panties on! \nBut nevetheless we continue our strugle to keep making words as random as it should be so we can count it all and get the most common ones out of it. Hope its big enought to make a fun exercise of counting.'

def removeNonisalNun(someText):
    txtWithAlphaNumOnly = ''
    for letter in someText:
        letter = letter.lower()
        if letter.isalnum() or letter == ' ':
            txtWithAlphaNumOnly += letter
    return txtWithAlphaNumOnly

def countWords(someText):
    wList = someText.split()
    wCounted = dict()
    for element in wList:
        wCounted[element] = wCounted.get(element, 0) + 1
    return wCounted

def orderedList(someDict):
    olList = list()
    ### a more compact and complex way to order it, to know more about it, search for List Comprehension ###
    olList = sorted( [ (value, key) for key,value in someDict.items()])
    ### this is a bigger way to do the same thing ###
    # for key,value in someDict.items():
    #     newTuple = (value, key)
    #     olList.append(newTuple)
    # olList = sorted(olList, reverse=True)
    return olList #return a list of tuples

def main():
    newString = removeNonisalNun(bigString)
    wordsCounted = countWords(newString)
    olList = orderedList(wordsCounted)
    print(olList)
if __name__ == '__main__':
    main()