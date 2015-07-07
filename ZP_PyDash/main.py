import os
import logging
import zp_st_pydash_app
from urllib import quote, unquote
from flask import Flask, render_template, Response, send_from_directory, request, current_app, redirect, jsonify, json
import zp_pydashie_interface as zp_st

app = Flask(__name__)
logging.basicConfig()
log = logging.getLogger(__name__)



@app.route("/")
def main():
    if(zp_st.getHostUrl() == None):
        print "Trying to set Host URL"
        zp_st.setHostUrl()
    if(zp_st.getHostUrl() == None):
        print "Error setting Host URL"
        exit()
    if(zp_st.initd()):
        return render_template('main.html', title='ZP SmartThings PyDash')
    else:
        return redirect("/auth/")

@app.route("/<path:path>/refresh/")
def refresh(path):
    print "Refreshing.."
    return redirect("/"+path)

@app.route("/refresh/")
def refreshed():
    print "Refreshing.."
    return redirect("/")

@app.route("/init/")
def init():
    print "Init.."
    zp_st.init()
    return redirect("/")

@app.route("/auth/")
def auth():
    print "auth.."
    zp_st.initST()
    redirecturl = zp_st.authInit("http://"+ zp_st.getHostUrl() + "/callback")
    return redirect(redirecturl)

@app.route("/reauth/")
def reauth():
    print "auth.."
    redirecturl = zp_st.reauth("http://"+ zp_st.getHostUrl() + "/callback")
    return redirect(redirecturl)

@app.route("/callback/")
def callback():
    authcode = request.args.get('code', '')
    redirecturl = zp_st.authSecond(authcode,"http://"+ zp_st.getHostUrl() + "/callback")
    return redirect(redirecturl)

@app.route("/switch/<path:path>/",methods = ['GET','POST'])
def switchState(path):
    if request.method == 'POST':
        data =  request.form
        device = data['deviceId']
        zp_st.toggleSwitch(device)
        status = zp_st.getDeviceStatus('switch',device,'state')
        if (status == 'on'):
            status = 'off'
        else:
            status = 'on'
        return Response(json.dumps({'error':1,'switch':status}))
    else:
        device =  unquote(path)
        status = zp_st.getDeviceStatus('switch',device,'state')
        results = {'switch':status}
        return Response(json.dumps(results))

@app.route("/setselectedhue/<path:path>/",methods = ['GET','POST'])
def selectedHueSet(path):
    device =  unquote(path)
    if request.method == 'POST':
        hue=zp_st.setSelectedHue(device)
        results = {'Set':True}
        return Response(json.dumps(results))
    else:
        hue=zp_st.setSelectedHue(device)
        results = {'Set':True}
        return Response(json.dumps(results))

@app.route("/setselecteddimmer/<path:path>/",methods = ['GET','POST'])
def selectedDimmerSet(path):
    device =  unquote(path)
    if request.method == 'POST':
        hue=zp_st.setSelectedDimmer(device)
        results = {'Set':True}
        return Response(json.dumps(results))
    else:
        #device =  unquote(path)
        hue=zp_st.setSelectedDimmer(device)
        results = {'Set':True}
        return Response(json.dumps(results))

@app.route("/setcolor/",methods = ['GET','POST'])
def setColor():
    if request.method == 'POST':
        data =  request.form
        device = zp_st.getSelectedHue()
        color = data['color']
        hue = data['hue']
        sat = data['sat']
        results = zp_st.setColorHSLA(device,hue,sat,color)
        return Response(json.dumps(results))
    else:
        results = {'Set':True}
        return Response(json.dumps(results))

@app.route("/setdimmer/",methods = ['GET','POST'])
def setDimmer():
    if request.method == 'POST':
        data =  request.form
        device = zp_st.getSelectedDimmer()
        level = data['level']
        if(level == "off"):
            zp_st.setSwitch(device,'off')
        else:
            zp_st.setSwitch(device,'on')
            zp_st.setDimmer(device,level)
        results = {'Set':True}
        return Response(json.dumps(results))
    else:
        results = {'Set':True}
        return Response(json.dumps(results))

