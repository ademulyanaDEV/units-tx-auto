# Ethereum Transaction Sender

This script allows you to send multiple transactions to random recipient addresses on the Ethereum network.

## Requirements

- Python 3.x
- `web3` library

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install required libraries:**
   You need to install the `web3` library to interact with the Ethereum blockchain. You can install it using pip:
   ```bash
   pip install web3
   ```

3. **Set up your private key:**
   Open the main script using your preferred text editor. For example, you can use `nano`:
   ```bash
   nano main.py
   ```
   Locate the line with `private_key = ''` and insert your private key between the quotes.

## Usage

To run the script, use the following command in your terminal:
```bash
python3 main.py
```

You will be prompted to enter the number of transactions you wish to send. The script will then attempt to send that many transactions to randomly selected recipient addresses.

## Notes

- Ensure you have sufficient ETH in your sender address to cover the transaction costs.
- The script will print the details of each transaction, including the amount sent and the transaction hash.
- If a transaction fails, the script will automatically retry until it is successful.

## Disclaimer

Use this script responsibly and be aware of the risks involved in handling cryptocurrencies. Make sure not to expose your private key and only test on test networks.
