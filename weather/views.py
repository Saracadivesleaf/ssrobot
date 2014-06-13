#-*- coding:utf-8 -*-

from django.shortcuts import render
import urllib2
import urllib
import json



# Create your views here.
def weather_query(location):
	data = {
		'location': location.encode('utf-8'),
		'output': 'json',
		'ak': 'dEXMWXM0cNvDebkOmq5S1djG',
	}
	url = 'http://api.map.baidu.com/telematics/v3/weather'
	post_str = urllib.urlencode(data)
	full_url = url + '?' + post_str
	res = urllib2.urlopen(full_url)

	json_get = res.read()
	result = json.loads(json_get)
	msg_str = decode_weather(result)
	print msg_str

	msg_content = {
		'msg_type': 'text',
		'content': msg_str
	}

	return msg_content



def decode_weather(result):
	weather_today = result['results'][0]['weather_data'][0]
	print weather_today
	msg_str = 'Weather: ' + weather_today['weather'] + '\n' + 'Temperature: ' + weather_today['temperature'] + '\n' + 'Wind: ' + weather_today['wind']

	return msg_str


def show_weather(request):
	location = u'北京'
	msg_content = weather_query(location)