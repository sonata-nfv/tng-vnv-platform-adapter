#!/usr/bin/python

from flask import Flask, request, jsonify, render_template
import os, sys, logging, uuid

import requests
from adapters.adapter import Adapter

class Osm(Adapter):

   #def __init__(self, name, host, type):
   #    Adapter.__inti__(self, name, host, type)

        def test(self):
                return "hola"

########################################## API Actions #########################################
#GET the Service Platform instantiate services
#@adapters.route('/services', methods=['GET'])
        def getServices(self):

                JSON_CONTENT_HEADER = {'Content-Type':'application/json'}
                sp_url = 'http://pre-int-sp-ath.5gtango.eu:32002/api/v3'

                url = sp_url + '/services'
                response = requests.get(url, headers=JSON_CONTENT_HEADER) 
                #return "hola"   
                if response.ok:        
                        return (response.text, response.status_code, response.headers.items())
                if response.content:
                        return (response.text, response.status_code, response.headers.items())    

########################################## API Actions #########################################
#GET the Service Platform instantiate services
#@app.route('/packages', methods=['GET'])
        def getPackages(self):

                JSON_CONTENT_HEADER = {'Content-Type':'application/json'}
                sp_url = 'http://pre-int-sp-ath.5gtango.eu:32002/api/v3'

                url = sp_url + '/packages'
                response = requests.get(url, headers=JSON_CONTENT_HEADER)    
                if response.ok:        
                        return (response.text, response.status_code, response.headers.items()) 
