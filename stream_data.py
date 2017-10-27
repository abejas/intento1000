#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import time, datetime
import json

class Client (object):
	api_url = 'http://api.carriots.com/streams'

	def __init__ (self, api_key = None, client_type = "json"):
		self.client_type = client_type
		self.api_key = api_key
		self.content_type = 'application/vnd.carriots.api.v2+%s' %(self.client_type)
		self.headers = {"User-Agent": "Python-Client-Carriots",
				"Content-Type": self.content_type,
				"Accept": self.content_type,
				"Carriots.apikey": self.api_key}

	def send (self, data):
		self.data = json.dumps(data)
		request = urllib2.Request(Client.api_url, self.data, self.headers)
		self.response = urllib2.urlopen(request)
		return self.response

def main():
	client_carriots = Client ('af95cedc3e22f6fded83fe281ce51a5f66ad60bcfc49ca201e6a74b70bdfeffb')
	data = {'protocol': 'v2',
		'device': 'defaultDevice',
		'at': int(time.mktime(datetime.datetime.utcnow().timetuple())),
		'data' : {'Temp' : '15'}
		}
	carriots_response = client_carriots.send(data)
	return 0

if __name__ == "__main__":
	main()
