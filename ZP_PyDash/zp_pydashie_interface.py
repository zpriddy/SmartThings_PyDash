#! /usr/bin/python
import sys
import requests
import pprint
import json
import os

from urllib import quote

import zp_smartthings

base_auth_url = "https://graph.api.smartthings.com/oauth/authorize?response_type=code&client_id="
base_auth_url2 = "&scope=app&redirect_uri="

callback_auth_url = "https://graph.api.smartthings.com/oauth/token?grant_type=authorization_code&client_id=CLIENTID&client_secret=CLIENTSECRECT&redirect_uri=URL&scope=app&code=CODE"

stInitd = False
selectedHue = None
selectedDimmer = None


def initST():
	global stInitd
	global smartThings
	global allDevices
	stInitd = False
	smartThings = zp_smartthings.SmartThings()


def initd():
	global stInitd
	return stInitd


def authInit(url,settingsFile="smartthings.json", filename="oauthin.json"):
	global smartThings
	global allDevices
	global oauthIn

	if(os.path.isfile(settingsFile)):
		init()
		return "/"

	oauthIn = {}
	with open(filename) as oauthfile:
		oauthIn = json.load(oauthfile)

	authURL = base_auth_url + oauthIn['client_id'] + base_auth_url2 + quote(url)	
	return authURL


def reauth(url,settingsFile="smartthings.json", filename="oauthin.json"):
	global smartThings
	global allDevices
	global oauthIn

	oauthIn = {}
	with open(filename) as oauthfile:
		oauthIn = json.load(oauthfile)

	authURL = base_auth_url + oauthIn['client_id'] + base_auth_url2 + quote(url)	
	return authURL

def authSecond(code, url, filename="smartthings.json"):
	global smartThings
	global allDevices
	global oauthIn

	authdata = {}

	authURL = callback_auth_url.replace("CLIENTID",oauthIn['client_id']).replace("CLIENTSECRECT",oauthIn['client_secret']).replace("CODE",code).replace("URL",quote(url))
	authdata = requests.get(authURL).json()
	authdata['client_id'] = oauthIn['client_id']
	authdata['client_secret'] = oauthIn['client_secret']
	authdata['api'] = "https://graph.api.smartthings.com/api/smartapps/endpoints/" + oauthIn['client_id'] + "/"
	authdata['api_location'] = "graph.api.smartthings.com"

	print authdata

	with open(filename,'w') as oauthfile:
		json.dump(authdata,oauthfile)

	return "/init"


def init():
	global stInitd
	global smartThings
	global allDevices
	stInitd = True

	#smartThings = zp_smartthings.SmartThings()
	smartThings.load_settings()
	smartThings.request_endpoints()

	allDevices = smartThings.getAllDevices()



def getAllDeviceType(deviceType):
	global allDevices
	return allDevices[deviceType]

def getDevice(deviceType, deviceId):
	global allDevices
	return allDevices[deviceType][deviceId]

def getDeviceStatus(deviceType, deviceId, deviceStatus):
	global allDevices
	device = getDevice(deviceType,deviceId)
	return device[deviceStatus]

def setSelectedHue(deviceId):
	global selectedHue
	selectedHue = deviceId

def getSelectedHue():
	global selectedHue
	return selectedHue

def setSelectedDimmer(deviceId):
	global selectedDimmer
	selectedDimmer = deviceId

def getSelectedDimmer():
	global selectedDimmer
	return selectedDimmer

def setColor(deviceId,color):
	global smartThings

	results = smartThings.set_color(deviceId,color)
	return results

def setColorHSLA(deviceId,hue,sat,color):
	global smartThings

	results = smartThings.set_color_hsla(deviceId,hue,sat,color)
	return results

def updateAll():
	global allDevices
	global smartThings

	allDevices = smartThings.getAllDevices()

def updateSwitch():
	global allDevices
	global smartThings

	allDevices['switch'] = smartThings.updateSwitch()

def updateColor():
	global allDevices
	global smartThings

	allDevices['color'] = smartThings.updateColor()

def updateContact():
	global allDevices
	global smartThings

	allDevices['contact'] = smartThings.updateContact()

def updatePresence():
	global allDevices
	global smartThings

	allDevices['presence'] = smartThings.updatePresence()

def updateHumidity():
	global allDevices
	global smartThings

	allDevices['humidity'] = smartThings.updateHumidity()

def updatePower():
	global allDevices
	global smartThings

	allDevices['power'] = smartThings.updatePower()

def updateMotion():
	global allDevices
	global smartThings

	allDevices['motion'] = smartThings.updateMotion()

def toggleSwitch(deviceId):
	global smartThings
	global allDevices

	newState = smartThings.command_switch(deviceId, 't')
	allDevices['switch'][deviceId]['state'] = newState
	allDevices['switch'] = smartThings.updateSwitch()

def setSwitch(deviceId,state):
	global smartThings
	global allDevices

	newState = smartThings.command_switch(deviceId, state)
	allDevices['switch'][deviceId]['state'] = state
	allDevices['switch'] = smartThings.updateSwitch()


def getMode():
	global allDevices
	return allDevices['mode']['Mode']['mode']

def updateMode():
	global allDevices
	global smartThings

	allDevices['mode'] = smartThings.updateMode()

def setMode(mode):
	global allDevices
	global smartThings

	smartThings.command_mode(mode)


def updateDimmer():
	global allDevices
	global smartThings

	allDevices['dimmer'] = smartThings.updateDimmer()

def setDimmer(deviceId,level):
	global allDevices
	global smartThings

	smartThings.command_dimmer(deviceId,level)
	allDevices['dimmer'][deviceId]['level'] = level
	allDevices['dimmer'] = smartThings.updateDimmer()

def getWeather():
	global smartThings

	return smartThings.get_weather()

def updateWeather():
	global allDevices
	global smartThings

	allDevices['weather'] = smartThings.updateWeather()

def updateTemp():
	global allDevices
	global smartThings

	allDevices['temperature'] = smartThings.updateTemp()

