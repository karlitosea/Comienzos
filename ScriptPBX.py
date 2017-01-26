#!usr/bin/env Python
# -*- coding: utf-8 -*-

import os, sys
import subprocess
import requests


'''comando = os.system("sudo su -")
comando = os.system("cd /var/log/asterisk/")
comando = os.system("cat full | grep Wrong")
print(comando)'''



def crear_ticket():
	"""Crea un ticket en invgate con los parámetros indicados"""
	url = 'https://mercadolibre:GPxK6FEnMWflkw6ik22pevuy@servicedesk.mercadolibre.com/api/v1/incident?'
	payload = {
        "category_id": "127",
        "description": "El log tanto: ",
        "type_id": "1",
        "priority_id": "2",
        "creator_id": "6959",
        "title": "Prueba de ticket automatico Charly",
        "customer_id": "6959",
        }
	r = requests.post(url, data=payload)
	print(r.content)
crear_ticket()