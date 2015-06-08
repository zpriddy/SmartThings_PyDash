from dashie_sampler import DashieSampler
import zp_pydashie_interface as zp_st

import random
import collections
import requests

class WebsiteUpSampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)
        self._last = 0
        self.page = 'https://zpriddy.com'

    def name(self):
        return 'website_up'

    def sample(self):
        try:
            r = requests.get(self.page)
            assert r.status_code == 200
            up='UP'
        except:
            up='DOWN'
        s = {'text':up}
        return s


class SynergySampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)
        self._last = 0

    def name(self):
        return 'synergy'

    def sample(self):
        s = {'value': random.randint(0, 100),
             'current': random.randint(0, 100),
             'last': self._last}
        self._last = s['current']
        return s

class BuzzwordsSampler(DashieSampler):
    def name(self):
        return 'buzzwords'

    def sample(self):
        my_little_pony_names = ['Rainbow Dash',
                                'Blossomforth',
                                'Derpy',
                                'Fluttershy',
                                'Lofty',
                                'Scootaloo',
                                'Skydancer']
        items = [{'label': pony_name, 'value': random.randint(0, 20)} for pony_name in my_little_pony_names]
        random.shuffle(items)
        return {'items':items}

class ConvergenceSampler(DashieSampler):
    def name(self):
        return 'convergence'

    def __init__(self, *args, **kwargs):
        self.seedX = 0
        self.items = collections.deque()
        DashieSampler.__init__(self, *args, **kwargs)

    def sample(self):
        self.items.append({'x': self.seedX,
                           'y': random.randint(0,20)})
        self.seedX += 1
        if len(self.items) > 10:
            self.items.popleft()
        return {'points': list(self.items)}


class StswitchSampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)
        self._last = 'on'

    def name(self):
        return "stswitch"

    def sample(self):

        zp_st.updateSwitch()
        results = zp_st.getAllDeviceType('switch')
        
        return results

class ContactSampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)
        self._last = 'on'

    def name(self):
        return "stcontact"

    def sample(self):

        zp_st.updateContact()
        results = zp_st.getAllDeviceType('contact')
        
        return results

class ColorSampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)
        self._last = 'on'

    def name(self):
        return "stcolor"

    def sample(self):

        zp_st.updateColor()
        results = zp_st.getAllDeviceType('color')
        
        return results

class PresenceSampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)
        self._last = 'on'

    def name(self):
        return "stpresence"

    def sample(self):

        zp_st.updatePresence()
        results = zp_st.getAllDeviceType('presence')
        
        return results

class MotionSampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)
        self._last = 'on'

    def name(self):
        return "stmotion"

    def sample(self):

        zp_st.updateMotion()
        results = zp_st.getAllDeviceType('motion')
        
        return results

class DimmerSampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)
        self._last = 'on'

    def name(self):
        return "stdimmer"

    def sample(self):

        zp_st.updateDimmer()
        results = zp_st.getAllDeviceType('dimmer')
        #print results
        
        return results

class PowerSampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)
        self._last = 'on'

    def name(self):
        return "stmeter"

    def sample(self):

        zp_st.updatePower()
        results = zp_st.getAllDeviceType('power')
        #print results
        
        return results

class WeatherSampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)
        self._last = 'on'

    def name(self):
        return "stweather"

    def sample(self):

        zp_st.updateWeather()
        results = zp_st.getWeather()
        
        return results

class TempSampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)
        self._last = 'on'

    def name(self):
        return "sttemp"

    def sample(self):

        zp_st.updateTemp()
        results = zp_st.getAllDeviceType('temperature')
        
        return results

class HumiditySampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)
        self._last = 'on'

    def name(self):
        return "sthumidity"

    def sample(self):

        zp_st.updateHumidity()
        results = zp_st.getAllDeviceType('humidity')
        
        return results

class ModeSampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)
        self._last = 'Unknown'

    def name(self):
        return "mode"

    def sample(self):
        zp_st.updateMode()
        mode = zp_st.getMode()
        results = {'mode':mode}
        
        return results