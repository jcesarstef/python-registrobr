# python-registrobr
A tiny library to handle with RegistroBR whois querys


# Motivation
From some troubles to manage Whois queries from brazilian domains/CIDR's with python libraries, i decide to build my own whois library.


# Installing (Manual only now, make a Pull request and help me to fix this :D)
```
$ git clone https://github.com/jcesarstef/python-registrobr

$ cd python-registrobr

$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from registrobr import registrobr
>>> query = registrobr("baixaki.com.br")
>>> query.dominio
'baixaki.com.br'
>>> query.titular
'No Zebra Network S.A.'
>>> query.documento
'04.883.570/0001-28'
>>> query.responsavel
'Sobhan Daliry'
>>> query2 = registrobr("200.160.4.2")
>>> query2.cidr
'200.160.0.0/20'
>>> query2.emails
['fneves@registro.br']
>>> 


```
