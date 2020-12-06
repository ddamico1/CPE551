#The purpose of this module is to house the generation of data for a simulated American Roulette table

import random

#Function that returns an array of dictionaries. Each dictionary is the result of a sample of spins.
def roulette(numOfSamples, sizeOfSamples):
    i = 0
    DictArray = [] #Create an empty list that will contain the final results of each sample.
    while (i < numOfSamples):
        i += 1
        j = 0
        
        #initializes dictionary to hold all pockets on a roulette wheel and how many times they occur in a sample.
        # 37 represents '0' ... 38 represents '00'.
        wheelValues = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0,
               13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:0, 22:0, 23:0,
               24:0, 25:0, 26:0, 27:0, 28:0, 29:0, 30:0, 31:0, 32:0, 33:0, 34:0,
               35:0, 36:0, 37:0, 38:0}
        while (j < sizeOfSamples):
            j += 1
            x = random.randrange(1, 39) #random number between 1 and 39 (1 included, 39 excluded).
            wheelValues[x] += 1
        DictArray.append(wheelValues)

    return DictArray

if __name__ == "__main__":
    print(roulette(50,300)) #For demonstration purposes... 50 samples, with each sample consisting of 300 spins

            








