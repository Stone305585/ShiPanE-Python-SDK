# -*- coding: utf-8 -*-

from shipane_sdk.jobs.basic_job import BasicJob


class NewStockPurchaseJob(BasicJob):
    def __init__(self, client, client_aliases=None, name=None, **kwargs):
        super(NewStockPurchaseJob, self).__init__(name, kwargs.get('schedule', None), kwargs.get('enabled', False))

        self._client = client
        self._client_aliases = client_aliases

    def __call__(self):
        self._client.purchase_new_stocks()
