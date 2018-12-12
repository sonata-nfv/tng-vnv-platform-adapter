#!/usr/bin/python

from flask import Flask, request, jsonify, render_template
import os, sys, logging, uuid, json
from werkzeug import secure_filename

#import serviceplatform
import psycopg2
import requests
import subprocess
import models.database as database
import re
import ast
from ast import literal_eval

FILE = "db-config.cfg"

  


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


    def updateToken(self,token):
        try:
            db = database.Database(FILE)
            connection = psycopg2.connect(user = db.user,
                                        password = db.password,
                                        host = db.host,
                                        port = db.port,
                                        database = db.database)  
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            print (self.name)
            get_type = "SELECT type FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_type)            
            update_token = "UPDATE service_platforms SET service_token = \'" +token+ "\' WHERE name = \'" +self.name+ "\'"            
            print (update_token)
            cursor.execute(update_token)
            connection.commit()
            return "token updated", 200    
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



    def getDBType(self):
        try:
            db = database.Database(FILE)
            connection = psycopg2.connect(user = db.user,
                                        password = db.password,
                                        host = db.host,
                                        port = db.port,
                                        database = db.database)  
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_type = "SELECT type FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_type)
            cursor.execute(get_type)
            all = cursor.fetchall()
            #return jsonify(all), 200 
            type_0 = all.__str__()
            print(type_0)
            type_1 = type_0[3:]            
            print(type_1)            
            type_2 = type_1[:-4]            
            print(type_2)                  
            return type_2
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
            db = database.Database(FILE)
            connection = psycopg2.connect(user = db.user,
                                        password = db.password,
                                        host = db.host,
                                        port = db.port,
                                        database = db.database)  
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            print (self.name)
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
        my_type =  self.getDBType()
        if my_type == 'sonata':               

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
        if my_type == 'osm': 
            return "osm packages"



    def getPackage(self,name,vendor,version):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'} 

        my_type =  self.getDBType()
        if my_type == 'sonata':    
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

        my_type =  self.getDBType()
        if my_type == 'sonata':    
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
        
        my_type =  self.getDBType()
        if my_type == 'sonata':              

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
        my_type =  self.getDBType()
        if my_type == 'sonata':               

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

    def uploadOSMService(self,request): 
        #JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()
        if my_type == 'osm':               

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

            sp_host_3 = sp_host_2[7:]
            print ("sp3 es: ")
            print (sp_host_3)            


            content = request.get_json()
            print ("request content:")
            print (content)
            

            token = self.getOSMToken(request)
            print (token)
            file_to_upload = content['service']
            print ("File to upload")
            print (file_to_upload)
            file_composed = "@" + file_to_upload
            print (file_composed)

            #file = {'file': open(file_to_upload, 'rb')}
            file = {'nsd-create': open(file_to_upload, 'rb')}
            
            print (file)
            data = {'service':file_to_upload}
            #data = request.get_json()
            print (data)

            HEADERS = {
                'Accept':'application/yaml',
                'Content-Type':'application/zip', 
                'Authorization':'Bearer ' +token+''                
            }
            print (HEADERS)

            url = sp_host_2 + ':9999/osm/nsd/v1/ns_descriptors_content'
            url_2 = url.replace("http","https")
            print (url_2)
            

            #upload_nsddddd = "osm --hostname " + sp_host_3 + " vnfd-create " + url_2
            upload_nsd = "curl -X POST --insecure -w \"%{http_code}\" -H \"Content-type: application/zip\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            upload_nsd_2 = upload_nsd +token + "\" "
            upload_nsd_3 = upload_nsd_2 + " --data-binary "
            upload_nsd_4 = upload_nsd_3 + "\"@" +file_to_upload+ "\" " + url_2
            print (upload_nsd_4)
            upload = subprocess.check_output([upload_nsd_4], shell=True)
            #return jsonify(upload_nsd_4) 
            return (upload)

      

    def uploadOSMFunction(self,request): 
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()
        if my_type == 'osm':               

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

            sp_host_3 = sp_host_2[7:]
            print ("sp3 es: ")
            print (sp_host_3)            

            
            token = self.getOSMToken(request)
            print (token)
            content = request.get_json()
            file_to_upload = content['function']
            url = sp_host_2 + ':9999/osm/vnfpkgm/v1/vnf_packages_content'
            url_2 = url.replace("http","https")
            print (url_2)
            
            upload_nsd = "curl -X POST --insecure -w \"%{http_code}\" -H \"Content-type: application/zip\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            upload_nsd_2 = upload_nsd +token + "\" "
            upload_nsd_3 = upload_nsd_2 + " --data-binary "
            upload_nsd_4 = upload_nsd_3 + "\"@" +file_to_upload+ "\" " + url_2
            print (upload_nsd_4)
            upload = subprocess.check_output([upload_nsd_4], shell=True)
            #return jsonify(upload_nsd_4) 
            return (upload) 



    def getServices(self):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}  
        my_type =  self.getDBType()
        if my_type == 'sonata':                
 
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

        if my_type == 'osm':                

            sp_host_0 = self.getDBHost()
            print (sp_host_0)
            sp_host = sp_host_0.__str__()
            print (sp_host)
            sp_host_1 = sp_host[4:]
            print ("sp1 es: ")
            print (sp_host_1)
            sp_host_2 = sp_host_1[:-10]
            print ("sp2 es: ")
            print (sp_host_2)
            sp_host_3 = sp_host_2[7:]
            print ("sp3 es: ")
            print (sp_host_3)            

            url = sp_host_2 + '/services'
            get_nsd_list = "osm --hostname " + sp_host_3 + " nsd-list"
            print (get_nsd_list)
            #get = os.system(get_nsd_list).__str__()    
            #return get
            get = subprocess.check_output([get_nsd_list], shell=True)
            return (get)
            

    def getFunctions(self):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}  
        my_type =  self.getDBType()
        if my_type == 'sonata':                

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

            url = sp_host_2 + '/functions'
            #url = sp_url + '/packages'
            response = requests.get(url, headers=JSON_CONTENT_HEADER)    
            if response.ok:        
                    return (response.text, response.status_code, response.headers.items()) 

        if my_type == 'osm':                

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
            sp_host_3 = sp_host_2[7:]
            print ("sp3 es: ")
            print (sp_host_3)            

            url = sp_host_2 + '/functions'
            get_vnfd_list = "osm --hostname " + sp_host_3 + " vnfd-list"
            print (get_vnfd_list)
            #get = os.system(get_nsd_list).__str__()
            #return get                    
            get = subprocess.check_output([get_vnfd_list], shell=True)
            return (get)            

    def getService(self,name,vendor,version):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}  

        my_type =  self.getDBType()
        if my_type == 'sonata':                

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

    def getServiceInstantiations(self,name,vendor,version):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}  

        my_type =  self.getDBType()
        if my_type == 'sonata':                

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

            url = sp_host_2 + '/requests'  
            print (name,vendor,version)
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            #response_json = response.text
            print (response_json)
            #json_str = json.dumps(response._content)
            #jjson = json.loads(response.text.__str__())
            #jjson = json.loads(response_json)
            jjson = json.loads(response.content)
            print (jjson)
            #services = [x for x in jjson if x['service']['name'] == name and x['service']['vendor'] == vendor and x['service']['version'] == version]

            #print (jjson['service']['name'])
            #print (obj for obj in jjson if(obj['service']['vendor'] == 'eu.5gtango'))
            #illo = [obj for obj in jjson if(obj['service'] == '11111')]
            
            print ("illo")
            #idd = print ([obj for obj in jjson[0]['service']['uuid']])
            idd = print (jjson[0]['service']['uuid'])
            idd = print (jjson[0]['service']['name'])
            idd = print (jjson[1]['service']['uuid'])
            idd = print (jjson[1]['service']['name'])            
   
            #idd = [obj.service['name'] for obj in jjson]
            print ("illo")
            
            
            N = 0
            for N in range(10000):
                print (jjson['service']['uuid'])

                N = N + 1
                print (N)


            

            


            if response.ok:        
                #return (response.text, response.status_code, response.headers.items())      
                    return jsonify("no")
                            


    def getServiceId(self,name,vendor,version):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}  
        my_type =  self.getDBType()
        if my_type == 'sonata':                

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


    def instantiationStatus(self,request):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            print('this SP is a Sonata')
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

            url = sp_host_2 + '/requests/' +  id
            print (url)
            
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            print (response_json)
            #return response_json
            if response.ok:        
                return (response.text, response.status_code, response.headers.items()) 


        if my_type == 'osm':
            print('this SP is a OSM')   
            print('this SP is a OSM')
            sp_host_0 = self.getDBHost()
            print (sp_host_0)
            sp_host = sp_host_0.__str__()
            print (sp_host)
            sp_host_1 = sp_host[4:]
            print ("sp1 es: ")
            print (sp_host_1)
            sp_host_2 = sp_host_1[:-10]
            print ("sp2 es: ")
            print (sp_host_2)
            sp_host_3 = sp_host_2[7:]
            print ("sp3 es: ")
            print (sp_host_3)            
            url = sp_host_3    


            token = self.getOSMToken(request)
            print (token)

            content = request.get_json()
            ns_id = content['ns_id']
            print (ns_id)            
            
            url = sp_host_2 + ':9999/osm/nslcm/v1/ns_instances'
            url_2 = url.replace("http","https")
            print (url_2)

            
            status_ns = "curl  --insecure -w \"%{http_code}\" -H \"Content-type: application/yaml\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            status_ns_2 = status_ns +token + "\" "
            status_ns_3 = status_ns_2 + " " + url_2 + "/" + ns_id          
            print (status_ns_3)

            status = subprocess.check_output([status_ns_3], shell=True)
            return (status)       

          


    def instantiationsStatus(self):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            print('this SP is a Sonata')
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

            url = sp_host_2 + '/requests'  
            print (url)
            
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            print (response_json)
            #return response_json
            if response.ok:        
                return (response.text, response.status_code, response.headers.items())

            #print("status")
            #return "status"
        if my_type == 'osm':
            print('this SP is a OSM')
            sp_host_0 = self.getDBHost()
            print (sp_host_0)
            sp_host = sp_host_0.__str__()
            print (sp_host)
            sp_host_1 = sp_host[4:]
            print ("sp1 es: ")
            print (sp_host_1)
            sp_host_2 = sp_host_1[:-10]
            print ("sp2 es: ")
            print (sp_host_2)
            sp_host_3 = sp_host_2[7:]
            print ("sp3 es: ")
            print (sp_host_3)            
            url = sp_host_3            
            
            get_status = "osm --hostname " + sp_host_3 + " ns-list"
            print (get_status)
            status = subprocess.check_output([get_status], shell=True)
            return (status)              


    def instantiation(self,request):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            print('this SP is a Sonata')
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
            url = sp_host_2 + '/requests'
            
            print(request.get_json())
            data = request.get_json()
            print(url)
            #upload = requests.post(url, files=files)
            
            #upload = requests.post(url, files=files)
            instantiate = requests.post(url,data,headers=JSON_CONTENT_HEADER) 

            if request.method == 'POST':
                return instantiate.text

        if my_type == 'osm':
            print('this SP is a OSM')  

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

            sp_host_3 = sp_host_2[7:]
            print ("sp3 es: ")
            print (sp_host_3)            

            url = sp_host_3
            print(request.get_json())
            content = request.get_json()
            print(content)


            token = self.getOSMToken(request)
            print (token)
            content = request.get_json()
            print (content)
            print (content['nsd_name'])
            print (content['ns_name'])
            print (content['vim_account'])
            
            url = sp_host_2 + ':9999/osm/nslcm/v1/ns_instances_content'
            url_2 = url.replace("http","https")
            print (url_2)

            print (content['vim_account'])
            vim_id = self.getVimId(content['vim_account'])
            print (vim_id)
            print (content['nsd_name'])
            nsd_id = self.getOSMNsdId(content['nsd_name'])
            print (nsd_id)



            HEADERS = {
                'Accept':'application/json',
                'Content-Type':'application/json', 
                'Authorization':'Bearer ' +token+''                
            }     

            data_inst = {
                'nsdId':''+nsd_id+'',
                'nsName':''+content['ns_name']+'',
                'vimAccountId':''+vim_id+''
            }       
            
            instantiate_nsd = "curl -X POST --insecure -w \"%{http_code}\" -H \"Content-type: application/yaml\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            instantiate_nsd_2 = instantiate_nsd +token + "\" "
            instantiate_nsd_3 = instantiate_nsd_2 + " --data \"" + str(data_inst) + "\""
            instantiate_nsd_4 = instantiate_nsd_3 + " " + url_2
            print (instantiate_nsd_4)

            inst = subprocess.check_output([instantiate_nsd_4], shell=True)
            return (inst)
           




    def instantiationDelete(self,request):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            print('this SP is a Sonata')

            print('this SP is a Sonata')
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
            url = sp_host_2 + '/requests'
            
            print(request.get_json())
            data = request.get_json()
            print(url)
            #upload = requests.post(url, files=files)
            
            #upload = requests.post(url, files=files)
            terminate = requests.post(url,data,headers=JSON_CONTENT_HEADER) 

            if request.method == 'POST':
                return terminate.text

        if my_type == 'osm':
            print('this SP is a OSM')  

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

            sp_host_3 = sp_host_2[7:]
            print ("sp3 es: ")
            print (sp_host_3)            

            url = sp_host_3
            print(request.get_json())
            print(url)
            



            token = self.getOSMToken(request)
            print (token)
            content = request.get_json()


            url = sp_host_2 + ':9999/osm/nslcm/v1/ns_instances_content'
            url_2 = url.replace("http","https")
            print (url_2)


            print (content['ns_id'])
            ns_id = content['ns_id']
            print (ns_id)

            
            delete_ns = "curl -X DELETE --insecure -w \"%{http_code}\" -H \"Content-type: application/yaml\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            delete_ns_2 = delete_ns +token + "\" "
            delete_ns_3 = delete_ns_2 + " " + url_2 + "/" + ns_id          
            print (delete_ns_3)

            terminate = subprocess.check_output([delete_ns_3], shell=True)
            return (terminate)            

            
            
            
            #delete_ns = "osm --hostname " + sp_host_3 + " ns-delete " + data['ns_name']
            #print (delete_ns)
            #delete = subprocess.check_output([delete_ns], shell=True)
            #return (delete)                            


    def getOSMToken(self,request):            
        #JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        JSON_CONTENT_HEADER = {'Accept':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'osm':
            print('this SP is a OSM')

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
            #url = sp_host_2 + '/requests'
            url = sp_host_2 + ':9999/osm/admin/v1/tokens'
            url_2 = url.replace("http","https")

            print (url_2)

            print(request.get_json())
            data = request.get_json()
            print(url_2)
            print (data)
            #print (data['nsd_name'])
            print (data['username'])
            print (data['password'])
            print (data['project_id'])

            username_for_token = data['username']
            password_for_token = data['password']
            project_id_for_token = data['project_id']
            
            admin_data = "{username: 'admin', password: 'admin', project_id: 'admin'}"
            print (admin_data)

            get_token = requests.post(url_2,data=data,headers=JSON_CONTENT_HEADER,verify=False)
            print (get_token.text)
            print (get_token.content)
            token_id = get_token.json()
            print (token_id['id'])

            upd_tok = self.updateToken(token_id['id'])

            print (upd_tok)

            return token_id['id']




    def getVims(self):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            print('this SP is a Sonata')
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

            url = sp_host_2 + '/requests'  
            print (url)
            return url

        if my_type == 'osm':
            print('this SP is a OSM')
            sp_host_0 = self.getDBHost()
            print (sp_host_0)
            sp_host = sp_host_0.__str__()
            print (sp_host)
            sp_host_1 = sp_host[4:]
            print ("sp1 es: ")
            print (sp_host_1)
            sp_host_2 = sp_host_1[:-10]
            print ("sp2 es: ")
            print (sp_host_2)
            sp_host_3 = sp_host_2[7:]
            print ("sp3 es: ")
            print (sp_host_3)            
            url = sp_host_3            
            
            get_vims = "osm --hostname " + sp_host_3 + " vim-list"
            print (get_vims)
            vims = subprocess.check_output([get_vims], shell=True)
            return (vims)              

             
    def getVim(self,vim):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            print('this SP is a Sonata')
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

            url = sp_host_2 + '/requests'  
            print (url)
            return url

        if my_type == 'osm':
            print('this SP is a OSM')
            sp_host_0 = self.getDBHost()
            print (sp_host_0)
            sp_host = sp_host_0.__str__()
            print (sp_host)
            sp_host_1 = sp_host[4:]
            print ("sp1 es: ")
            print (sp_host_1)
            sp_host_2 = sp_host_1[:-10]
            print ("sp2 es: ")
            print (sp_host_2)
            sp_host_3 = sp_host_2[7:]
            print ("sp3 es: ")
            print (sp_host_3)            
            url = sp_host_3            
            
            get_vim = "osm --hostname " + sp_host_3 + " vim-show " + vim
            print (get_vim)
            vim_info = subprocess.check_output([get_vim], shell=True)
            return jsonify(vim_info) 
   


    def getVimId(self,vim):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            print('this SP is a Sonata')
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

            url = sp_host_2 + '/requests'  
            print (url)
            return url

        if my_type == 'osm':
            print('this SP is a OSM')
            sp_host_0 = self.getDBHost()
            print (sp_host_0)
            sp_host = sp_host_0.__str__()
            print (sp_host)
            sp_host_1 = sp_host[4:]
            print ("sp1 es: ")
            print (sp_host_1)
            sp_host_2 = sp_host_1[:-10]
            print ("sp2 es: ")
            print (sp_host_2)
            sp_host_3 = sp_host_2[7:]
            print ("sp3 es: ")
            print (sp_host_3)            
            url = sp_host_3            
            
            get_vim = "osm --hostname " + sp_host_3 + " vim-show " + vim
            print (get_vim)
            vim_info = subprocess.check_output([get_vim], shell=True)
            print (vim_info)
            
            print (type(vim_info))    


            s = json.dumps(str(vim_info))

            print(s)
            print (type(s))                 
            
            print ("ILLO")
            start = s.find('_id')
            end = s.find('\\\" ', start)
            print (s[start+20:end])
            vim_id = s[start+20:end]
            print ("ILLO")
            return vim_id




    def getOSMNsdId(self,nsd_name):    

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'osm':
            print('this SP is a OSM')
            sp_host_0 = self.getDBHost()
            print (sp_host_0)
            sp_host = sp_host_0.__str__()
            print (sp_host)
            sp_host_1 = sp_host[4:]
            print ("sp1 es: ")
            print (sp_host_1)
            sp_host_2 = sp_host_1[:-10]
            print ("sp2 es: ")
            print (sp_host_2)
            sp_host_3 = sp_host_2[7:]
            print ("sp3 es: ")
            print (sp_host_3)            
            url = sp_host_3            
            
            get_nsd = "osm --hostname " + sp_host_3 + "  nsd-show " + nsd_name
            print (get_nsd)
            nsd_info = subprocess.check_output([get_nsd], shell=True)
            print (nsd_info)
            
            print (type(nsd_info))    


            s = json.dumps(str(nsd_info))

            print(s)
            print (type(s))   
                
            
            print ("ILLO")
            start = s.find('_id')
            end = s.find('\\\" ', start)
            print (s[start+21:end])
            vim_id = s[start+21:end]
            print ("ILLO")



            return vim_id            