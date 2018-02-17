#!/usr/bin/python3

import requests
from lxml import html
from bs4 import BeautifulSoup
import re

def get(query):
	headers = {
	    'Accept-Encoding': 'gzip, deflate, br',
	    'Accept-Language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7,da;q=0.6',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	}

	params = (
	    ('qr', query),
	)

	response = requests.get('https://registro.br/2/whois', headers=headers, params=params)

	soup = BeautifulSoup(str(response.text), "lxml")
	out = soup.findAll('pre')[0]
	return out

class registrobr:
	def __init__(self, domain):
		self.raw = re.sub("\<pre\>|\<\/pre>", "", str(get(domain)))
		try:
			self.dominio = re.findall('dom.nio\:\W*(.*)', str(self.raw))[0]
		except IndexError:
			self.dominio = ""
		try:
			self.cidr = self.inetnum = re.findall('inetnum:\W*(.*)', str(self.raw))[0]
		except IndexError:
			self.cidr = self.inetnum = ""
		self.titular = re.findall('titular\:\W*(.*)', str(self.raw))[0]
		self.documento = re.findall('documento\:\W*(.*)', str(self.raw))[0]
		self.responsavel = re.findall('respons.vel\:\W*(.*)', str(self.raw))[0]
		self.pais = re.findall('pa.s\:\W*(.*)', str(self.raw))[0]
		self.emails = re.findall('e\-mail\:\W*(.*)', str(self.raw))
