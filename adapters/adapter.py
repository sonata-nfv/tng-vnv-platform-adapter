#!/usr/bin/python

from flask import Flask, request, jsonify, render_template
import os, sys, logging, uuid, json
from werkzeug import secure_filename

#import serviceplatform
import psycopg2
import requests


class Adapter:

    def __init__(self, name):
        self.name = name
        self.host = "host"
        self.type = "type" 

    def getName(self):
        return self.name
    def setName(self, newName):
        self.name = newName        

    def getHost(self):
        return self.host
    def setHost(self, newHost):
        self.host = newHost

    def getType(self):
        return self.type
    def setType(self, newType):
        self.type = newType        


    def getDBType(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "172.18.0.2",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_type = "SELECT type FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_type)
            cursor.execute(get_type)
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

    def getDBHost(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "172.18.0.2",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_host = "SELECT host FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_host)
            cursor.execute(get_host)
            all = cursor.fetchall()
            #return jsonify(all), 200  
            return all, 200    
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


    def getPackages(self):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   

        sp_host_0 = self.getDBHost()
        print (sp_host_0)
        sp_host = sp_host_0.__str__()
        print (sp_host)
        #print (self.getDBHost())
        sp_host_1 = sp_host[4:]
        print ("sp1 es: ")
        print (sp_host_1)
        sp_host_2 = sp_host_1[:-10]
        print ("sp2 es: ")
        print (sp_host_2)

        url = sp_host_2 + '/packages'
        #url = sp_url + '/packages'
        response = requests.get(url, headers=JSON_CONTENT_HEADER)    
        if response.ok:        
                return (response.text, response.status_code, response.headers.items()) 




    def getPackage(self,name,vendor,version):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   

        sp_host_0 = self.getDBHost()
        print (sp_host_0)
        sp_host = sp_host_0.__str__()
        print (sp_host)
        #print (self.getDBHost())
        sp_host_1 = sp_host[4:]
        print ("sp1 es: ")
        print (sp_host_1)
        sp_host_2 = sp_host_1[:-10]
        print ("sp2 es: ")
        print (sp_host_2)

        url = sp_host_2 + '/packages'  
        print (name,vendor,version)
        response = requests.get(url,headers=JSON_CONTENT_HEADER)
        response_json = response.content
        jjson = json.loads(response_json)
        pkg = [x for x in jjson if x['pd']['name'] == name and x['pd']['vendor'] == vendor and x['pd']['version'] == version]
        
        if response.ok: 
                print(pkg)
                return jsonify(pkg)

    def deletePackage(self,name,vendor,version):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   

        sp_host_0 = self.getDBHost()
        print (sp_host_0)
        sp_host = sp_host_0.__str__()
        print (sp_host)
        #print (self.getDBHost())
        sp_host_1 = sp_host[4:]
        print ("sp1 es: ")
        print (sp_host_1)
        sp_host_2 = sp_host_1[:-10]
        print ("sp2 es: ")
        print (sp_host_2)

        url = sp_host_2 + '/packages'  
        print (name,vendor,version)
        response = requests.get(url,headers=JSON_CONTENT_HEADER)
        response_json = response.content
        jjson = json.loads(response_json)
        pkg = [x for x in jjson if x['pd']['name'] == name and x['pd']['vendor'] == vendor and x['pd']['version'] == version]
        
        if pkg:

            print(pkg)
            #uuid_to_delete = pkg['pd']['uuid']
            #uuid_to_delete_1 = [uuid for x in jjson if x['pd']['name'] == name and x['pd']['vendor'] == vendor and x['pd']['version'] == version]
            uuid_to_delete_1 = [obj['uuid'] for obj in jjson if(obj['pd']['name'] == name)]            
            print(uuid_to_delete_1)
            uuid_0 = uuid_to_delete_1.__str__()
            uuid_to_delete_2 = uuid_0[2:]
            print(uuid_to_delete_2)
            uuid_to_delete_3 = uuid_to_delete_2[:-2]
            print(uuid_to_delete_3)

            url_for_delete = url + '/' + uuid_to_delete_3
            print (url_for_delete)
            delete = requests.delete(url_for_delete, headers=JSON_CONTENT_HEADER)

        if response.ok:                 
                return (delete.text, delete.status_code, delete.headers.items())




    def getPackagebyId(self,name,vendor,version):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   

        sp_host_0 = self.getDBHost()
        print (sp_host_0)
        sp_host = sp_host_0.__str__()
        print (sp_host)
        #print (self.getDBHost())
        sp_host_1 = sp_host[4:]
        print ("sp1 es: ")
        print (sp_host_1)
        sp_host_2 = sp_host_1[:-10]
        print ("sp2 es: ")
        print (sp_host_2)

        url = sp_host_2 + '/packages'  
        print (name,vendor,version)
        response = requests.get(url,headers=JSON_CONTENT_HEADER)
        response_json = response.content
        jjson = json.loads(response_json)
        pkg = [x for x in jjson if x['pd']['name'] == name and x['pd']['vendor'] == vendor and x['pd']['version'] == version]
        
        if pkg:

            print(pkg)
            #uuid_to_delete = pkg['pd']['uuid']
            #uuid_to_delete_1 = [uuid for x in jjson if x['pd']['name'] == name and x['pd']['vendor'] == vendor and x['pd']['version'] == version]
            uuid_to_delete_1 = [obj['uuid'] for obj in jjson if(obj['pd']['name'] == name)]            
            print(uuid_to_delete_1)
            uuid_0 = uuid_to_delete_1.__str__()
            uuid_to_delete_2 = uuid_0[2:]
            print(uuid_to_delete_2)
            uuid_to_delete_3 = uuid_to_delete_2[:-2]
            print(uuid_to_delete_3)

            url_for_delete = url + '/' + uuid_to_delete_3
            print (url_for_delete)
            delete = requests.get(url_for_delete, headers=JSON_CONTENT_HEADER)

        if response.ok:                 
                return (delete.text, delete.status_code, delete.headers.items())                

                

                



    def uploadPackage(self,package):

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}           
        sp_host_0 = self.getDBHost()
        print (sp_host_0)
        sp_host = sp_host_0.__str__()
        print (sp_host)
        #print (self.getDBHost())
        sp_host_1 = sp_host[4:]
        print ("sp1 es: ")
        print (sp_host_1)
        sp_host_2 = sp_host_1[:-10]
        print ("sp2 es: ")
        print (sp_host_2)
        url = sp_host_2 + '/packages'
        
        print(package)
        print(url)

        files = {'package': open(package,'rb')}
        upload = requests.post(url, files=files)

        if request.method == 'POST':
            return upload.text

        



    def getServices(self):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   

        sp_host_0 = self.getDBHost()
        print (sp_host_0)
        sp_host = sp_host_0.__str__()
        print (sp_host)
        #print (self.getDBHost())
        sp_host_1 = sp_host[4:]
        print ("sp1 es: ")
        print (sp_host_1)
        sp_host_2 = sp_host_1[:-10]
        print ("sp2 es: ")
        print (sp_host_2)

        url = sp_host_2 + '/services'
        #url = sp_url + '/packages'
        response = requests.get(url, headers=JSON_CONTENT_HEADER)    
        if response.ok:        
                return (response.text, response.status_code, response.headers.items()) 

    def getService(self,name,vendor,version):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   

        sp_host_0 = self.getDBHost()
        print (sp_host_0)
        sp_host = sp_host_0.__str__()
        print (sp_host)
        #print (self.getDBHost())
        sp_host_1 = sp_host[4:]
        print ("sp1 es: ")
        print (sp_host_1)
        sp_host_2 = sp_host_1[:-10]
        print ("sp2 es: ")
        print (sp_host_2)

        url = sp_host_2 + '/services'  
        print (name,vendor,version)
        response = requests.get(url,headers=JSON_CONTENT_HEADER)
        response_json = response.content
        jjson = json.loads(response_json)
        pkg = [x for x in jjson if x['nsd']['name'] == name and x['nsd']['vendor'] == vendor and x['nsd']['version'] == version]
        
        if response.ok: 
                print(pkg)
                return jsonify(pkg)                


    def getServiceId(self,name,vendor,version):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   

        sp_host_0 = self.getDBHost()
        print (sp_host_0)
        sp_host = sp_host_0.__str__()
        print (sp_host)
        #print (self.getDBHost())
        sp_host_1 = sp_host[4:]
        print ("sp1 es: ")
        print (sp_host_1)
        sp_host_2 = sp_host_1[:-10]
        print ("sp2 es: ")
        print (sp_host_2)

        url = sp_host_2 + '/services'  
        print (name,vendor,version)
        response = requests.get(url,headers=JSON_CONTENT_HEADER)
        response_json = response.content
        print (response_json)
        jjson = json.loads(response_json)
        pkg = [x for x in jjson if x['nsd']['name'] == name and x['nsd']['vendor'] == vendor and x['nsd']['version'] == version]
        
        if pkg:

            print(pkg)
            uuid_to_delete_1 = [obj['uuid'] for obj in jjson if(obj['nsd']['name'] == name)]            
            print(uuid_to_delete_1)
            uuid_0 = uuid_to_delete_1.__str__()
            uuid_to_delete_2 = uuid_0[2:]
            print(uuid_to_delete_2)
            uuid_to_delete_3 = uuid_to_delete_2[:-2]
            print(uuid_to_delete_3)
            url_for_delete = url + '/' + uuid_to_delete_3
            print (url_for_delete)
            delete = requests.get(url_for_delete, headers=JSON_CONTENT_HEADER)
      
        if response.ok:                                        
                return uuid_to_delete_3
