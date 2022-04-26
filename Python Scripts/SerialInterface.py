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

import hashlib
import os
import json
import serial
from web3 import Web3

ser = serial.Serial(port = '/dev/cu.usbmodem1101', baudrate = 9600)#, timeout = 1)

data = ser.readline().decode('ascii')
print(data)

encoded = data.encode()
result = hashlib.sha256(encoded)
print(result.hexdigest())

infura_url = 'https://kovan.infura.io/v3/f6f6710578e443d6ba9a7e3a5ed3319c'
web3 = Web3(Web3.HTTPProvider(infura_url))

privateKey = os.environ.get('TEST_PRIVATE_KEY')
account = '0x01accf242Ba1828E84B648FF8059a195b9Bfa08e' #test metamask account

print(web3.isConnected())
print(privateKey)

abi = json.loads('[{"inputs": [],"name": "data","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"},{"inputs": [],"name": "get","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"},{"inputs": [{"internalType": "string","name": "_data","type": "string"}],"name": "set","outputs": [],"stateMutability": "nonpayable","type": "function"}]')
address = Web3.toChecksumAddress('0xef4e99c254a14c324aa1a9edf0cf0f037ab01373')


contract = web3.eth.contract(address= address, abi= abi)
nonce = web3.eth.get_transaction_count(account)
# print(contract)

txData = {
    'from': Web3.toChecksumAddress('0x01accf242Ba1828E84B648FF8059a195b9Bfa08e'),
  'maxFeePerGas' : 2000000000,
  'maxPriorityFeePerGas' : 1000000000,
  'nonce' : nonce,
}

tx = contract.functions.set(result.hexdigest).buildTransaction(txData)
signedTx = web3.eth.account.sign_transaction(tx, privateKey)
txHash = web3.eth.send_raw_transaction(signedTx.rawTransaction)
web3.eth.wait_for_transaction_receipt(txHash)
print(contract.functions.get().call())
