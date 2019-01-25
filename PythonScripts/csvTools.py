def toCSV(valArray, fileName):
    #Expects an array formatted like [[x,y,z],[xx,yy,zz]]
    csvFile = open(fileName,"w")
    #countX is a variable used to step through the 1st level of the list
    countX = 0
    for x in valArray:
        #countY is a variable used to step through the 2nd level of the list
        countY = 0
        #for loop looping through all items in  valArray, in this case, each 
        #item will be another list.
        for y in valArray[countX]:
            #This checks if you are at the last element of any given second 
            #level list.This is important because CSV files do not have another
            #comma at the end of a line.
            if countY < len(valArray[countX])-1:
                csvFile.write(valArray[countX][countY] + ",")
            else:
                csvFile.write(valArray[countX][countY])
            countY += 1
        csvFile.write('\n')
        countX += 1
    csvFile.close()

def fromCSV(csvFile):
    csvArr = []                                          
    csvFile = open(csvFile,"r")                           
    #The lineHold variable is initialized here with the first line of the file
    lineHold = csvFile.readline()
    #The while loop will loop through every line in the file by checking to see 
    #if there is a line stored in linehold, it evaluates to true, if ther isnt
    #it will evaluate to false, breaking the loop. 
    while lineHold:
        #strips away trailing newlines
        lineHold = lineHold.rstrip()
        #splits the given line into a list
        lineHold = lineHold.split(",")
        #appends said list to the csvArr list
        csvArr.append(lineHold)
        #lineHold is assigned a new line, and the loop attempts to continue
        lineHold = csvFile.readline()
    csvFile.close()
    return csvArr


#Testing
toCSV(fromCSV("testData.csv"),"nameTest.csv")


                                                                                                                                                                                                                                
