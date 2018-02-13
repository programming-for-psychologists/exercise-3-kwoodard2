'''Write a function called repetition which takes three arguments: 
    letters (a list), 
    numberBeforeSwitch (an integer),
    numRepetitions (also an integer). 
The function should produce a sequences of letters, one per line, such that 
calls to repetition with various parameters, generate the following outputs'''

def repetition_myversion(letters, numberBeforeSwitch, numRepetitions):   
    for i in range(numRepetitions):
        for i in letters:
            print (i + '\n') * (numberBeforeSwitch-1) + i
            #this last line makes sure not extra indent

def repetition(letters, numberBeforeSwitch, numRepetitions):   
    for i in range(numRepetitions):
        for i2 in letters:
            for i3 in range(numberBeforeSwitch):
                print i2



