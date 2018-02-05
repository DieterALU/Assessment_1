# Assessment_1

## Dieter Gebert
## Create sensor data for 32 sensors with 16 bit data and store in a file

##Imports
import random

##Initialize all parameters
NoOfDict = 32                                                                   ##No of Sensors
NoOfFloat = 16                                                                  ##Floating numbers in a Dictionary
count = 1
myDict = {}                                                                     ##Creat Dictionary

##Crete the x number dictionary's with bits and data
for i in range(NoOfDict):
    tempNameDict = "sensor_data_" + str(i)
    myDict[tempNameDict] = []
    for j in range(NoOfFloat):
        tempNameBit = "bit_" + str(j)
        myDict[tempNameDict].append([tempNameBit, random.uniform(0.0, 1.0)])    ##append the dictionary x with bit x and sensor data x

for l in range(NoOfDict):
    print 'Sensor number:', count
    count = count + 1
    for k in range(NoOfFloat):
        print myDict['sensor_data_1'][k]                                        ##Print the dictionarys x

    if myDict.keys() == 'err':                                                  ##Check Dictionary for 'err' error
       print("Error in Data")
       logFileTxtEr = open('SensorDataErrorLog.txt','w')                        ##Create Error Log File 'SensorDAtaErrorLog.txt'
       logFileTxtEr.writelines(myDict)                                          ##Write to Log File
       logFileTxtEr.close()                                                     ##Close Log File
    else:
       print("Data is Good")

    logFileTxt = open('SensorDataLog.txt','w')                                  ##Create Log File 'SensorDataLog.txt'
    logFileTxt.writelines(str(myDict))                                          ##Write to Log File
    logFileTxt.close()                                                          ##Close Log File
