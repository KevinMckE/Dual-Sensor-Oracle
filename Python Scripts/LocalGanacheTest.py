from web3 import Web3

ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

account1 = "0x1b875Ff40D0aD942F1f290275292b8E5e73d69A6"
account2 = "0xd528340eB4098B676e40eF2Ed1B27391b9920355"

privateKey = "792566f667f088e0dd6767bf73f43d84bee203093e7006632821aa8841fe0c34"

nonce = web3.eth.getTransactionCount(account1)

tx = {
    'nonce': nonce,
    'to': account2,
    'value': web3.toWei(1, 'ether'),
    'gas': 200000,
    'gasPrice': web3.toWei('50', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, privateKey)
txHash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(txHash))
# send tx
# get tx hash