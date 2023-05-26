# Dual-Sensor-Oracle

Simple proof-of-concept of a blockchain-connected Arduino hardware oracle designed to increase likelihood of the validity of incoming data to a blockchain and reduce total data written to the blockchain.

This project takes input from two Arduino sensors, compares the values received, and if it is within an acceptable confidence rating then offers the user the option to write the information to a Kovan testnet smart contract.

If the information is not within this acceptable rating, the data is automatically discarded.

Apologies for poor commenting, if you want to actually use any of this, let me know.