@app.route("/selectedhue/",methods = ['GET','POST'])
def selectedHue():
    if request.method == 'POST':
        return Response(json.dumps({'error':1}))
    else:
        hue=zp_st.getSelectedHue()
        results = {'selectedhue':hue}
        return Response(json.dumps(results))

@app.route("/selecteddimmer/",methods = ['GET','POST'])
def selectedDimmer():
    if request.method == 'POST':
        return Response(json.dumps({'error':1}))
    else:
        hue=zp_st.getSelectedDimmer()
        results = {'selecteddimmer':hue}
        return Response(json.dumps(results))

@app.route("/color/<path:path>/",methods = ['GET','POST'])
def colorValue(path):
    if request.method == 'POST':
        data =  request.form
        device = data['deviceId']
        zp_st.toggleSwitch(device)
        status = zp_st.getDeviceStatus('switch',device,'state')
        if (status == 'on'):
            status = 'off'
        else:
            status = 'on'

        return Response(json.dumps({'error':1,'switch':status}))
    else:
        device =  unquote(path)
        hue = zp_st.getDeviceStatus('color',device,'hue')
        sat = zp_st.getDeviceStatus('color',device,'sat')
        results = {'hue':hue,'sat':sat}
        return Response(json.dumps(results))

@app.route("/hue/<path:path>/<path:color>/",methods = ['GET','POST'])
def hueColor(path,color):
    if request.method == 'POST':
        data =  request.form
        device = data['deviceId']
        zp_st.toggleSwitch(device)
        status = zp_st.getDeviceStatus('switch',device,'state')
        if (status == 'on'):
            status = 'off'
        else:
            status = 'on'
        return Response(json.dumps({'error':1,'switch':status}))
    else:
        device =  unquote(path)
        status = zp_st.getDeviceStatus('switch',device,'state')
        results = {'switch':status,'color':color}
        return Response(json.dumps(results))

@app.route("/contact/<path:path>/",methods = ['GET','POST'])
def contactState(path):
    if request.method == 'POST':
        return Response(json.dumps({'error':0}))
    else:
        device =  unquote(path)
        status = zp_st.getDeviceStatus('contact',device,'state')
        results = {'state':status}
        return Response(json.dumps(results))

@app.route("/humidity/<path:path>/",methods = ['GET','POST'])
def humidityValue(path):
    if request.method == 'POST':
        return Response(json.dumps({'error':0}))
    else:
        device =  unquote(path)
        status = zp_st.getDeviceStatus('humidity',device,'value')
        results = {'value':status}
        return Response(json.dumps(results))

@app.route("/power/<path:path>/",methods = ['GET','POST'])
def powerState(path):
    if request.method == 'POST':
        return Response(json.dumps({'error':0}))
    else:
        device =  unquote(path)
        power = zp_st.getDeviceStatus('power',device,'value')
        energy  = zp_st.getDeviceStatus('power',device,'energy')
        results = {'value':power,'energy':energy}
        return Response(json.dumps(results))

@app.route("/presence/<path:path>/",methods = ['GET','POST'])
def presenceState(path):
    if request.method == 'POST':
        return Response(json.dumps({'error':0}))
    else:
        device =  unquote(path)
        status = zp_st.getDeviceStatus('presence',device,'state')
        results = {'state':status}
        return Response(json.dumps(results))

@app.route("/motion/<path:path>/",methods = ['GET','POST'])
def motionState(path):
    if request.method == 'POST':
        return Response(json.dumps({'error':0}))
    else:
        device =  unquote(path)
        status = zp_st.getDeviceStatus('motion',device,'state')
        results = {'state':status}
        return Response(json.dumps(results))

