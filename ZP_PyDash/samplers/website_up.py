from pydashie.dashie_sampler import DashieSampler

import requests

class WebsiteUpSampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)
        self._last = 0
        self.page = 'http://zpriddy.com'

    def name(self):
        return 'website_up'

    def sample(self):
        try:
            r = requests.get(self.page)
            assert r.status_code == 200
            up='on'
        except:
            up='off'
        s = {'state':up}
        return s

class StswitchSampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)
        self._last = 0

    def name(self):
        return "stswitch"

    def sample(self):
        return 'on'
