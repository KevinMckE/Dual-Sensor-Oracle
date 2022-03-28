# Input data from Serial Monitor feed
    # create serial object
    # read serial data line by line
    # create class for individual data points
    # set a loop that accepts the data from serial
    # store margin, input 1, and input 2 in variables in this class
    # use these variables to create new JSON for each aggregate
    # place these variables into SQL database / data structure 
    # JSON format
# Parse data from Serial Monitor feed, turn strings into ints

# Store data from Serial Monitor feed in JSON format
# Do I need to create a DB of JSON information? - If so is this SQL?
# Batch JSON into some other data storage(can you make lists of JSON?)

import hashlib, json, serial, web3

ser = serial.Serial(port = '/dev/cu.usbmodem1101', baudrate = 9600)#, timeout = 1)

data = ser.readline().decode('ascii')
print(data)

encoded = data.encode()
result = hashlib.sha256(encoded)
print(result.hexdigest())