@app.route("/dimmer/<path:path>/",methods = ['GET','POST'])
def dimmerState(path):
    if request.method == 'POST':
        data =  request.form
        device = data['deviceId']
        if( data['deviceType'] == 'dimmerLevel'):
            status = zp_st.getDeviceStatus('switch',device,'state')
            if (status == 'on') :
                level = data['level']
                zp_st.setDimmer(device,level)

            return Response(json.dumps({'error':1}))

        if( data['deviceType'] == 'switch'):
            zp_st.toggleSwitch(device)
            status = zp_st.getDeviceStatus('switch',device,'state')
            if (status == 'on'):
                status = 'off'
            else:
                status = 'on'

            return Response(json.dumps({'error':1,'switch':status}))

    else:
        device =  unquote(path)
        state = zp_st.getDeviceStatus('dimmer',device,'state')
        level = zp_st.getDeviceStatus('dimmer',device,'level')
        results = {'state':state,'level':level}
        return Response(json.dumps(results))

@app.route("/mode/",methods = ['GET','POST'])
def modeState():
    if request.method == 'POST':
        return Response(json.dumps({'error':1}))
    else:
        mode = zp_st.getMode()
        results = {'mode':mode}
        return Response(json.dumps(results))

@app.route("/setmode/<path:path>",methods = ['GET','POST'])
def modeSet(path):
    if request.method == 'POST':
        return Response(json.dumps({'error':1}))
    else:
        mode =  unquote(path)
        zp_st.setMode(mode)
        return redirect("/")

@app.route("/temp/<path:path>/",methods = ['GET','POST'])
def tempState(path):
    if request.method == 'POST':
        return Response(json.dumps({'error':1}))
    else:
        device =  unquote(path)
        temp = zp_st.getDeviceStatus('temperature',device,'value')
        results = {'value':temp}
        return Response(json.dumps(results))

@app.route("/weather/",methods = ['GET','POST'])
def modeWeather():
    if request.method == 'POST':
        return Response(json.dumps({'error':1}))
    else:
        weather = zp_st.getWeather()
        results = weather
        return Response(json.dumps(results))


@app.route("/dashboard/<dashlayout>/")
def custom_layout(dashlayout):
    return render_template('%s.html'%dashlayout, title='ZP SmartThings PyDash')

@app.route("/assets/application.js")
def javascripts():
    if not hasattr(current_app, 'javascripts'):
        import coffeescript
        scripts = [
            'assets/javascripts/jquery.js',
            'assets/javascripts/es5-shim.js',
            'assets/javascripts/d3.v2.min.js',


            'assets/javascripts/batman.js',
            'assets/javascripts/batman.jquery.js',

            'assets/javascripts/jquery.gridster.js',
            'assets/javascripts/jquery.leanModal.min.js',

            'assets/javascripts/dashing.coffee',
            'assets/javascripts/dashing.gridster.coffee',
            'assets/javascripts/cycleDashboards.coffee',

            'assets/javascripts/jquery.knob.js',
            'assets/javascripts/rickshaw.min.js',
            'assets/javascripts/application.coffee',
            #'assets/javascripts/app.js',
            'widgets/clock/clock.coffee',
            'assets/javascripts/clickablewidget.coffee',
            'widgets/stswitch/stswitch.coffee',
            'widgets/stmode/stmode.coffee',
            'widgets/stselectcolor/stselectcolor.coffee',
            'widgets/stselecthue/stselecthue.coffee',
            'widgets/stmodechange/stmodechange.coffee',
            'widgets/stdimmer/stdimmer.coffee',
            'widgets/stpresence/stpresence.coffee',
            'widgets/stweather/stweather.coffee',
            'widgets/sthumidity/sthumidity.coffee',
            'widgets/sttemp/sttemp.coffee',
            'widgets/stsetlevel/stsetlevel.coffee',
            'widgets/stselectdimmer/stselectdimmer.coffee',
            'widgets/stcontact/stcontact.coffee',
            'widgets/stmotion/stmotion.coffee',
            'widgets/stmeter/stmeter.coffee',
            'widgets/changepage/changepage.coffee',
            'widgets/number/number.coffee',
        ]
        nizzle = True
        if not nizzle:
            scripts = ['assets/javascripts/application.js']

        output = []
        for path in scripts:
            output.append('// JS: %s\n' % path)
            if '.coffee' in path:
                log.info('Compiling Coffee for %s ' % path)
                contents = coffeescript.compile_file(path)
            else:
                f = open(path)
                contents = f.read()
                f.close()

            output.append(contents)

        if nizzle:
            f = open('/tmp/foo.js', 'w')
            for o in output:
                print >> f, o
            f.close()

            f = open('/tmp/foo.js', 'rb')
            output = f.read()
            f.close()
            current_app.javascripts = output
        else:
            current_app.javascripts = ''.join(output)


    return Response(current_app.javascripts, mimetype='application/javascript')

