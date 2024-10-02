import json
import random
from web3 import Web3
import time

# Sender's private key
private_key = '' #MASUKAN PRIVATE KEY DI SINI

# Load recipient addresses from JSON file
with open('recipient_addresses.json') as f:
    recipient_addresses = json.load(f)

# User input for the number of transactions to send
user_input_count = int(input(f"Enter the number of transactions: "))

# Network configuration
network_config = {
    'rpc_url': 'https://rpc-testnet.unit0.dev',  # Update with your RPC URL
    'chain_id': 88817,  # Update with your chain ID, if different
}

# Function to connect to the Ethereum network
def connect_to_network(rpc_url):
    web3 = Web3(Web3.HTTPProvider(rpc_url))
    if not web3.is_connected():
        raise ConnectionError(f'Failed to connect to network: {rpc_url}')
    return web3

# Connect to the network
web3 = connect_to_network(network_config['rpc_url'])

# Get the sender's address
sender_address = web3.eth.account.from_key(private_key).address

# Get the nonce
nonce = web3.eth.get_transaction_count(sender_address)

# Success counter
success_count = 0

# Loop through the number of transactions requested by the user
for index in range(user_input_count):
    while True:  # Keep trying until the transaction is successful
        try:
            # Randomly select an address from the list, even if more than the available addresses
            recipient_address = random.choice(recipient_addresses)
            
            # Convert the recipient address to checksum format
            recipient_address = Web3.to_checksum_address(recipient_address)
            
            # Generate a random amount of ETH between 0.00000009 and 0.0000010
            random_amount_eth = random.uniform(0.00000009, 0.0000010)
            amount_in_wei = Web3.to_wei(random_amount_eth, 'ether')

            # Print the recipient address and amount to validate
            print(f"Attempting to send {random_amount_eth:.10f} ETH to recipient address: {recipient_address}")

            # Create the transaction
            tx = {
                'to': recipient_address,
                'value': amount_in_wei,
                'gasPrice': web3.eth.gas_price,  # Set gas price to the lowest available
                'nonce': nonce,
                'chainId': network_config['chain_id'],
            }

            # Estimate the required gas
            gas_limit = web3.eth.estimate_gas(tx)
            tx['gas'] = gas_limit  # Set the estimated gas limit

            # Sign the transaction
            signed_tx = web3.eth.account.sign_transaction(tx, private_key)

            # Send the transaction
            tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

            # Print the transaction hash and amount
            print(f'Transaction {index + 1} successful to {recipient_address} with amount: {random_amount_eth:.10f} ETH, hash: {web3.to_hex(tx_hash)}')

            # Increment the nonce for the next transaction
            nonce += 1

            # Increment success counter
            success_count += 1

            # Delay between transactions (set to 5 seconds)
            time.sleep(5)  # 5 seconds delay

            # Break out of the retry loop when successful
            break

        except Exception as e:
            print(f"Error during transaction {index + 1} to {recipient_address}: {str(e)}. Retrying...")

# Final output of successful transactions
print(f"Successfully processed {success_count} transactions.")
