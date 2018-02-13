'''Can be masked or not masked; left or right'''

def trial_generator(numBlocks,blockLength): #function to print blocks
    count = 1
    for j in range (numBlocks):
        for i in range(blockLength):
            if i % 2 == 0:
                direction = 'left'
            elif i % 2 != 0:
                direction = 'right'  
            if i / 2 == 2:
                masking = 'unmasked'
            else:
                masking = 'masked'
            print str(count) + ',' + masking + ',' + direction
        count+=1
        
trial_generator(5,6)