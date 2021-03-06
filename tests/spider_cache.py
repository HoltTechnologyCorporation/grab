from copy import deepcopy
import itertools
import time
import logging

import six
import mock

from grab.error import GrabFeatureIsDeprecated
from tests.util import BaseGrabTestCase, build_spider
from grab.spider import Spider, Task

class SimpleSpider(Spider):
    pass


class CacheUsageRaisesExceptionTestCase(BaseGrabTestCase):
    def test_use_cache(self):
        bot = SimpleSpider()

        self.assertRaises(
            GrabFeatureIsDeprecated,
            lambda: bot.setup_cache(backend='mongodb')
        )
        self.assertRaises(
            GrabFeatureIsDeprecated,
            lambda: bot.cache_reader_service
        )
        self.assertRaises(
            GrabFeatureIsDeprecated,
            lambda: bot.cache_writer_service
        )
        self.assertRaises(
            GrabFeatureIsDeprecated,
            lambda: Task(disable_cache=True)
        )
        self.assertRaises(
            GrabFeatureIsDeprecated,
            lambda: Task(refresh_cache=True)
        )
        self.assertRaises(
            GrabFeatureIsDeprecated,
            lambda: Task(cache_timeout=1)
        )
