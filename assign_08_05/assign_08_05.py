def dealWithFile(fileToOpen):
    listOfEmails = []
    if '.' not in fileToOpen:
        fileToOpen = fileToOpen + '.txt'
    try:
        fileh = open(fileToOpen)
    except:
        print(f'File {fileToOpen} not found')
        quit()

    for line in fileh:
        line = line.rstrip()
        if 'From' in line:
            getEmailFromList(listOfEmails, line.split())
    return listOfEmails

def getEmailFromList(emailList, listToLook):
    for element in listToLook:
        if '@' in element:
            emailList.append(element)
    return emailList

def main():
    fileName = input('File name: ')
    listOfEmails = dealWithFile(fileName)
    for email in listOfEmails:
        print(email)

if __name__ == "__main__":
    main()

