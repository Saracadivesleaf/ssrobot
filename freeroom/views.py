from django.shortcuts import render_to_response

import datetime
import urllib
import urllib2
from bs4 import BeautifulSoup

# Create your views here.
def midware(msg_text):
	attr = msg_text.split(' ')



def get_str(building, date, from_class, to_class):
	url = 'http://59.67.225.73/m/Home/FreeClassroom'
	data = {
		'JXML': building,
		'Date': date,
		'Begin': from_class,
		'End': to_class,
	}
	post_str = urllib.urlencode(data)

	res = urllib2.urlopen(url, post_str)
	page = res.read()

	# Resolve HTML page by BeautifulSOAP! Throw a soap!
	soap = BeautifulSoup(page)
	soap_throw = soap.find(name = 'div', attr = {'id': 'content'})
	soap_get = BeautifulSoup(soap_throw)
	soap_text = soap_get.text

def generate_page(free_room):