@app.route('/assets/application.css')
def application_css():
    scripts = [
        'assets/stylesheets/application.css'
    ]
    output = ''
    for path in scripts:
        output = output + open(path).read()
    return Response(output, mimetype='text/css')

@app.route('/assets/images/<path:filename>')
def send_static_img(filename):
    directory = os.path.join('assets', 'images')
    return send_from_directory(directory, filename)

@app.route('/assets/fonts/<path:filename>')
def send_static_font(filename):
    directory = os.path.join('assets', 'fonts')
    return send_from_directory(directory, filename)

@app.route('/views/<widget_name>.html')
def widget_html(widget_name):
    html = '%s.html' % widget_name
    path = os.path.join('widgets', widget_name, html)
    if os.path.isfile(path):
        f = open(path)
        contents = f.read()
        f.close()
        return contents

import Queue

class Z:
    pass
xyzzy = Z()
xyzzy.events_queue = {}
xyzzy.last_events = {}
xyzzy.using_events = True
xyzzy.MAX_QUEUE_LENGTH = 20
xyzzy.stopped = False

@app.route('/events')
def events():
    if xyzzy.using_events:
        event_stream_port = request.environ['REMOTE_PORT']
        current_event_queue = Queue.Queue()
        xyzzy.events_queue[event_stream_port] = current_event_queue
        current_app.logger.info('New Client %s connected. Total Clients: %s' %
                                (event_stream_port, len(xyzzy.events_queue)))

        #Start the newly connected client off by pushing the current last events
        for event in xyzzy.last_events.values():
            current_event_queue.put(event)
        return Response(pop_queue(current_event_queue), mimetype='text/event-stream')

    return Response(xyzzy.last_events.values(), mimetype='text/event-stream')

def pop_queue(current_event_queue):
    while not xyzzy.stopped:
        try:
            data = current_event_queue.get(timeout=0.1)
            yield data
        except Queue.Empty:
            #this makes the server quit nicely - previously the queue threads would block and never exit. This makes it keep checking for dead application
            pass

def purge_streams():
    big_queues = [port for port, queue in xyzzy.events_queue if len(queue) > xyzzy.MAX_QUEUE_LENGTH]
    for big_queue in big_queues:
        current_app.logger.info('Client %s is stale. Disconnecting. Total Clients: %s' %
                                (big_queue, len(xyzzy.events_queue)))
        del queue[big_queue]

def close_stream(*args, **kwargs):
    event_stream_port = args[2][1]
    try:
        del xyzzy.events_queue[event_stream_port]
    except:
        log.info('Error Closing Client..')
    log.info('Client %s disconnected. Total Clients: %s' % (event_stream_port, len(xyzzy.events_queue)))


def run_zp_st_pydash_app():
    import SocketServer
    SocketServer.BaseServer.handle_error = close_stream
    SocketServer.ThreadingTCPServer.allow_reuse_address = True
    zp_st_pydash_app.run(app, xyzzy)


if __name__ == "__main__":
    zp_st.initST()
    run_zp_st_pydash_app()

