myString = "My string"

print myString.upper()

print myString

print "this string".upper()

# Reverse

print "string"[::-1]

# Leekspeak



def leekSpeak(aParagraph):
    workingCopy = list(aParagraph)

    for i in range (0,(len(aParagraph))):
        if (workingCopy[i] == 'A' or workingCopy[i] == 'a'):
            workingCopy[i] = '4'
        elif (workingCopy[i] == 'E' or workingCopy[i] == 'e'):
            workingCopy[i] = '3'
        elif (workingCopy[i] == 'G' or workingCopy[i] == 'g'):
            workingCopy[i] = '6'
        elif (workingCopy[i] == 'I' or workingCopy[i] == 'i'):
            workingCopy[i] = '1'
        elif (workingCopy[i] == 'O' or workingCopy[i] == 'o'):
            workingCopy[i] = '0'
        elif (workingCopy[i] == 'S' or workingCopy[i] == 's'):
            workingCopy[i] = '5'
        elif (workingCopy[i] == 'T' or workingCopy[i] == 't'):
            workingCopy[i] = '7'

    return workingCopy

testParagraph = "Leet"

newParagraph = leekSpeak(testParagraph)

print str(newParagraph)

print testParagraph
