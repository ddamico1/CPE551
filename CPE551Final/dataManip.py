from __future__ import division
import roulette_simulator


#numOfSamples = 100
#sizeOfSamples = 2000

#Function that converts the values for each key in each dictionary to decimal format,
# returns an array of these altered dictionaries
def getPercentages(numOfSamples, sizeOfSamples):
    DictArrayPercentages = []
    for dictionary in (roulette_simulator.roulette(numOfSamples,sizeOfSamples)): #For each dictionary in the array returned by roulette(x,y)
        #print 'NEW SAMPLE'
        for dictKEY in dictionary:  #for each key in the dictionary...
            timesOcurred = dictionary[dictKEY] #retrieves the amount of times a space won and copies that value to timesOccured
            percentage = timesOcurred / sizeOfSamples
            percentage *= 100
            dictionary[dictKEY] = percentage

        DictArrayPercentages.append(dictionary)

    return DictArrayPercentages
            

#Function to count how many samples have pockets that occured more than the desired threshold percentage.
def countAboveThresh(thresh, num, size):
    counter = 0
    DictArrayPercentages = getPercentages(num, size)
    for dictionary in DictArrayPercentages:
        for dictKEY in dictionary:
            if dictionary[dictKEY] >= thresh: #If a pocket occured at a higher rate than the threshold percentage...
                counter += 1
                break
    #print counter
    return counter



if __name__ == "__main__":
    #print(getPercentages())
    countAboveThresh(3.0)
   
