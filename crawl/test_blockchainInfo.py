from unittest import TestCase
import time
from crawl.blockchain_info import BlockchainInfo
import logging

from crawl.models import Block


class TestBlockchainInfo(TestCase):
    # Get an instance of a logger
    logger = logging.getLogger(__name__)

    def test_get_blocks_in_one_day(self):
        r = BlockchainInfo.backfill_blocks_in_one_day(int(time.time()) * 1000)
        print(r)
        print(Block.objects.all().count())