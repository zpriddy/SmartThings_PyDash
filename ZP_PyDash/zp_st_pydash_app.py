from smartthings_samplers import *

samplers = []


def run(app, xyzzyP):
    global samplers
    global xyzzy
    xyzzy = xyzzyP

    samplers = [
        StswitchSampler(xyzzy, 7),
        DimmerSampler(xyzzy, 7),
        ColorSampler(xyzzy, 7),
        HumiditySampler(xyzzy, 30),
        ContactSampler(xyzzy, 7),
        MotionSampler(xyzzy, 15),
        PowerSampler(xyzzy, 10),
        ModeSampler(xyzzy, 10),
        PresenceSampler(xyzzy, 10),
        WeatherSampler(xyzzy, 600),
        TempSampler(xyzzy,60)
        
    ]

    try:
        app.run(debug=True,
                port=5000,
                threaded=True,
                use_reloader=False,
                use_debugger=True,
                host='0.0.0.0'
                )
    finally:
        print "Disconnecting clients"
        xyzzy.stopped = True

        print "Stopping %d timers" % len(samplers)
        for (i, sampler) in enumerate(samplers):
            sampler.stop()

    print "Done"

def startSamplers():
    global samplers
    global xyzzy
    samplers = [

    ]
