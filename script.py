import time
import requests


def main():
    now = int(time.time()) * 1000

    while now > 0:
        print(now)
        r = requests.get("http://127.0.0.1:8000/chain/blocks/{}".format(now))
        print(r.json())
        now -= 24 * 60 * 60 * 1000

main()