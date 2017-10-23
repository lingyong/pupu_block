import json

from django.http import HttpResponse
from django.shortcuts import render

from crawl.blockchain_info import BlockchainInfo
from crawl.models import Block


def block_detail(request, time):
    BlockchainInfo.backfill_blocks_in_one_day(time)
    count = Block.objects.all().count()
    return HttpResponse(json.dumps({"count": count}))