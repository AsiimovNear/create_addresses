from web3 import Web3
import datetime

web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/596ab8c6dc54432db6c5438d5b283126'))
accounts = []

for _ in range(int(input("Сколько адресов сгенерировать? "))):
    account = web3.eth.account.create()
    private_key = str(account.privateKey.hex())
    address = str(account.address)
    accounts.append([address, private_key])

    print(address + ": " + private_key)

with open(f'Accounts_{str(datetime.datetime.now()).replace(" ", "_").replace(":", "-")[:str(datetime.datetime.now()).index(".")]}.txt', 'w') as file:
    for k, v in accounts:
        file.write(f'{k}:{v}\n')
