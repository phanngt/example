from datetime import datetime
import os


def buy_token(tezos_client_command):
    time_threshold = datetime(2021, month=10, day=13, hour=1, minute=15, second=0)
    while True:
        time_now = datetime.utcnow()
        print(time_now)
        if time_now >= time_threshold:
            result = os.system(tezos_client_command)
            if result == 0:
                print("BUY SUCCESS")
                break
            else:
                print("OH SHIT, SOMETHING IS WRONG")
        else:
            print("NOT TIME")


tezoz_client_command = "tezos-client --endpoint https://mainnet-node.madfish.solutions transfer 120 from  hoangkaay to KT1EprinFopUPZRVsSNta93QT3LVZUPpuoBF --entrypoint 'mint' --arg '4' --burn-cap 0.1 --fee 0.5 --fee-cap 1.5"

buy_token(tezoz_client_command)

