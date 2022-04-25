import os
import json
from web3 import Web3

infura_url = 'https://kovan.infura.io/v3/f6f6710578e443d6ba9a7e3a5ed3319c'
web3 = Web3(Web3.HTTPProvider(infura_url))

privateKey = os.environ.get('TEST_PRIVATE_KEY')
account = '0x01accf242Ba1828E84B648FF8059a195b9Bfa08e' #test metamask account

print(web3.isConnected())

abi = json.loads('[{"inputs": [],"name": "data","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"},{"inputs": [],"name": "get","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"},{"inputs": [{"internalType": "string","name": "_data","type": "string"}],"name": "set","outputs": [],"stateMutability": "nonpayable","type": "function"}]')
address = Web3.toChecksumAddress('0xef4e99c254a14c324aa1a9edf0cf0f037ab01373')

contract = web3.eth.contract(address= address, abi= abi)
print(contract.functions)
# print(contract)

tx = {
  'to': Web3.toChecksumAddress('0xef4e99c254a14c324aa1a9edf0cf0f037ab01373'),
  'from': Web3.toChecksumAddress('0x01accf242Ba1828E84B648FF8059a195b9Bfa08e'),
  'gas' : 20000,
}

tx = contract.functions.set('helloworld').transact(sendTx)
signedTx = web3.eth.account.signTransaction(tx, privateKey)
txHash = web3.eth.sendRawTransaction(signedTx.rawTransaction)
print(txHash)
web3.eth.waitForTransactionReceipt(txHash)
print(contract.functions.get().call())