## Dieter Gebert

##Read Error Log File and write error in new log file
##infile=r"SensorDataErrorFile.txt"

import mmap

f = open('SensorDataErrorFile.txt')
s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
if s.find('err') != -1:
    print('true')
    print('Error in Data')
    logFileTxtEr = open('SensorDataErrorLog.txt', 'a')                                              ##Create Error Log File 'SensorDAtaErrorLog.txt'
    logFileTxtEr.write((' ' + datetime.datetime.now().strftime(fmt).format()) + ' ' + str(myDict))  ##Write to Log File
    logFileTxtEr.close()
