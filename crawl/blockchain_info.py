import requests
import time
from crawl.models import Block


class BlockchainInfo:
    def backfill_blocks_in_one_day(epoch_time):
        start = time.time()
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        r = requests.get("https://blockchain.info/blocks/{}?format=json".format(epoch_time), headers=headers)
        end = time.time()
        print("request took: {}".format(end-start))

        start = time.time()
        for block in r.json()['blocks']:
            hash = block['hash']
            t = block['time']
            # only insert if the time stamp doesn't exist
            if Block.objects.filter(time=t).count() == 0:
                b = Block(time=t, block_hash=hash)
                b.save()
        end = time.time()
        print("db write took: {}".format(end-start))
