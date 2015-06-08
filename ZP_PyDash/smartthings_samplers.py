from dashie_sampler import DashieSampler
import zp_pydashie_interface as zp_st

import random
import collections
import requests


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