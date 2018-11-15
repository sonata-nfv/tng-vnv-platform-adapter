#!/usr/bin/python

from flask import Flask, request, jsonify, render_template
import os, sys, logging, uuid
import psycopg2
import requests

import requests
from adapters.adapter import Adapter

class Sonata(Adapter):

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



        def getUsers(self):
                try:

                        connection = psycopg2.connect(user = "sonatatest",
                                                password = "sonata",
                                                host = "172.18.0.2",
                                                port = "5432",
                                                database = "gatekeeper")
                        cursor = connection.cursor()
                        print ( connection.get_dsn_parameters(),"\n")
                        
                        get_sps = ("""
                                SELECT A.* FROM pm_users A inner join service_platforms B on A.service_platform = B.name AND B.type = 'sonata'
                                """)               
                        cursor.execute(get_sps)
                        all = cursor.fetchall()
                        return jsonify(all), 200     
                except (Exception, psycopg2.Error) as error :
                        print (error)
                        exception_message = str(error)
                        return exception_message, 401
                finally:
                        #closing database connection.
                        if(connection):
                                cursor.close()
                                connection.close()
                                print("PostgreSQL connection is closed") 

        def getSPs(self):
                try:
                        connection = psycopg2.connect(user = "sonatatest",
                                                password = "sonata",
                                                host = "172.18.0.2",
                                                port = "5432",
                                                database = "gatekeeper")
                        cursor = connection.cursor()
                        print ( connection.get_dsn_parameters(),"\n")
                        #create table Service Platforms
                        get_sps = ("""
                        SELECT * FROM service_platforms WHERE type='sonata'
                                """)               
                        cursor.execute(get_sps)
                        all = cursor.fetchall()
                        return jsonify(all), 200     
                except (Exception, psycopg2.Error) as error :
                        print (error)
                        exception_message = str(error)
                        return exception_message, 401
                finally:
                        #closing database connection.
                        if(connection):
                                cursor.close()
                                connection.close()
                                print("PostgreSQL connection is closed")                  
