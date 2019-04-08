#!/usr/bin/python

from flask import Flask, request, jsonify, render_template
import os, sys, logging, uuid, json
#from werkzeug import secure_filename

#import serviceplatform
import psycopg2
import requests
import subprocess
import models.database as database
import re
import ast
from ast import literal_eval
import yaml
import time
from threading import Thread
import threading 
from _thread import start_new_thread
import _thread
import logging

FILE = "db-config.cfg"

class Adapter:

    def __init__(self, name):
        self.name = name
        self.host = "host"
        self.type = "type" 
        logging.getLogger().setLevel(logging.DEBUG)        

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
            #print (self.name)
            logging.info(self.name)
            get_type = "SELECT type FROM service_platforms WHERE name=\'" +self.name+ "\'"
            logging.info(get_type)
            #print (get_type)            
            update_token = "UPDATE service_platforms SET service_token = \'" +token+ "\' WHERE name = \'" +self.name+ "\'"            
            #print (update_token)
            logging.info(update_token)
            cursor.execute(update_token)
            connection.commit()
            return "token updated", 200    
        except (Exception, psycopg2.Error) as error :
            print (error)
            logging.error(error)
            exception_message = str(error)
            return exception_message, 401
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    #print("PostgreSQL connection is closed")         
                    logging.info("PostgreSQL connection is closed")



    def getDBType(self):
        logging.info("getdbtype starts")
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
            #print (get_type)
            cursor.execute(get_type)
            all = cursor.fetchall()
            #return jsonify(all), 200 
            type_0 = all.__str__()
            #print(type_0)
            type_1 = type_0[3:]            
            #print(type_1)            
            type_2 = type_1[:-4]            
            #print(type_2)                  
            return type_2
        except (Exception, psycopg2.Error) as error :
            #print (error)
            logging.error(error)
            exception_message = str(error)
            return exception_message, 401
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed") 




    def getDBUserName(self):
        logging.info("getdbusername starts")
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
            get_username = "SELECT username FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_username)
            cursor.execute(get_username)
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
            #print (error)
            logging.error(error)
            exception_message = str(error)
            return exception_message, 401
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")


    def getDBProjectName(self):
        logging.info("getprojectname starts")
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
            get_project_name = "SELECT project_name FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_project_name)
            cursor.execute(get_project_name)
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
            #print (error)
            logging.error(error)
            exception_message = str(error)
            return exception_message, 401
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")                    


    def getDBPassword(self):
        logging.info("get password starts")
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
            get_password= "SELECT password FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_password)
            cursor.execute(get_password)
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
            #print (error)
            logging.error(error)
            exception_message = str(error)
            return exception_message, 401
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")      


    def getDBProject(self):
        logging.info("get project starts")
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
            get_password= "SELECT project_name FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_password)
            cursor.execute(get_password)
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
            #print (error)
            logging.error(error)
            exception_message = str(error)
            return exception_message, 401
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")                                    




    def getDBHost(self):
        logging.info("get dbhost starts")
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
            #print (error)
            logging.error(error)
            exception_message = str(error)
            return exception_message, 401
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed") 


    def getMonitoringURLs(self):
        logging.info("get monitoring urls starts")
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
            get_type = "SELECT monitoring_urls FROM service_platforms WHERE name=\'" +self.name+ "\'"
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
            #print (error)
            logging.error(error)
            exception_message = str(error)
            return exception_message, 401
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")                     


    def getPackages(self):    
        logging.info("get packages starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()
        if my_type == 'sonata':               

            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)
            logging.info(sp_host_2)

            url = sp_host_2 + ':32002/api/v3/packages'
            #url = sp_url + '/packages'
            response = requests.get(url, headers=JSON_CONTENT_HEADER)    
            if response.ok:        
                    #return (response.text, response.status_code, response.headers.items()) 
                    logging.info(response)                    
                    logging.debug(response.text.__str__())
                    return response.text
        if my_type == 'osm': 
            return "osm packages"



    def getPackage(self,name,vendor,version):    
        logging.info("get package starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'} 

        my_type =  self.getDBType()
        if my_type == 'sonata':    
            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            url = sp_host_2 + ':32002/api/v3/packages'  
            #print (name,vendor,version)
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            jjson = json.loads(response_json)
            pkg = [x for x in jjson if x['pd']['name'] == name and x['pd']['vendor'] == vendor and x['pd']['version'] == version]
            
            if response.ok: 
                    #print(pkg)
                    logging.debug(pkg)
                    return jsonify(pkg)

    def deletePackage(self,name,vendor,version):    
        logging.info("delete package starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   

        my_type =  self.getDBType()
        if my_type == 'sonata':    
            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            url = sp_host_2 + ':32002/api/v3/packages'  
            #print (name,vendor,version)
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            jjson = json.loads(response_json)
            pkg = [x for x in jjson if x['pd']['name'] == name and x['pd']['vendor'] == vendor and x['pd']['version'] == version]
            
            if pkg:

                #print(pkg)
                logging.info (pkg)
                #uuid_to_delete = pkg['pd']['uuid']
                #uuid_to_delete_1 = [uuid for x in jjson if x['pd']['name'] == name and x['pd']['vendor'] == vendor and x['pd']['version'] == version]
                uuid_to_delete_1 = [obj['uuid'] for obj in jjson if(obj['pd']['name'] == name)]            
                #print(uuid_to_delete_1)
                uuid_0 = uuid_to_delete_1.__str__()
                uuid_to_delete_2 = uuid_0[2:]
                #print(uuid_to_delete_2)
                uuid_to_delete_3 = uuid_to_delete_2[:-2]
                #print(uuid_to_delete_3)

                url_for_delete = url + '/' + uuid_to_delete_3
                #print (url_for_delete)
                logging.debug(url_for_delete)
                delete = requests.delete(url_for_delete, headers=JSON_CONTENT_HEADER)

            if response.ok:                 
                    logging.debug(delete.text)
                    return (delete.text, delete.status_code, delete.headers.items())
                    



    def getPackagebyId(self,name,vendor,version):    
        logging.info("get package id starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'} 
        
        my_type =  self.getDBType()
        if my_type == 'sonata':              

            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            url = sp_host_2 + ':32002/api/v3/packages'  
            #print (name,vendor,version)
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            jjson = json.loads(response_json)
            pkg = [x for x in jjson if x['pd']['name'] == name and x['pd']['vendor'] == vendor and x['pd']['version'] == version]
            
            if pkg:
                #print(pkg)
                logging.info(pkg)
                #uuid_to_delete = pkg['pd']['uuid']
                #uuid_to_delete_1 = [uuid for x in jjson if x['pd']['name'] == name and x['pd']['vendor'] == vendor and x['pd']['version'] == version]
                uuid_to_delete_1 = [obj['uuid'] for obj in jjson if(obj['pd']['name'] == name)]            
                #print(uuid_to_delete_1)
                uuid_0 = uuid_to_delete_1.__str__()
                uuid_to_delete_2 = uuid_0[2:]
                #print(uuid_to_delete_2)
                uuid_to_delete_3 = uuid_to_delete_2[:-2]
                #print(uuid_to_delete_3)

                url_for_delete = url + '/' + uuid_to_delete_3
                #print (url_for_delete)
                delete = requests.get(url_for_delete, headers=JSON_CONTENT_HEADER)

            if response.ok:                 
                    logging.debug(delete.text)
                    return (delete.text, delete.status_code, delete.headers.items())                

                

                



    def uploadPackage(self,package):
        logging.info("upload package starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()
        if my_type == 'sonata':               

            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)
            url = sp_host_2 + ':32002/api/v3/packages'
            
            #print(package)
            logging.info(package)
            #print(url)
            logging.info(url)

            files = {'package': open(package,'rb')}
            upload = requests.post(url, files=files)

            if request.method == 'POST':
                logging.debug(upload.text)
                return upload.text


        if my_type == 'onap':               

            #sp_host_0 = self.getDBHost()
            print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            print ("sp1 es: ")
            print (sp_host_1)
            sp_host_2 = sp_host_1[:-10]
            print ("sp2 es: ")
            print (sp_host_2)
            url = sp_host_2 + '/sdc/v1/catalog/services/{uuid}/resourceInstances/{resourceInstanceNormalizedName}/artifacts'
            
            print(package)
            print(url)

            files = {'package': open(package,'rb')}
            upload = requests.post(url, files=files)

            if request.method == 'POST':
                return upload.text





    def uploadOSMService(self,request): 
        #JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        logging.info("upload osm service starts")
        my_type =  self.getDBType()
        if my_type == 'osm':               

            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            sp_host_3 = sp_host_2[7:]
            #print ("sp3 es: ")
            #print (sp_host_3)            


            content = request.get_json()
            #print ("request content:")
            #print (content)
            logging.info(content)
            

            token = self.getOSMToken(request)
            #print (token)
            logging.debug(token)
            file_to_upload = content['service']
            #print ("File to upload")
            #print (file_to_upload)
            file_composed = "@" + file_to_upload
            #print (file_composed)

            #file = {'file': open(file_to_upload, 'rb')}
            file = {'nsd-create': open(file_to_upload, 'rb')}
            
            #print (file)
            data = {'service':file_to_upload}
            #data = request.get_json()
            #print (data)

            HEADERS = {
                'Accept':'application/yaml',
                'Content-Type':'application/zip', 
                'Authorization':'Bearer ' +token+''                
            }
            print (HEADERS)

            #url = sp_host_2 + ':9999/osm/nsd/v1/ns_descriptors_content'
            url = sp_host_2 + ':9999/osm/nsd/v1/ns_descriptors'
            url_2 = url.replace("http","https")
            #print (url_2)
            
            #upload_nsd = "curl -X POST --insecure -w \"%{http_code}\" -H \"Content-type: application/zip\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            upload_nsd = "curl -X POST --insecure -H \"Content-type: application/yaml\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            upload_nsd_2 = upload_nsd +token + "\" "
            upload_nsd_3 = upload_nsd_2 + " --data-binary "
            upload_nsd_4 = upload_nsd_3 + "\"@" +file_to_upload+ "\" " + url_2
            #print (upload_nsd_4)
            logging.debug(upload_nsd_4)
            upload = subprocess.check_output([upload_nsd_4], shell=True)

            #if content['callback']:
            #    _thread.start_new_thread(self.OSMUploadServiceCallback, (token,url_2,content['callback'],upload))
            try:
                callback_url = content['callback']
                logging.debug("Callback url specified")
                _thread.start_new_thread(self.OSMUploadServiceCallback, (token,url_2,callback_url,upload))
            except:
                logging.debug("No callback url specified")

            logging.debug(upload)
            return (upload)

      

    def uploadOSMFunction(self,request):
        logging.info("upload osm function starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()
        if my_type == 'osm':               

            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            sp_host_3 = sp_host_2[7:]
            #print ("sp3 es: ")
            #print (sp_host_3)            

            
            token = self.getOSMToken(request)
            #print (token)
            logging.debug(token)
            content = request.get_json()
            file_to_upload = content['function']
            #url = sp_host_2 + ':9999/osm/vnfpkgm/v1/vnf_packages_content'
            url = sp_host_2 + ':9999/osm/vnfpkgm/v1/vnf_packages'
            url_2 = url.replace("http","https")
            #print (url_2)
            
            upload_nsd = "curl -X POST --insecure -H \"Content-type: application/yaml\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            upload_nsd_2 = upload_nsd +token + "\" "
            upload_nsd_3 = upload_nsd_2 + " --data-binary "
            upload_nsd_4 = upload_nsd_3 + "\"@" +file_to_upload+ "\" " + url_2
            logging.debug(upload_nsd_4)
            upload = subprocess.check_output([upload_nsd_4], shell=True)
            #return jsonify(upload_nsd_4) 

            #if content['callback']:
            #    _thread.start_new_thread(self.OSMUploadFunctionCallback, (token,url_2,content['callback'],upload))
            try:
                callback_url = content['callback']
                logging.debug ("Callback url specified")
                _thread.start_new_thread(self.OSMUploadServiceCallback, (token,url_2,callback_url,upload))
            except:
                logging.debug ("No callback url specified")                

            return (upload) 



    def getServices(self):    
        logging.info("get services starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}  
        my_type =  self.getDBType()        
        print (my_type)
        if my_type == 'sonata':                        
 
            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            url = sp_host_2 + ':32002/api/v3/services'
            logging.debug (url)
            #url = sp_url + '/packages'
            response = requests.get(url, headers=JSON_CONTENT_HEADER)    
            if response.ok:        
                    logging.debug(response.text)
                    return (response.text, response.status_code, response.headers.items()) 

        if my_type == 'osm':                

            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)
            sp_host_3 = sp_host_2[7:]
            #print ("sp3 es: ")
            #print (sp_host_3)            

            #url = sp_host_2 + ':32002/api/v3/services'
            #get_nsd_list = "osm --hostname " + sp_host_3 + " nsd-list"
            #print (get_nsd_list)
            #get = os.system(get_nsd_list).__str__()    
            #return get
            #get = subprocess.check_output([get_nsd_list], shell=True)
            #return (get)

    
            token = self.getOSMToken(request)
            #print (token)
            logging.debug(token)
            url = sp_host_2 + ':9999/osm/nsd/v1/ns_descriptors'
            url_2 = url.replace("http","https")
            logging.debug (url_2)
            
            services_nsd = "curl --insecure -w \"%{http_code}\" -H \"Content-type: application/zip\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            services_nsd_2 = services_nsd +token + "\" "  + url_2
            logging.debug (services_nsd_2)
            services = subprocess.check_output([services_nsd_2], shell=True)
            #return jsonify(upload_nsd_4) 
            logging.debug(services)
            return (services) 




            

    def getFunctions(self):    
        logging.info("get functions starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}  
        my_type =  self.getDBType()
        if my_type == 'sonata':                

            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            url = sp_host_2 + ':32002/api/v3/functions'
            #url = sp_url + '/packages'
            response = requests.get(url, headers=JSON_CONTENT_HEADER)    
            if response.ok:        
                    logging.debug(response.text)
                    return (response.text, response.status_code, response.headers.items()) 

        if my_type == 'osm':                

            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)
            sp_host_3 = sp_host_2[7:]
            #print ("sp3 es: ")
            #print (sp_host_3)            

            token = self.getOSMToken(request)
            logging.debug (token)
            url = sp_host_2 + ':9999/osm/vnfpkgm/v1/vnf_packages'
            url_2 = url.replace("http","https")
            logging.debug (url_2)
            
            functions_vnfd = "curl --insecure -w \"%{http_code}\" -H \"Content-type: application/zip\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            functions_vnfd_2 = functions_vnfd +token + "\" "  + url_2
            logging.debug (functions_vnfd_2)
            functions = subprocess.check_output([functions_vnfd_2], shell=True)
            logging.debug(functions)
            return (functions)          






    def getService(self,name,vendor,version):    
        logging.info("get service starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}  

        my_type =  self.getDBType()
        if my_type == 'sonata':                

            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            url = sp_host_2 + ':32002/api/v3/services'  
            #print (name,vendor,version)
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            jjson = json.loads(response_json)
            pkg = [x for x in jjson if x['nsd']['name'] == name and x['nsd']['vendor'] == vendor and x['nsd']['version'] == version]
            
            if response.ok: 
                    logging.debug(pkg)
                    return jsonify(pkg)     

    def getServiceInstantiations(self,name,vendor,version):    
        logging.info("get service instantiations starts")

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}  

        my_type =  self.getDBType()
        if my_type == 'sonata':                

            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            url = sp_host_2 + ':32002/api/v3/requests'  
            #print (name,vendor,version)
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content

            logging.debug (response_json)

            jjson = json.loads(response.content)
            logging.debug (jjson)

            idd = print (jjson[0]['service']['uuid'])
            idd = print (jjson[0]['service']['name'])
            idd = print (jjson[1]['service']['uuid'])
            idd = print (jjson[1]['service']['name'])            

            
            N = 0
            for N in range(10000):
                print (jjson['service']['uuid'])

                N = N + 1
                print (N)


            if response.ok:            
                return jsonify("no")
                            


    def getServiceId(self,name,vendor,version):    
        logging.info("get service id starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}  
        my_type =  self.getDBType()
        if my_type == 'sonata':                

            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            url = sp_host_2 + ':32002/api/v3/services'  
            #print (name,vendor,version)
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            logging.debug (response_json)
            jjson = json.loads(response_json)
            pkg = [x for x in jjson if x['nsd']['name'] == name and x['nsd']['vendor'] == vendor and x['nsd']['version'] == version]
            
            if pkg:

                logging.debug(pkg)
                uuid_to_delete_1 = [obj['uuid'] for obj in jjson if(obj['nsd']['name'] == name)]            
                logging.debug(uuid_to_delete_1)
                uuid_0 = uuid_to_delete_1.__str__()
                uuid_to_delete_2 = uuid_0[2:]
                print(uuid_to_delete_2)
                uuid_to_delete_3 = uuid_to_delete_2[:-2]
                #print(uuid_to_delete_3)
                url_for_delete = url + '/' + uuid_to_delete_3
                #print (url_for_delete)
                delete = requests.get(url_for_delete, headers=JSON_CONTENT_HEADER)
        
            if response.ok:                                        
                    logging.debug(uuid_to_delete_3)
                    return uuid_to_delete_3


    def getPackageId(self,name,vendor,version):    
        logging.info("get package id starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}  
        my_type =  self.getDBType()
        if my_type == 'sonata':                

            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            url = sp_host_2 + ':32002/api/v3/packages'  
            #print (name,vendor,version)
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            logging.debug (response_json)
            jjson = json.loads(response_json)
            pkg = [x for x in jjson if x['pd']['name'] == name and x['pd']['vendor'] == vendor and x['pd']['version'] == version]
            
            if pkg:

                logging.debug(pkg)
                uuid_to_delete_1 = [obj['uuid'] for obj in jjson if(obj['pd']['name'] == name)]            
                #print(uuid_to_delete_1)
                uuid_0 = uuid_to_delete_1.__str__()
                uuid_to_delete_2 = uuid_0[2:]
                #print(uuid_to_delete_2)
                uuid_to_delete_3 = uuid_to_delete_2[:-2]
                #print(uuid_to_delete_3)
                url_for_delete = url + '/' + uuid_to_delete_3
                #print (url_for_delete)
                delete = requests.get(url_for_delete, headers=JSON_CONTENT_HEADER)
        
            if response.ok:                                        
                    logging.debug(uuid_to_delete_3)
                    return uuid_to_delete_3



    def getPackageFile(self,pkg_id):    
        logging.info("get package file starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}  
        my_type =  self.getDBType()
        if my_type == 'sonata':                

            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            url = sp_host_2 + ':32002/api/v3/packages'  
            url_2 = url + "/" + pkg_id + "/package-file --output temp-file.tgo"
            logging.debug(url_2)
            

            response = requests.get(url_2,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            logging.debug (response_json)
            #return response_json
            if response.ok:    
                logging.debug(response.text)    
                return (response.text, response.status_code, response.headers.items())                  



    def instantiationStatus(self,request):    
        logging.info("instantiation status starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            #print('this SP is a Sonata')
            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            ##sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            ##sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            #url = sp_host_2 + ':32002/api/v3/requests/' +  id
            url = sp_host_2 + ':32002/api/v3/requests/' +  request
            logging.debug (url)
            
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            logging.debug (response_json)
            #return response_json
            if response.ok:        
                logging.debug(response.text)
                return (response.text)


        if my_type == 'osm':
            #print('this SP is a OSM')   
            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)
            sp_host_3 = sp_host_2[7:]
            #print ("sp3 es: ")
            #print (sp_host_3)            
            url = sp_host_3    


            token = self.getOSMToken(request)
            logging.debug (token)

            #content = request.get_json()
            #ns_id = content['ns_id']
            ns_id = request
            logging.debug (ns_id)            
            
            url = sp_host_2 + ':9999/osm/nslcm/v1/ns_instances'
            url_2 = url.replace("http","https")
            logging.debug (url_2)

            
            status_ns = "curl  --insecure  -H \"Content-type: application/yaml\"  -H \"Accept: application/json\" -H \"Authorization: Bearer "
            status_ns_2 = status_ns +token + "\" "
            status_ns_3 = status_ns_2 + " " + url_2 + "/" + ns_id          
            logging.debug (status_ns_3)

            status = subprocess.check_output([status_ns_3], shell=True)
            status = subprocess.check_output([status_ns_3], shell=True)
            logging.debug (status)
            return (status)       

          


    def instantiationsStatus(self):    
        logging.info("instantatiations status starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            #print('this SP is a Sonata')
            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            url = sp_host_2 + ':32002/api/v3/requests'  
            logging.debug (url)
            
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            logging.debug (response_json)
            #return response_json
            if response.ok: 
                logging.debug(response.text)       
                return (response.text, response.status_code, response.headers.items())

            #print("status")
            #return "status"
        if my_type == 'osm':
            #print('this SP is a OSM')
            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)
            sp_host_3 = sp_host_2[7:]
            #print ("sp3 es: ")
            #print (sp_host_3)            
            url = sp_host_3            
            

            token = self.getOSMToken(request)
            logging.debug (token)
            url = sp_host_2 + ':9999/osm/nslcm/v1/ns_instances'
            url_2 = url.replace("http","https")
            logging.debug (url_2)
            
            #instances_1 = "curl --insecure -w \"%{http_code}\" -H \"Content-type: application/json\"  -H \"Accept: application/json\" -H \"Authorization: Bearer "
            instances_1 = "curl --insecure -H \"Content-type: application/json\"  -H \"Accept: application/json\" -H \"Authorization: Bearer "                    
            instances_2 = instances_1 +token + "\" "  + url_2
            logging.debug (instances_2)
            
            ns_instances = subprocess.check_output([instances_2], shell=True)
            ns_instances = subprocess.check_output([instances_2], shell=True)
            #return jsonify(upload_nsd_4) 
            return (ns_instances)         



    def instantiation(self,request):    
        logging.info("instantiation starts")
        print ("INSTANTIATION FUNCTION BEGINS")
        print (request)
        request_str = request.__str__()
        #print (request['service_uuid'])
        #print (request['name'])
        logging.debug (request_str)
        JSON_CONTENT_HEADER = {'content-Type':'application/json'}   
        my_type =  self.getDBType()


        if my_type == 'onap':
            print('this SP is ONAP')
            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            print ("sp2 es: ")
            print (sp_host_2)
            url = sp_host_2 + '}/serviceInstances/v4'
            print (url)

            #print(request.get_json())
            #data = request.get_json()
            print(request_str.get_json())
            data = request_str.get_json()
            print(url)
            print (data)
            instantiate = requests.post( url, data=json.dumps(data), headers=JSON_CONTENT_HEADER)            
            print (instantiate)
            if request.method == 'POST':
                return instantiate.text            


        if my_type == 'sonata':
            #print('this SP is a Sonata')
            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)
            url = sp_host_2 + ':32002/api/v3/requests'
            #print (url)
            
            #print(request.get_json())
            #data = request.get_json()            
            #data = json.dumps(request)
            logging.debug(url)
            #print (data)
            #upload = requests.post(url, files=files)
            
            #upload = requests.post(url, files=files)
            #instantiate = requests.post(url,data,headers=JSON_CONTENT_HEADER)
            #instantiate = requests.post( url, data=json.dumps(data), headers=JSON_CONTENT_HEADER)           
            instantiate = requests.post( url, data=request, headers=JSON_CONTENT_HEADER)           
            
            logging.debug ("THIS IS THE INSTANTIATE RESPONSE:")
            logging.debug (instantiate)
            #print (" - ")
            #if data['callback']:
            #    _thread.start_new_thread(self.SonataInstantiateCallback, (url,data['callback'],instantiate))
            #if request.method == 'POST':
            #    return instantiate.text
            logging.debug (instantiate.text)
            return instantiate.text

        if my_type == 'osm':
            print('this SP is a OSM')  

            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            sp_host_3 = sp_host_2[7:]
            #print ("sp3 es: ")
            #print (sp_host_3)            

            url = sp_host_3
            #print(request.get_json())
            content = request.get_json()
            logging.debug(content)


            token = self.getOSMToken(request)
            logging.debug (token)
            content = request.get_json()
            #print (content)
            #print (content['nsd_name'])
            #print (content['ns_name'])
            #print (content['vim_account'])
            
            url = sp_host_2 + ':9999/osm/nslcm/v1/ns_instances_content'
            url_2 = url.replace("http","https")
            logging.debug (url_2)

            #print (content['vim_account'])
            vim_id = self.getVimId(content['vim_account'])
            logging.debug (vim_id)
            logging.debug (content['nsd_name'])
            nsd_id = self.getOSMNsdId(content['nsd_name'])
            logging.debug (nsd_id)



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
            
            #instantiate_nsd = "curl -X POST --insecure -w \"%{http_code}\" -H \"Content-type: application/yaml\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            instantiate_nsd = "curl -X POST --insecure -H \"Content-type: application/yaml\"  -H \"Accept: application/json\" -H \"Authorization: Bearer "                
            instantiate_nsd_2 = instantiate_nsd +token + "\" "
            instantiate_nsd_3 = instantiate_nsd_2 + " --data \"" + str(data_inst) + "\""
            instantiate_nsd_4 = instantiate_nsd_3 + " " + url_2
            logging.debug (instantiate_nsd_4)



            

            inst = subprocess.check_output([instantiate_nsd_4], shell=True)

            #if content['callback']:
            #    _thread.start_new_thread(self.OSMInstantiateCallback, (token,url_2,content['callback'],inst))
            try:
                callback_url = content['callback']
                logging.debug ("Callback url specified")
                _thread.start_new_thread(self.OSMUploadServiceCallback, (token,url_2,callback_url,inst))
            except:
                logging.debug ("No callback url specified")                

            #inst = subprocess.check_output([instantiate_nsd_4], shell=True)
            logging.debug(inst)
            return (inst)




    def instantiationDelete(self,request):    
        logging.info("instantiation delete starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()


        if my_type == 'onap':
            #print('this SP is ONAP')
            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)
            url = sp_host_2
            #print (url)


            content = request.get_json()

            #print (content['ns_instance_id'])
            ns_instance_id = content['ns_instance_id']
            logging.debug (ns_instance_id) 



            url_2 = url + '/ns/' + ns_instance_id
            logging.debug (url_2)                    
            
            #upload = requests.post(url, files=files)
            terminate = requests.delete(url_2,headers=JSON_CONTENT_HEADER) 

            if request.method == 'POST':
                logging.debug(terminate.text)
                return terminate.text


        if my_type == 'sonata':
            #print('this SP is a Sonata')
            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)
            url = sp_host_2 + ':32002/api/v3/requests'
            
            #print(request.get_json())
            #data = request.get_json()
            logging.debug(url)
            logging.debug (request)
            #print (data)
            #print ("datadatadatadatadata")

            terminate = requests.post(url,data=request,headers=JSON_CONTENT_HEADER) 
            logging.debug (terminate)
            logging.debug (terminate.text)
            return terminate.text

        if my_type == 'osm':
            #print('this SP is a OSM')  

            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            sp_host_3 = sp_host_2[7:]
            #print ("sp3 es: ")
            #print (sp_host_3)            

            url = sp_host_3
            logging.debug(request.get_json())
            logging.debug(url)
            



            token = self.getOSMToken(request)
            logging.debug (token)
            content = request.get_json()


            url = sp_host_2 + ':9999/osm/nslcm/v1/ns_instances_content'
            url_2 = url.replace("http","https")
            #print (url_2)


            #print (content['ns_id'])
            ns_id = content['ns_id']
            logging.debug (ns_id)

            
            #delete_ns = "curl -X DELETE --insecure -w \"%{http_code}\" -H \"Content-type: application/yaml\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            delete_ns = "curl -X DELETE --insecure -H \"Content-type: application/yaml\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            delete_ns_2 = delete_ns +token + "\" "
            delete_ns_3 = delete_ns_2 + " " + url_2 + "/" + ns_id          
            logging.debug (delete_ns_3)

            terminate = subprocess.check_output([delete_ns_3], shell=True)

            #if content['callback']:
            #    _thread.start_new_thread(self.OSMTerminateCallback, (token,url_2,content['callback'],content['ns_id']))
            try:
                callback_url = content['callback']
                logging.debug ("Callback url specified")
                _thread.start_new_thread(self.OSMUploadServiceCallback, (token,url_2,callback_url,content['ns_id']))
            except:
                logging.debug ("No callback url specified")                 
                
            logging.debug(terminate)
            return (terminate)            

                        


    def getOSMToken(self,request):        
        logging.info("get osm token starts")    
        #JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        JSON_CONTENT_HEADER = {'Accept':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'osm':
            print('this SP is a OSM')

            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)
            #url = sp_host_2 + '/requests'
            url = sp_host_2 + ':9999/osm/admin/v1/tokens'
            url_2 = url.replace("http","https")

            logging.debug (url_2)

            #print(request.get_json())
            #data = request.get_json()
            #print(url_2)
            #print (data)
            #print (data['nsd_name'])
            #print (data['username'])
            #print (data['password'])
            #print (data['project_id'])


            pr_name = self.getDBProjectName()
            logging.debug ("project name from DB:")
            logging.debug (pr_name)

            if pr_name:
                project_id_for_token = pr_name

            if not pr_name:
                data = request.get_json()
                project_id_for_token = data['project_id']
                logging.debug ("project name from json body:")
                logging.debug (pr_name)

            #project_id_for_token = data['project_id']
            logging.debug (project_id_for_token)

            #username_for_token = data['username']
            #password_for_token = data['password']

            username_for_token = self.getDBUserName()
            password_for_token = self.getDBPassword()

            #project_id_for_token = data['project_id']
            
            admin_data = "{username: 'admin', password: 'admin', project_id: 'admin'}"
            logging.debug (admin_data)

            #update_token = "UPDATE service_platforms SET service_token = \'" +token+ "\' WHERE name = \'" +self.name+ "\'" 
            
            data_for_token= "{username: \'" +username_for_token+ "\', password: \'" +password_for_token+ "\', project_id: \'" +project_id_for_token+ "\'}"
            #print (data)
            

            get_token = requests.post(url_2,data=data_for_token,headers=JSON_CONTENT_HEADER,verify=False)
            logging.debug (get_token.text)
            logging.debug (get_token.content)
            token_id = get_token.json()
            #print (token_id['id'])

            #upd_tok = self.updateToken(token_id['id'])

            #print (upd_tok)
            logging.debug(token_id['id'])
            return token_id['id']



    def getWims(self):    
        logging.info("get wims starts")

        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            url = self.getHostIp()  
            logging.debug (url)
            curl_vims = 'curl ' + url + ':32002/api/v3/settings/wims'
            logging.debug (curl_vims)
            vims = subprocess.check_output([curl_vims], shell=True)
            logging.debug(vims)
            return vims



    def getVims(self):    
        logging.info("get vims starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            url = self.getHostIp()  
            logging.debug (url)
            curl_vims = 'curl ' + url + ':32002/api/v3/settings/vims'
            logging.debug (curl_vims)
            vims = subprocess.check_output([curl_vims], shell=True)
            logging.debug(vims)
            return vims

        if my_type == 'osm':
            #print('this SP is a OSM')
            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)
            sp_host_3 = sp_host_2[7:]
            #print ("sp3 es: ")
            #print (sp_host_3)            
            url = sp_host_3            
            
            token = self.getOSMToken(request)
            logging.debug (token)
            url = sp_host_2 + ':9999/osm/admin/v1/vim_accounts'
            url_2 = url.replace("http","https")
            logging.debug (url_2)
            
            vimss = "curl --insecure -w \"%{http_code}\" -H \"Content-type: application/zip\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            vimss_2 = vimss +token + "\" "  + url_2
            logging.debug (vimss_2)
            vims = subprocess.check_output([vimss_2], shell=True)
            #return jsonify(upload_nsd_4) 
            logging.debug(vims)
            return (vims)              


    def getWim(self,vim):    
        logging.info("get wim starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            url = self.getHostIp()  
            logging.debug (url)
            curl_vim = 'curl ' + url + ':32002/api/v3/settings/wims/' + vim
            logging.debug (curl_vim)
            vim = subprocess.check_output([curl_vim], shell=True)
            logging.debug(vim)
            return vim




    def getVim(self,vim):    
        logging.info("get vim starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            url = self.getHostIp()  
            logging.debug (url)
            curl_vim = 'curl ' + url + ':32002/api/v3/settings/vims/' + vim
            logging.debug (curl_vim)
            vim = subprocess.check_output([curl_vim], shell=True)
            logging.debug(vim)
            return vim

        if my_type == 'osm':
            #print('this SP is a OSM')
            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)
            sp_host_3 = sp_host_2[7:]
            #print ("sp3 es: ")
            #print (sp_host_3)            
            url = sp_host_3            
            
    
            token = self.getOSMToken(request)
            logging.debug (token)
            url = sp_host_2 + ':9999/osm/admin/v1/vim_accounts'
            url_2 = url.replace("http","https")
            logging.debug (url_2)
            
            vimss = "curl --insecure -w \"%{http_code}\" -H \"Content-type: application/zip\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            vimss_2 = vimss +token + "\" "  + url_2 + "/" + vim
            logging.debug (vimss_2)
            vims = subprocess.check_output([vimss_2], shell=True)
            #return jsonify(upload_nsd_4) 
            logging.debug(vims)
            return (vims) 
   


    def getVimId(self,vim):    
        logging.info("get vim id starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            #print('this SP is a Sonata')
            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            url = sp_host_2 + ':32002/api/v3/requests'  
            logging.debug (url)
            return url

        if my_type == 'osm':
            #print('this SP is a OSM')
            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)
            sp_host_3 = sp_host_2[7:]
            #print ("sp3 es: ")
            #print (sp_host_3)            
            url = sp_host_3            
            
            get_vim = "osm --hostname " + sp_host_3 + " vim-show " + vim
            logging.debug (get_vim)
            vim_info = subprocess.check_output([get_vim], shell=True)
            logging.debug (vim_info)
            
            logging.debug (type(vim_info))    


            s = json.dumps(str(vim_info))

            logging.debug(s)
            logging.debug (type(s))                 

            start = s.find('_id')
            end = s.find('\\\" ', start)
            logging.debug (s[start+20:end])
            vim_id = s[start+20:end]

            logging.debug(vim_id)
            return vim_id




    def getOSMNsdId(self,nsd_name):    
        logging.info("get osm nsd id starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'osm':
            #print('this SP is a OSM')
            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)
            sp_host_3 = sp_host_2[7:]
            #print ("sp3 es: ")
            #print (sp_host_3)            
            url = sp_host_3            
            
            get_nsd = "osm --hostname " + sp_host_3 + "  nsd-show " + nsd_name
            logging.debug (get_nsd)
            nsd_info = subprocess.check_output([get_nsd], shell=True)
            logging.debug (nsd_info)
            
            print (type(nsd_info))    


            s = json.dumps(str(nsd_info))

            logging.debug(s)
            logging.debug (type(s))                             
            
            start = s.find('_id')
            end = s.find('\\\" ', start)
            #print (s[start+21:end])
            #vim_id = s[start+21:end]
            logging.debug (s[start+21:end])
            vim_id = s[start+21:end]         

            logging.debug(vim_id)
            return vim_id            





    def downloadPackageSonata(self,package_id):
        logging.info("download package sonata starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}                              
        #sp_host_0 = self.getDBHost()
        #print (sp_host_0)
        #sp_host = sp_host_0.__str__()
        #print (sp_host)
        #print (self.getDBHost())
        #sp_host_1 = sp_host[4:]
        #print ("sp1 es: ")
        #print (sp_host_1)
        #sp_host_2 = sp_host_1[:-10]
        sp_host_2 = self.getHostIp()
        #print ("sp2 es: ")
        #print (sp_host_2)
        url = sp_host_2 + ':32002/api/v3/packages'
        
        url2 = 'curl ' + url + '/' + package_id + '/package-file --output /app/packages/' + package_id + '.tgo'
        
        logging.debug(url2)

        download = subprocess.check_output([url2], shell=True)
        #return (download)    
        msg = "Package downloaded to: " + "/app/packages/" + package_id + '.tgo' 
        logging.debug(msg)
        return (msg)

        
        #download = requests.get(url2)
        #if request.method == 'GET':
        #    return download.text




    def deleteOSMService(self,id_to_delete):
            logging.info("delete osm service starts")
            #print('this SP is a OSM')  

            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            sp_host_3 = sp_host_2[7:]
            #print ("sp3 es: ")
            #print (sp_host_3)            

            url = sp_host_3


            token = self.getOSMTokenForDelete()
            logging.debug (token)

           

            url = sp_host_2 + ':9999/osm/nsd/v1/ns_descriptors_content'
            url_2 = url.replace("http","https")
            logging.debug (url_2)            

            


      
            
            delete_nsd = "curl  --insecure -w \"%{http_code}\" -H \"Content-type: application/yaml\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            delete_nsd_2 = delete_nsd +token + "\"  " + url_2 + "/" + id_to_delete + " -X DELETE" 
            logging.debug (delete_nsd_2)

            deletion = subprocess.check_output([delete_nsd_2], shell=True)
            return (deletion)



    def deleteOSMFunction(self,id_to_delete):
            logging.info("delete osm function starts")
            #print('this SP is a OSM')  

            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            ##print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            sp_host_3 = sp_host_2[7:]
            #print ("sp3 es: ")
            #print (sp_host_3)            

            url = sp_host_3

            token = self.getOSMTokenForDelete()
            logging.debug (token)           

            url = sp_host_2 + ':9999/osm/vnfpkgm/v1/vnf_packages'
            url_2 = url.replace("http","https")
            logging.debug (url_2)            
                              
            delete_nsd = "curl  --insecure -w \"%{http_code}\" -H \"Content-type: application/yaml\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            delete_nsd_2 = delete_nsd +token + "\"  " + url_2 + "/" + id_to_delete + " -X DELETE" 
            logging.debug (delete_nsd_2)

            deletion = subprocess.check_output([delete_nsd_2], shell=True)
            return (deletion)            



    def getOSMTokenForDelete(self):            
        logging.info("get osm token for delete starts")
        JSON_CONTENT_HEADER = {'Accept':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'osm':
            #print('this SP is a OSM')

            #sp_host_0 = self.getDBHost()
            #logging.debug (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #logging.debug (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #logging.debug ("sp1 es: ")
            #logging.debug (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            logging.debug ("sp2 es: ")
            logging.debug (sp_host_2)
            #url = sp_host_2 + '/requests'
            url = sp_host_2 + ':9999/osm/admin/v1/tokens'
            url_2 = url.replace("http","https")

            logging.debug (url_2)

            
            #data = request.get_json()
            logging.debug(url_2)
            #print (data)
            #print (data['nsd_name'])
            #print (data['username'])
            #print (data['password'])
            #print (data['project_id'])


            pr_name = self.getDBProjectName()
            logging.debug ("project name from DB:")
            logging.debug (pr_name)

            if pr_name:
                project_id_for_token = pr_name

            if not pr_name:
                #data = request.get_json()
                #project_id_for_token = data['project_id']
                project_id_for_token = self.getDBProject()
                logging.debug ("project name from json body:")
                logging.debug (pr_name)

            #project_id_for_token = data['project_id']
            print (project_id_for_token)

            #username_for_token = data['username']
            #password_for_token = data['password']

            username_for_token = self.getDBUserName()
            password_for_token = self.getDBPassword()

            #project_id_for_token = data['project_id']
            
            admin_data = "{username: 'admin', password: 'admin', project_id: 'admin'}"
            logging.debug (admin_data)

            #update_token = "UPDATE service_platforms SET service_token = \'" +token+ "\' WHERE name = \'" +self.name+ "\'" 
            
            data_for_token= "{username: \'" +username_for_token+ "\', password: \'" +password_for_token+ "\', project_id: \'" +project_id_for_token+ "\'}"
            #print (data)

            get_token = requests.post(url_2,data=data_for_token,headers=JSON_CONTENT_HEADER,verify=False)
            logging.debug (get_token.text)
            logging.debug (get_token.content)
            token_id = get_token.json()
            logging.debug (token_id['id'])

            #upd_tok = self.updateToken(token_id['id'])

            #print (upd_tok)

            return token_id['id']            


    def getOSMInstaceStatus(self,service_id): 
            logging.info("get osm instance status starts")            
            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)
            sp_host_3 = sp_host_2[7:]
            #print ("sp3 es: ")
            #print (sp_host_3)            
            url = sp_host_3    


            token = self.getOSMToken(service_id)
            logging.debug (token)     
            
            url = sp_host_2 + ':9999/osm/nslcm/v1/ns_instances/' + service_id
            url_2 = url.replace("http","https")
            logging.debug (url_2)

            
            status_ns = "curl  --insecure -w \"%{http_code}\" -H \"Content-type: application/yaml\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            status_ns_2 = status_ns +token + "\" "
            status_ns_3 = status_ns_2 + " " + url_2        
            logging.debug (status_ns_3)

            status = subprocess.check_output([status_ns_3], shell=True)                        
            return (status)     

    def OSMInstantiateCallback(self,token,url_2,callback_url,inst_resp_yaml):
        logging.info("osm instantiate callback starts")
        logging.debug ("callback start")
                
        response = yaml.load(inst_resp_yaml)
        service_id = response['id']
        logging.debug(service_id)

        status_url = "curl --insecure -H \"Content-type: application/json\"  -H \"Accept: application/json\" -H \"Authorization: Bearer " + token + "\" " + url_2 + "/" + service_id + " > /app/temp.file"
        logging.debug(status_url)
        status_curl = subprocess.check_output([status_url], shell=True)
        logging.debug (status_curl)
        #status_json = json.dumps(status_curl)
        #status_json = status_curl.get_json()

        with open('/app/temp.file') as f:
            data = json.load(f)

        status = 'my_status'
        is_active = 'not'

        while status != 'ACTIVE':    
            while is_active == 'not':
                try:
                    status = data['admin']['deployed']['RO']['nsr_status'] 
                    is_active = 'yes'
                    status = 'ACTIVE'
                except:
                    is_active = 'not'
                    status = 'my_status'
                    print("Retraying in 3 sec")
                    print(status)
                    time.sleep(3)
                    status_curl = subprocess.check_output([status_url], shell=True)
                    print (status_curl)
                    with open('/app/temp.file') as f:
                        data = json.load(f)
                                   

        #status = data['admin']['deployed']['RO']['nsr_status']        
        logging.debug (status)

        callback_msg='{\"Message\":\"The service ' + service_id + ' is in status: ' + status + '\"}'
        logging.debug (callback_msg)
        callback_post = "curl -X POST --insecure -H 'Content-type: application/json' " + " --data '" + str(callback_msg) + "'" + " " + callback_url

        call = subprocess.check_output([callback_post], shell=True)
        logging.debug(call)
        logging.debug ("callback end")



    def OSMTerminateCallback(self,token,url_2,callback_url,ns_id):
        logging.info("osm terminate callback starts")
        print ("callback start")
                
        #response = yaml.load(inst_resp_yaml)
        service_id = ns_id
        logging.debug(service_id)

        status_url = "curl --insecure -H \"Content-type: application/json\"  -H \"Accept: application/json\" -H \"Authorization: Bearer " + token + "\" " + url_2 + "/" + service_id + " > /app/temp.file"
        logging.debug(status_url)
        status_curl = subprocess.check_output([status_url], shell=True)
        logging.debug (status_curl)
        #status_json = json.dumps(status_curl)
        #status_json = status_curl.get_json()

        with open('/app/temp.file') as f:
            data = json.load(f)

        status = 'my_status'
        is_active = 'not'

        while status != '404':    
            while is_active == 'not':
                try:
                    status = data['admin']['deployed']['RO']['nsr_status'] 
                    is_active = 'yes'
                    status = '404'
                except:
                    is_active = 'not'
                    status = 'my_status'
                    logging.debug("Retraying in 3 sec")
                    logging.debug(status)
                    time.sleep(3)
                    status_curl = subprocess.check_output([status_url], shell=True)
                    logging.debug (status_curl)
                    with open('/app/temp.file') as f:
                        data = json.load(f)
                                   

        #status = data['admin']['deployed']['RO']['nsr_status']        
        logging.debug (status)



        callback_msg='{\"Message\":\"The service ' + service_id + ' was terminated\"}'
        logging.debug (callback_msg)
        callback_post = "curl -X POST --insecure -H 'Content-type: application/json' " + " --data '" + str(callback_msg) + "'" + " " + callback_url
        call = subprocess.check_output([callback_post], shell=True)
        logging.debug(call)
        logging.debug ("callback end")        



    def OSMUploadFunctionCallback(self,token,url_2,callback_url,inst_resp_yaml):
        logging.info("osm upload function callback starts")        
                
        response = yaml.load(inst_resp_yaml)
        service_id = response['id']
        logging.debug(service_id)

        status_url = "curl --insecure -H \"Content-type: application/json\"  -H \"Accept: application/json\" -H \"Authorization: Bearer " + token + "\" " + url_2 + "/" + service_id + " > /app/temp.file"
        logging.debug(status_url)
        status_curl = subprocess.check_output([status_url], shell=True)
        logging.debug (status_curl)
        #status_json = json.dumps(status_curl)
        #status_json = status_curl.get_json()

        with open('/app/temp.file') as f:
            data = json.load(f)

        logging.debug (data)
        status = 'my_status'
        #status = data['_admin']['onboardingState']

        while status == 'my_status': 
            #print (" ")                               
            status = data['_admin']['onboardingState']
            if status != 'ONBOARDED':
                logging.debug ("Retrying in 3 sec")
                logging.debug (status)
                time.sleep(3)
                status_url = "curl --insecure -H \"Content-type: application/json\"  -H \"Accept: application/json\" -H \"Authorization: Bearer " + token + "\" " + url_2 + "/" + service_id + " > /app/temp.file"
                logging.debug(status_url)            
                status_curl = subprocess.check_output([status_url], shell=True)
                logging.debug (status_curl)
                with open('/app/temp.file') as f:
                    data = json.load(f)
                    logging.debug("data content:")
                    logging.debug (data)
     
        logging.debug (status)


        callback_msg='{\"Message\":\"The function descriptor ' + service_id + ' is in status: ' + status + '\"}'


        logging.debug (callback_msg)       
        callback_post = "curl -X POST --insecure -H 'Content-type: application/json' " + " --data '" + str(callback_msg) + "'" + " " + callback_url
        logging.debug (callback_post)
        call = subprocess.check_output([callback_post], shell=True)
        logging.debug(call)
        logging.debug ("callback end")        


    def OSMUploadServiceCallback(self,token,url_2,callback_url,inst_resp_yaml):
        logging.info("osm upload service callback starts")       
                
        response = yaml.load(inst_resp_yaml)
        service_id = response['id']
        logging.debug(service_id)

        status_url = "curl --insecure -H \"Content-type: application/json\"  -H \"Accept: application/json\" -H \"Authorization: Bearer " + token + "\" " + url_2 + "/" + service_id + " > /app/temp.file"
        logging.debug(status_url)
        status_curl = subprocess.check_output([status_url], shell=True)
        logging.debug (status_curl)
        #status_json = json.dumps(status_curl)
        #status_json = status_curl.get_json()

        with open('/app/temp.file') as f:
            data = json.load(f)

        print (data)
        status = 'my_status'
        #status = data['_admin']['onboardingState']

        while status == 'my_status': 
            #print (" ")                               
            status = data['_admin']['onboardingState']
            if status != 'ONBOARDED':
                logging.debug ("Retrying in 3 sec")
                logging.debug (status)
                time.sleep(3)
                status_url = "curl --insecure -H \"Content-type: application/json\"  -H \"Accept: application/json\" -H \"Authorization: Bearer " + token + "\" " + url_2 + "/" + service_id + " > /app/temp.file"
                logging.debug(status_url)            
                status_curl = subprocess.check_output([status_url], shell=True)
                logging.debug (status_curl)
                with open('/app/temp.file') as f:
                    data = json.load(f)
                    #print("data content:")
                    logging.debug (data)
     
        logging.debug (status)

        callback_msg='{\"Message\":\"The function descriptor ' + service_id + ' is in status: ' + status + '\"}'
        logging.debug (callback_msg)
        callback_post = "curl -X POST --insecure -H 'Content-type: application/json' " + " --data '" + str(callback_msg) + "'" + " " + callback_url
        logging.debug (callback_post)
        call = subprocess.check_output([callback_post], shell=True)
        logging.debug(call)
        logging.debug ("callback end")     

    def monitoringTests(self,monitoring_type):
        logging.info("monitoring tests starts")
        JSON_CONTENT_HEADER = {'Accept':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            logging.debug('this SP is a Sonata')

        if my_type == 'osm':
            #print('this SP is a OSM')

            current_string="date -u +\"%Y-%m-%dT%H:%M:%S.%3N\""
            

            current_date = subprocess.check_output([current_string], shell=True)
            #print (current_date)
            current_date_1 = current_date.__str__()
            #print (current_date_1)
            current_date_2 = current_date_1.__str__()[2:25]
            #print (current_date_2)
            #print ("aaaaaa")

            yesterday_string="date -d \"1 days ago\" -u +\"%Y-%m-%dT%H:%M:%S.%3N\""

            yesterday_date = subprocess.check_output([yesterday_string], shell=True)
            yesterday_date_1 = yesterday_date.__str__()
            #print (yesterday_date_1)
            yesterday_date_2 = yesterday_date_1.__str__()[2:25]
            #print (yesterday_date_2)
            #print ("aaaaaa")    


            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            sp_host_2 = self.getHostIp()
            #print ("sp2 es: ")
            #print (sp_host_2)

            sp_host_3 = sp_host_2[7:]
            #print ("sp3 es: ")
            #print (sp_host_3)            

            url = sp_host_3

            #token = self.getOSMTokenForDelete()
            #print (token)
           
            url = sp_host_2 + ':9091/api/v1/query_range?query=osm_'
            url_2 = url.replace("http","https")
            logging.debug (url_2) 


            monitoring_string = "curl \"" + url + monitoring_type + "&start="  + yesterday_date_2 + "Z&end=" + current_date_2 + "Z&step=15s\""
            #+ "&start=" + yesterday_date_1 + "Z&end=" + current_date_1 + "Z&step=15s"
            logging.debug (monitoring_string)

            monitoring_curl = subprocess.check_output([monitoring_string], shell=True)
            logging.debug (monitoring_curl)

            return monitoring_curl

            
                   


    def getSonataToken(self,request):            
        logging.info("get sonata token starts")
        JSON_CONTENT_HEADER = {'Content-type':'application/json'}   
        #print('this SP is a Sonata')
        #sp_host_0 = self.getDBHost()
        #print (sp_host_0)
        #sp_host = sp_host_0.__str__()
        #print (sp_host)
        #print (self.getDBHost())
        #sp_host_1 = sp_host[4:]
        #print ("sp1 es: ")
        #print (sp_host_1)
        #sp_host_2 = sp_host_1[:-10]
        sp_host_2 = self.getHostIp()
        #print ("sp2 es: ")
        #print (sp_host_2)
        #url = sp_host_2 + '/requests'
        url = sp_host_2 + ':4567/login'
        url_2 = url.replace("http","https")

        logging.debug (url_2)

        username_for_token = self.getDBUserName()
        password_for_token = self.getDBPassword()        
        data_for_token= "{\"username\": \"" +username_for_token+ "\", \"password\": \"" +password_for_token+ "\"}"

        #print ("Data for token:")
        logging.debug (data_for_token)    

        #get_token = requests.post(url,data=data_for_token,headers=JSON_CONTENT_HEADER,verify=False)

        get_token = "curl -i -X POST -H Content-type: application/json -d '" + data_for_token + "' " + url 

        logging.debug (get_token)

        token_curl = subprocess.check_output([get_token], shell=True)

        logging.debug (token_curl)

        string = token_curl.__str__()
        start = string.find('{')
        end = string.find('}', start)
        tok = string[start:end+1]
        logging.debug (tok)


        #return token_curl

        token_id_json = json.loads(tok)
        logging.debug (token_id_json['token'])

        return token_id_json['token']                   
        #return tok['token']



    def downloadPackageTGO(self,package_id):
        logging.info("dwnload package tgo starts")
        get_package_curl = 'curl -H \'Content-type: application/json\' http://tng-cat:4011/api/catalogues/v2/packages/' + package_id
        package_json = subprocess.check_output([get_package_curl], shell=True)
        package_json_loaded = json.loads(package_json)

        package_file_uuid = package_json_loaded['pd']['package_file_uuid']       
        logging.debug (package_file_uuid)

        get_tgo_curl = 'curl -H \'Content-type: application/zip\' http://tng-cat:4011/api/catalogues/v2/tgo-packages/' + package_file_uuid + ' --output /app/packages/' + package_file_uuid + '.tgo'            
        logging.debug (get_tgo_curl)    
        package_tgo = subprocess.check_output([get_tgo_curl], shell=True)

        #msg = "The package " + package_id + " with id " + package_file_uuid +"was downloaded to: /app/packages/" + package_file_uuid + '.tgo' 
        msg = "{\"package\": \"/app/packages/" + package_file_uuid + ".tgo\"}" 
        logging.debug(msg)
        return (msg)




    def osmInstantiationIPs(self,request):    
        logging.info("osm instantiation ips starts")
        #print('this SP is a OSM')   
        #sp_host_0 = self.getDBHost()
        #print (sp_host_0)
        #sp_host = sp_host_0.__str__()
        #print (sp_host)
        #sp_host_1 = sp_host[4:]
        #print ("sp1 es: ")
        #print (sp_host_1)
        #sp_host_2 = sp_host_1[:-10]
        sp_host_2 = self.getHostIp()
        #print ("sp2 es: ")
        #print (sp_host_2)
        sp_host_3 = sp_host_2[7:]
        #print ("sp3 es: ")
        #print (sp_host_3)            
        url = sp_host_3    


        token = self.getOSMToken(request)
        logging.debug (token)

        #content = request.get_json()
        #ns_id = content['ns_id']
        ns_id = request
        logging.debug (ns_id)            
        
        url = sp_host_2 + ':9999/osm/nslcm/v1/ns_instances'
        url_2 = url.replace("http","https")
        logging.debug (url_2)

        
        status_ns = "curl  --insecure  -H \"Content-type: application/yaml\"  -H \"Accept: application/json\" -H \"Authorization: Bearer "
        status_ns_2 = status_ns +token + "\" "
        status_ns_3 = status_ns_2 + " " + url_2 + "/" + ns_id          
        logging.debug (status_ns_3)

        status = subprocess.check_output([status_ns_3], shell=True)

        logging.debug (json.loads(status))
        ns_instance_json = json.loads(status)

        vnfs_array_json = ns_instance_json['constituent-vnfr-ref']
        url_3 = url_2.replace("ns_instances","vnf_instances")

        #response = "{\"NSI id\": \"" + ns_instance_json['id'] + "\"}"
        response = "{\"NSI id\": \"" + ns_instance_json['id'] + "\", \"vnf_instances\": ["

        for vnf_id in vnfs_array_json:
            logging.debug (vnf_id)
            url_4 = "curl  --insecure  -H \"Content-type: application/yaml\"  -H \"Accept: application/json\" -H \"Authorization: Bearer " + token + "\"  " + url_3+ "/" + vnf_id
            vnf_instance_curl= subprocess.check_output([url_4], shell=True)
            vnf_instance_json = json.loads(vnf_instance_curl)
            logging.debug ("This is an VNF instance:")
            logging.debug (vnf_instance_json)

            vdur_arrays = vnf_instance_json['vdur']
            
            for x in vdur_arrays:
                logging.debug (x)
                vdur_name = x['name']
                #response = response + "{\"instance_name\": \"" + x['name'] +"\","

                response = response + "{\"instance_name\": \"" + x['name'] +"\",\"instance_id\": \"" + x['_id']+"\","


                logging.debug (vdur_name)    
                vdur_interfaces = x['interfaces']	
                logging.debug (vdur_interfaces)
                response = response + "\"interfaces\":{"
                for y in vdur_interfaces:
                    logging.debug (y)
                    interface_name = y['name']
                    interface_ip_addresss = y['ip-address']
                    logging.debug (interface_name)
                    logging.debug (interface_ip_addresss) 
                    response = response + "\"" + interface_name + "\": \"" + interface_ip_addresss + "\"}}," 
                    logging.debug (response)
                      
                response_2 = response[:-1]
                #response_2 =  response_2 + "}" 

        #response_3 = response_2[:-1] 
        response_3 = response_2 + "]}"
        logging.debug(response_3)
        return response_3



    def getVnVPackages(self):    
        logging.info("get vnv packages starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}
        url = 'http://tng-cat:4011/api/catalogues/v2/packages'
        response = requests.get(url, headers=JSON_CONTENT_HEADER)    
        if response.ok:        
            logging.debug(response.text)
            #return (response.text, response.status_code, response.headers.items()) 
            return (response.text)

    def getSonataSPPackages(self):    
        logging.info("get sonata sp packages starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}
        host  = self.getHostIp()
        #url = 'http://tng-cat:4011/api/catalogues/v2/packages'
        url =  'http://' + host + ':32002/api/v3/packages'
        response = requests.get(url, headers=JSON_CONTENT_HEADER)    
        if response.ok:        
            logging.debug(response.text)
            #return (response.text, response.status_code, response.headers.items()) 
            return (response.text)


    def getVnVPackagebyId(self,name,vendor,version):    
        logging.info("get vnv packagae id starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'} 
        
        url = 'http://tng-cat:4011/api/catalogues/v2/packages'  
        #print (name,vendor,version)
        response = requests.get(url,headers=JSON_CONTENT_HEADER)
        response_json = response.content
        jjson = json.loads(response_json)
        for x in jjson:
            #print(x)
            if ( x['pd']['name'] == name and x['pd']['vendor'] == vendor and x['pd']['version'] == version ) :
                #print("same name")
                uuid = x['uuid']
                #print(uuid)  
        
        logging.debug(uuid)
        return uuid                   
    

    def getHostIp(self):
        logging.info("get host ip starts")
        sp_host_0 = self.getDBHost()
        sp_host = sp_host_0.__str__()
        sp_host_1 = sp_host[4:]
        sp_host_2 = sp_host_1[:-10]
        url = sp_host_2
        logging.debug(url)
        return url



    def instantiationInfoMonitoring(self,id):    
        logging.info("instantiation info monitoring starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            #response = requests.get(url,headers=JSON_CONTENT_HEADER)
            #response_json = response.content
            #print (response_json) 
            instance_request = self.instantiationStatus(id) 
            logging.debug (instance_request)               
            instance_request_json = json.loads(instance_request)
            instance_uuid = instance_request_json['instance_uuid']
            logging.debug (instance_uuid)

            url = self.getHostIp()
            logging.debug (url)

            response = "{\"ns_instance_uuid\": \"" + instance_uuid + "\",\"functions\":["

            url_records_services = url + ':32002/api/v3/records/services/' + instance_uuid
            service_record = requests.get(url_records_services,headers=JSON_CONTENT_HEADER)
            logging.debug (service_record.text)
            service_record_json = json.loads(service_record.text)
            vnfr_array = service_record_json['network_functions']
            logging.debug (vnfr_array)
            for vnf in vnfr_array:
                function_record_uuid = vnf['vnfr_id']
                logging.debug(function_record_uuid)

                response = response + "{\"vnfr_id\": \"" + function_record_uuid + "\","

                url_records_functions = url + ':32002/api/v3/records/functions/' + function_record_uuid
                function_record = requests.get(url_records_functions,headers=JSON_CONTENT_HEADER)
                function_record_json = json.loads(function_record.text)
                logging.debug(function_record_json)
                try:
                    function_vdu_array = function_record_json['cloudnative_deployment_units']
                    logging.debug (function_vdu_array)
                    for vdu in function_vdu_array:
                        #print(vdu['vim_id'])
                        function_vim = vdu['vim_id']
                        cdu_reference = vdu['cdu_reference']
                        #print (function_vim)
                        response = response + "\"pod_name\": \"" + cdu_reference + "\","
                        response = response + "\"vim_id\": \"" + function_vim + "\","
                        vim_object= self.getVim(function_vim)
                        vim_json = json.loads(vim_object)
                        vim_endpoint = vim_json['endpoint']
                        response = response + "\"vim_endpoint\": \"" + vim_endpoint + "\"},"                 
                except:                    
                    function_vdu_array = function_record_json['virtual_deployment_units']
                    logging.debug (function_vdu_array)
                    for x in function_vdu_array:
                        logging.debug (x)
                        vi = x['vnfc_instance']
                        logging.debug (vi)
                        for y in vi:  
                            logging.debug (y)                                                                       
                            function_vim = y['vim_id']
                            function_vc = y['vc_id']
                            logging.debug(function_vim)
                            logging.debug (function_vc)
                            response = response + "\"vc_id\": \"" + function_vc + "\","
                            response = response + "\"vim_id\": \"" + function_vim + "\","
                            vim_object= self.getVim(function_vim)
                            vim_json = json.loads(vim_object)
                            vim_endpoint = vim_json['endpoint']
                            response = response + "\"vim_endpoint\": \"" + vim_endpoint + "\"},"



                response_2 = response[:-1]                
                response_2 = response_2 + "]"
                response_2 = response_2 + ",\"test_id\": \"null\""

            #return instance_request
            response_2 = response_2 + "}"
            return response_2


    def unzipPackage(self,package):
        logging.info("unzip package starts")
        import zipfile
        package_string = package.__str__()
        package_string_2 = package_string[:-4]
        logging.debug (package_string_2)

        with zipfile.ZipFile(package,"r") as zip_ref:        
            zip_ref.extractall(package_string_2)
        
        msg_response = "The package " + package + " was unzipped to: " + package_string_2
        logging.debug(msg_response)
        return msg_response


    def instantiationInfoCurator(self,id):    
        logging.info("instantiation info curator starts")
        k8s = None
        response_k8s = None
        response_k8s_2 = None
        response_3 = None
        function_record_uuid = None
        ports = None
        fip = None
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            #response = requests.get(url,headers=JSON_CONTENT_HEADER)
            #response_json = response.content
            #print (response_json) 
            instance_request = self.instantiationStatus(id) 
            logging.debug (instance_request)               
            instance_request_json = json.loads(instance_request)
            try:
                instance_uuid = instance_request_json['instance_uuid']
                logging.debug (instance_uuid)
            except:
                error = instance_request_json['error']
                logging.debug (error)
                return instance_request_json

            url = self.getHostIp()
            logging.debug (url)

            #response = "{\"ns_instance_uuid\": \"" + instance_uuid + "\",\"functions\":["
            response = "{\"ns_instance_uuid\": \"" + instance_uuid + "\","                
            response = response + "\"platform_type\": \"" + my_type + "\","
            response = response + "\"functions\":["    

            url_records_services = url + ':32002/api/v3/records/services/' + instance_uuid
            service_record = requests.get(url_records_services,headers=JSON_CONTENT_HEADER)
            logging.debug (service_record.text)
            service_record_json = json.loads(service_record.text)
            vnfr_array = service_record_json['network_functions']
            logging.debug (vnfr_array)
            for vnf in vnfr_array:
                function_record_uuid = vnf['vnfr_id']
                
                logging.debug(function_record_uuid)

                #response = response + "{\"vnfr_id\": \"" + function_record_uuid + "\","
                #response = response + ",{\"id\": \"" + function_record_uuid + "\","
                response = response + ",{"

                url_records_functions = url + ':32002/api/v3/records/functions/' + function_record_uuid
                function_record = requests.get(url_records_functions,headers=JSON_CONTENT_HEADER)
                function_record_json = json.loads(function_record.text)
                logging.debug(function_record_json)
                try:
                    
                    #response = response + "\"platform_type\": \"" + my_type + "\","
                    function_vdu_array = function_record_json['cloudnative_deployment_units']
                    function_type = "cnf" 
                    cnf_name = None
                    response = response + "\"id\": \"" + function_record_uuid + "\","
                    response = response + "\"function_type\": \"" + function_type + "\","                    
                    k8s = "k8s"
                    
                    logging.debug (function_vdu_array)
                    floating_ip = None
                    #response = response + "\"endpoints\": ["
                    
                    for vdu in function_vdu_array:
                        #print(vdu['vim_id'])
                        logging.debug (vdu)
                        #print ("1")
                        #function_vim = vdu['vim_id']
                        cdu_reference = vdu['cdu_reference']
                        #print ("2")                      
                        
                        #response = response + "\"vdu_reference\": \"" + vdu_reference + "\","
                        #response = response + "\"name\": \"" + cdu_reference_2 + "\","
                        cnf_name = cdu_reference[0: cdu_reference.find(":") ]

                        logging.debug (cnf_name)
                        logging.debug (response)
                        #print ("3")   
                        #print (function_vim)
                        #response = response + "{\"container_name\": \"" + cdu_reference + "\","
                        #response = response + "\"name\": \"" + cdu_name + "\","
                        #print ("4")   
                        logging.debug (response)


                        connection_points = vdu['connection_points']
                        logging.debug (connection_points)
                        
                        #response = response + "\"endpoints\": [{"
                        ports = "\"ports\": ["
                        for c in connection_points:
                            #print (c)
                            port_id = c['id']
                            #print (port_id)
                            port_port = c['port']
                            #print (port_port)
                            port_type = c['type']
                            #print (port_type)
                            #response = response + "{\"id\": \"" + port_id + "\","
                            #response = response + "{\"id\": \"" + port_id + "\",\"port\": \""
                            ports = ports + "{\"id\": \"" + port_id + "\",\"port\": \""
                            logging.debug(response)
                            
                            #response = response + port_port.__str__() + "\","
                            ports = ports + port_port.__str__() + "\"},"
                            #response = response + "\"port\": \"" + port_port + "\","
                            #print(response)  
                                                       
                            #response = response + "\"type\": \"" + port_type + "\"},"
                            #print(response)

                        response_ports = ports[:-1]
                        ports = response_ports + "]"
                        #response_port = response[:-1]
                        #response = response + ports + "}]}"                        
                        logging.debug(response)

                        try:
                            load_balancer_ip = vdu['load_balancer_ip']
                            
                            
                            #print ("load_balancer_ipload_balancer_ipload_balancer_ipload_balancer_ipload_balancer_ipload_balancer_ipload_balancer_ipload_balancer_ipload_balancer_ipload_balancer_ipload_balancer_ip")
                            logging.debug (load_balancer_ip)  
                            
                            load_balancer_ip_str =  load_balancer_ip.__str__()
                            #print("1111")
                            #print("1111")
                            #print("1111")
                            #print("1111")
                            load_balancer_ip_str_replaced = load_balancer_ip_str.replace("'","\"")
                            lb_json = json.loads(load_balancer_ip_str_replaced)
                            fip_fip = lb_json['floating_ip']
                            logging.debug (fip_fip)
                            logging.debug(lb_json)
                            #print("1111")
                            #print("1111")
                            #print("1111")
                            #print("1111")


                            load_balancer_ip_str_replaced = load_balancer_ip_str.replace("'","\"")
                            logging.debug (load_balancer_ip_str_replaced)
                            
                            #lb_1 = load_balancer_ip_str_replaced[0: load_balancer_ip_str_replaced.find(",") ]
                            #lb_2 = lb_1[1:]
                            lb_1 = load_balancer_ip_str_replaced.split(",")
                            lb_2 = lb_1[1]

                            
                            

                            #fip = lb_2[:-1]
                            fip = "\"address\": \"" + fip_fip + "\""
                            logging.debug (fip)
                            #print ("load_balancer_ipload_balancer_ipload_balancer_ipload_balancer_ipload_balancer_ipload_balancer_ipload_balancer_ipload_balancer_ipload_balancer_ipload_balancer_ipload_balancer_ip")
                            
                            #load_balancer_ip_str =  load_balancer_ip.__str__()
                            #load_balancer_ip_str_replaced = load_balancer_ip_str.replace("'","\"") 
                            
                            #load_balancer_ip_json = json.loads(load_balancer_ip_str_replaced)           
                            #print (load_balancer_ip_json['floating_ip'])
                            #print ("lplplplppllpplplpplplplplpllpplpl")
                            #response = response + "\"load_balance_ip\": " + load_balancer_ip_str_replaced + ","
                        except:
                            logging.debug ("no load balancer")

                        logging.debug(response)
                        
 
                    response = response + "\"name\": \"" + cnf_name + "\","
                    response = response + "\"endpoints\": [{"
                    response = response + "\"id\": \"" + "floating_ip" + "\"," 
                    response = response + "\"type\": \"" + "floating_ip" + "\","    
                    #response = response + fip + ","
                    fip_ip = fip.replace("floating_ip","address")
                    
                    fip_ip_2 = fip_ip.replace("internal_ip","address")
                    response = response + fip_ip_2 + ","
                    response = response + ports + "}]}"
                    response_2 = response[:-1]
                    response = response_2

                    response = response + "},"
                    response_k8s = response
                                  
                except:
                    function_type = "vnf"                                        
                    function_vdu_array = function_record_json['virtual_deployment_units']
                    logging.debug (function_vdu_array)
                    
                    for x in function_vdu_array:
                        logging.debug (x)
                        vdu_reference = x['vdu_reference']
                        vdu_reference_2 = vdu_reference[0: vdu_reference.find(":") ]
                        #response = response + "\"vdu_reference\": \"" + vdu_reference + "\","                        
                        response = response + "\"function_type\": \"" + function_type + "\","
                        response = response + "\"name\": \"" + vdu_reference_2 + "\","
                        vi = x['vnfc_instance']
                        logging.debug (vi)
                        for y in vi:  
                            logging.debug (y)                                                                       
                            function_vim = y['vim_id']
                            function_vc = y['vc_id']
                            logging.debug(function_vim)
                            logging.debug (function_vc)

                            connection_points = y['connection_points']
                            logging.debug (connection_points)
                            response = response + "\"endpoints\": ["

                            for z in connection_points:
                                logging.debug (z)
                                port_id = z['id']
                                port_type = z['type']
                                port_interface = z['interface']
                                port_ip = port_interface['address']

                                #response = response + "{\"port_id\": \"" + port_id + "\","
                                #response = response + "\"port_type\": \"" + port_type + "\","
                                #response = response + "\"port_ip\": \"" + port_ip + "\"},"

                                response = response + "{\"id\": \"" + port_id + "\","
                                response = response + "\"type\": \"" + port_type + "\","
                                response = response + "\"address\": \"" + port_ip + "\"},"                                    
                            response_port = response[:-1]
                            response = response_port + "]"
                            #response = response_port + "],"

                            #response = response + "\"vc_id\": \"" + function_vc + "\","
                            #response = response + "\"vim_id\": \"" + function_vim + "\","
                            #vim_object= self.getVim(function_vim)
                            #vim_json = json.loads(vim_object)
                            #vim_endpoint = vim_json['endpoint']
                            #response = response + "\"vim_endpoint\": \"" + vim_endpoint + "\"},"



                response_2 = response[:-1]                
                #response_2 = response_2 + "]}]"
                response_2 = response_2 + "]}]}"
                
                #response_2 = response_2 + ",\"test_id\": \"null\""

            
            if k8s == "k8s":
                logging.debug (k8s)
                response_k8s_2 = response_k8s[:-1]
                #response_2 = response[:-1]
                response_2 = response_k8s[:-1]
                #response = response_2 + "]}]}]}"
                #response = response_2 + "]}]}"
                response = response_2 + "]}"
                #print (response)
                #return response
                response_str_replaced = response.replace("[,","[") 
                #print (response_str_replaced)
                response_str_replaced_2 = response_str_replaced.replace("},,","},") 
                logging.debug (response_str_replaced_2)
                return response_str_replaced_2


            #response_2 = response_2 + "}"
            #return response_2

            response_str_replaced = response_2.replace("[,","[") 
            response_str_replaced_2 = response_str_replaced.replace("],","]},") 
            #response_str_replaced_2 = response_str_replaced_2 + "}"
            logging.debug (response_str_replaced_2)
            return response_str_replaced_2
            #response_4 = response_3[1:]
            #return response_4
        
        if my_type == 'osm':
            instance_request = self.instantiationStatus(id) 
            logging.debug (instance_request) 
            instance_request_json =  json.loads(instance_request)
            ns_id = instance_request_json['ns-instance-config-ref']
            logging.debug (ns_id)

            response = "{\"ns_instance_uuid\": \"" + ns_id + "\","
            response = response + "\"platform_type\": \"osm\","
            response = response + "\"functions\": \"["

            vnfr_array = instance_request_json['constituent-vnfr-ref']
            print (vnfr_array)
            for vnfr_id in vnfr_array:
                print ("FUCNTION")
                print(vnfr_id)
                response_function = "{\"id\": \"" + vnfr_id + "\", \"function_type\": " + "osm_function,"
                

                function_request = self.functionRecordOSM(vnfr_id)
                function_request_json =  json.loads(function_request)
                print (function_request_json)
                vnfd_name = function_request_json['vnfd-ref']

                response_function = response_function + "\"name\": \"" + vnfd_name + "\","

                response_function = response_function + "\"endpoints\": ["

                vdur = function_request_json['vdur']                                
                print (vdur)
                for vdu in vdur:
                    interfaces = vdu['interfaces']
                    print (interfaces)
                    for interface in interfaces:                       
                        print (interface)
                        address = interface['ip-address']
                        print (address)
                        name = interface['name']
                        print (name)

                response_function = "{ + + },"

            print (response)
            return response




    def functionRecordOSM(self, vnfr_id):

        url = self.getHostIp()
        token = self.getOSMToken(vnfr_id)
        logging.debug (token)

        #content = request.get_json()
        #ns_id = content['ns_id']
        #ns_id = request
        #logging.debug (ns_id)            
        
        url = url + ':9999/osm/nslcm/v1/vnf_instances'
        url_2 = url.replace("http","https")
        #logging.debug (url_2)

        
        status_ns = "curl  --insecure  -H \"Content-type: application/yaml\"  -H \"Accept: application/json\" -H \"Authorization: Bearer "
        status_ns_2 = status_ns +token + "\" "
        status_ns_3 = status_ns_2 + " " + url_2 + "/" + vnfr_id          
        logging.debug (status_ns_3)

        vnfr = subprocess.check_output([status_ns_3], shell=True)
        vnfr = subprocess.check_output([status_ns_3], shell=True)
        logging.debug (vnfr)
        return (vnfr)  
        
        







    def instantiateServiceNoCallback(self,request): 
        logging.info("instantiation service no callback starts")
        content = request.get_json()
        #print ("request content:")
        logging.debug (content)

        name = content['service_name']
        vendor = content['service_vendor']
        version = content['service_version']        
        callback = content['callback']


        my_type =  self.getDBType()      
        if my_type == 'sonata':
            #print('this SP is a Sonata')  
            
            ### package operations

            package_id = self.getVnVPackagebyId(name,vendor,version)
            logging.debug (package_id)
            download_pkg = self.downloadPackageTGO(package_id)
            logging.debug (download_pkg)            
            download_pkg_json = json.loads(download_pkg)
            logging.debug (download_pkg_json)
            package_path = download_pkg_json['package']
            logging.debug (package_path)
            upload_pkg = self.uploadPackage(package_path)
            logging.debug (upload_pkg)

            #package_id = self.getServiceInstantiations(name,vendor,version)
            #download_pkg = self.downloadPackageTGO(package_id)
            #download_pkg_json = download_pkg.get_json()
            #upload_pkg = self.uploadPackage(download_pkg_json['package'])
            #upload_pkg = self.uploadPackage("/app/packages/basic_package.tgo")
            time.sleep(15)
            
            ### service operations

            service_id = self.getServiceId(name,vendor,version)
            time.sleep(5)
            try:
                instance_name = content['instance_name']
            except:
                #iname = download_pkg_json['package']
                #instance_name = iname[:-4]
                #print ("hi")
                logging.debug("Instance name not found")

            instantiate_str = "{\"service_uuid\": \"" + service_id + "\", \"name\": \"" + instance_name + "\"}"
            logging.debug (instantiate_str)
            instantiate_str_replaced = instantiate_str.replace("'","\"")  
            instantiate_json = json.loads(instantiate_str_replaced)

            #instantiate_json_replaced = instantiate_json.replace("'","\"")            
            print (instantiate_json)
            instantiation_call = self.instantiation(instantiate_str)

            logging.debug (instantiation_call)

            instantiation_request_json_dumps = json.dumps(instantiation_call)
            #print (instantiation_request_json_dumps)
            #print (instantiation_request_json_dumps['id'])

            #instantiation_request_json = json.loads(instantiation_request_json_dumps)
            instantiation_request_json = json.loads(instantiation_call)
            #print (instantiation_request_json)
            #print (instantiation_request_json['id'])
            #print (instantiation_request_json[0][0])
            
            #request_json_loaded = instantiation_request_json.get_json()
            instantiation_request_id = instantiation_request_json['id']
            #instantiation_request_id = instantiation_call['id']
            logging.debug (instantiation_request_id)


            instance_status = self.wait_for_instantiation(instantiation_request_id)
            logging.debug (instance_status)



            #instance_id = self.getRequestInstanceId(instantiation_request_id)
            #print (instance_id)


            if instance_status == 'READY':
                instantiation_info = self.instantiationInfoCurator(instantiation_request_id)
                logging.debug (instantiation_info)                         
            if instance_status == 'ERROR':
                instantiation_info = "Instantiation error"
                logging.debug (instantiation_info)              


        logging.debug(instantiation_info)
        return instantiation_info
            



    def wait_for_instantiation(self,id):
        logging.info("wait for instantiation starts")
        status = None
        while status == None:
            status =  self.getRequestStatus(id)
            logging.debug (status)
            if status == None:
                time.sleep(5)
        while status == 'NEW':
            status =  self.getRequestStatus(id)
            logging.debug (status)
            if status == 'NEW':
                time.sleep(5)        
        while status == 'INSTANTIATING':
            status =  self.getRequestStatus(id)
            logging.debug (status)
            if status == 'INSTANTIATING':
                time.sleep(5)                             
        logging.debug(status)
        return status
        



    def getRequestStatus(self,id):
        logging.info("get request status starts")
        #print ("getRequestStatus begins")
        status_call = self.instantiationStatus(id)
        logging.debug(status_call)

        instantiation_request_json_dumps = json.dumps(status_call)
        logging.debug (instantiation_request_json_dumps)
        #print (instantiation_request_json_dumps['id'])

        #instantiation_request_json = json.loads(instantiation_request_json_dumps)
        instantiation_request_json = json.loads(status_call)
        #print (instantiation_request_json)
        #print (instantiation_request_json['id'])
        #print (instantiation_request_json['status'])



        #request_json = request.get_json()
        try:
            status = instantiation_request_json['status']
            logging.debug(status)
            return (status)
        except:
            msg = "{\"error\": \"the record's status has no value\"}"
            return (msg) 

    def getRequestInstanceId(self,id):
        logging.info("get request if starts")
        request = self.instantiationStatus(id)
        request_json = request.get_json()
        logging.debug(request_json['instance_uuid'])
        return (request_json['instance_uuid'])



    def DownloadUploadTest(self,request):
        logging.info("download upload test starts")
        content = request.get_json()
        #print ("request content:")
        logging.debug (content)

        name = content['service_name']
        vendor = content['service_vendor']
        version = content['service_version']        
        callback = content['callback']

        package_id = self.getVnVPackagebyId(name,vendor,version)
        
        download_pkg = self.downloadPackageTGO(package_id)
        
        #download_pkg_json = download_pkg.get_json()
        download_pkg_json = json.loads(download_pkg)
        
        package_path = download_pkg_json['package']
        
        upload_pkg = self.uploadPackage(package_path)   

        logging.debug(upload_pkg)
        return upload_pkg          




    def instantiateService(self,request): 
        logging.info("instantiate service starts")
        content = request.get_json()
        #print ("request content:")
        logging.debug (content)
        name = content['service_name']
        vendor = content['service_vendor']
        version = content['service_version']        
        callback = content['callback']


        my_type =  self.getDBType()      
        if my_type == 'sonata':
            #print('this SP is a Sonata')  
            
            ### package operations


            vnv_service_id = self.getVnVServiceId(name,vendor,version)
            package_id = self.getPackageIdfromServiceId(vnv_service_id)
            #package_id = self.getVnVPackagebyId(name,vendor,version)
            logging.debug (package_id)
            download_pkg = self.downloadPackageTGO(package_id)
            logging.debug (download_pkg)            
            download_pkg_json = json.loads(download_pkg)
            logging.debug (download_pkg_json)
            package_path = download_pkg_json['package']
            logging.debug (package_path)
            
            ###### commented for try test ffor when the service already exists in the SP
            #upload_pkg = self.uploadPackage(package_path)            
            #logging.debug (upload_pkg)

            try:
                service_id = self.getServiceId(name,vendor,version)
                if service_id:
                    logging.debug("The Service is already in the SP")

            except:
                logging.debug:("The Service is not in the SP  ") 
                upload_pkg = self.uploadPackage(package_path)  
                logging.debug (upload_pkg) 
                

            time.sleep(15)
            
            ### service operations

            service_id = self.getServiceId(name,vendor,version)
            time.sleep(5)
            try:
                instance_name = content['instance_name']
            except:
                #iname = download_pkg_json['package']
                #instance_name = iname[:-4]
                #print ("hi")
                logging.debug("No instance name found")

            instantiate_str = "{\"service_uuid\": \"" + service_id + "\", \"name\": \"" + instance_name + "\"}"
            logging.debug (instantiate_str)
            instantiate_str_replaced = instantiate_str.replace("'","\"")  
            instantiate_json = json.loads(instantiate_str_replaced)
            #instantiate_json_replaced = instantiate_json.replace("'","\"")            
            logging.debug (instantiate_json)
            instantiation_call = self.instantiation(instantiate_str)       

            #try:
            #    _thread.start_new_thread(self.SonataInstantiateCallback, (callback,instantiation_call))
            #    print ("callback init")
            #    return (instantiation_call)	        
            #except:
            #    print ("callback init error")
            #    return (instantiation_call)

            _thread.start_new_thread(self.SonataInstantiateCallback, (callback,instantiation_call))
            
            instantiation_call_str = instantiation_call.__str__()
            instantiation_call_str_replaced = instantiation_call_str.replace("'","\"")
            instantiation_call_str_replaced_2 = instantiation_call_str_replaced[1:]

            string_inicial = "{\"package_id\": \"" + package_id + "\","
            request_response = string_inicial + instantiation_call_str_replaced_2

            logging.debug(request_response)   
            return (request_response)	

            #return (instantiation_call)	
        if my_type == 'osm':
            logging.debug("This SP is osm")
            ### package operations
            """             
            vnv_service_id = self.getVnVServiceId(name,vendor,version)
            package_id = self.getPackageIdfromServiceId(vnv_service_id)            
            logging.debug (package_id)
            download_pkg = self.downloadPackageTGO(package_id)
            logging.debug (download_pkg)            
            download_pkg_json = json.loads(download_pkg)
            logging.debug (download_pkg_json)
            package_path = download_pkg_json['package']
            logging.debug (package_path)            
            """

            """
            try:
                # comprobamos si el servicio esta en el osm de destino
                service_id = self.getOSMServiceId(name,vendor,version)
                if service_id:
                    logging.debug("The Service is already in the SP")

            except:
                logging.debug:("The Service is not in the SP  ") 
                # creamos un array con los path de las funciones de osm que hay en el path donde se ha descargafo el pkg
                functions_array = self.createFunctionsArray(package_path)
                
                for function in functions_array:
                    function_path = self.getOSMFunctionPath(function)
                    upload_function = self.uploadOSMFunction(function_path)
                    logging.debug (upload_function)
                
                service_path = self.getOSMServicePath(package_path)
                upload_service = self.uploadOSMService(service_path) 
                logging.debug (upload_service) 
                service_id = self.getUploadedOSMServiceId(upload_service)
                
            time.sleep(15)
            """
            """
            ## INSTANCIANDO
            nsd_name = service_id
            ns_name = content['ns_name']
            vim_account = content['vim_account']

            instantiate_str = "{\"nsd_name\": \"" + nsd_name + "\", \"ns_name\": \"" + ns_name + "\", \"vim_account\": + \"vim_account\" + "}"
            logging.debug(instantiate_str)

            instantiation_call = self.instantiation(instantiate_str)    
            loggin.debug (instantiation_call)

            _thread.start_new_thread(self.OSMInstantiateCallback, (callback,instantiation_call))
            
            return (instantiation_call)
            """


    def SonataInstantiateCallback(self,callback,instantiation_call):
        logging.info("sonata instantiate callback starts")
        #print ("sonata instantiate callback start")
                
        logging.debug (instantiation_call)

        instantiation_request_json_dumps = json.dumps(instantiation_call)
        logging.debug (instantiation_request_json_dumps)
        #print (instantiation_request_json_dumps['id'])

        #instantiation_request_json = json.loads(instantiation_request_json_dumps)
        instantiation_request_json = json.loads(instantiation_call)
        logging.debug (instantiation_request_json)
        logging.debug (instantiation_request_json['id'])
        #print (instantiation_request_json[0][0])
        
        #request_json_loaded = instantiation_request_json.get_json()
        instantiation_request_id = instantiation_request_json['id']
        #instantiation_request_id = instantiation_call['id']
        logging.debug (instantiation_request_id)


        instance_status = self.wait_for_instantiation(instantiation_request_id)
        logging.debug (instance_status)


        #instance_id = self.getRequestInstanceId(instantiation_request_id)
        #print (instance_id)


        if instance_status == 'READY':
            instantiation_info = self.instantiationInfoCurator(instantiation_request_id)
            logging.debug (instantiation_info) 
            instantiation_info_str = instantiation_info.__str__()
            string_replaced = instantiation_info_str.replace("'","\"")        
            callback_post = "curl -X POST --insecure -H 'Content-type: application/json'" + " --data '" +  string_replaced  +  "' " + callback        
            logging.debug (callback_post)		
            call = subprocess.check_output([callback_post], shell=True)
            logging.debug(call)	

            monitoring_callback = self.getMonitoringURLs()
            info_monitoring =self.instantiationInfoMonitoring(instantiation_request_id)	
            print (info_monitoring) 
            info_monitoring_str = info_monitoring.__str__()
            monitoring_string_replaced = info_monitoring_str.replace("'","\"")        
            monitoring_callback_post = "curl -X POST --insecure -H 'Content-type: application/json'" + " --data '" +  monitoring_string_replaced  +  "' " + monitoring_callback        
            logging.debug (monitoring_callback_post)		
            call_mon = subprocess.check_output([monitoring_callback_post], shell=True)            


        if instance_status == 'ERROR': 

            instantiation_info_json = json.loads(instantiation_info)
            inst_error = instantiation_info_json['error']
            #logging.debug ("This is the instantiation error")
            logging.error (inst_error)

            #callback_post = "curl -X POST --insecure -H 'Content-type: application/json'" + " --data '{\"error\": \"Instantiation error\"}' " + callback        
            callback_post = "curl -X POST --insecure -H 'Content-type: application/json'" + " --data '{\"error\": \"" + inst_error + "\"}' " + callback        
            logging.debug (callback_post)		
            call = subprocess.check_output([callback_post], shell=True)
            logging.debug(call)

            monitoring_callback = self.getMonitoringURLs()
            monitoring_callback_post = "curl -X POST --insecure -H 'Content-type: application/json'" + " --data '{\"error\": \"" + inst_error + "\"}' " + monitoring_callback	                        
            logging.debug (monitoring_callback_post)		
            call_mon = subprocess.check_output([monitoring_callback_post], shell=True)   

        #instantiation_info_str = instantiation_info.__str__()
        #string_replaced = instantiation_info_str.replace("'","\"")        
        #callback_post = "curl -X POST --insecure -H Content-type: application/json" + " --data '" +  string_replaced  +  "' " + callback        
        #print (callback_post)		
        #call = subprocess.check_output([callback_post], shell=True)
        #print(call)		
        
        logging.info ("sonata instantiate callback ends")        


    def instantiateServiceTest(self,request): 
        logging.info("instantiate service starts")
        content = request.get_json()
        #print ("request content:")
        logging.debug (content)
        #print (" - ")    
        #print (" - ")
        name = content['service_name']
        vendor = content['service_vendor']
        version = content['service_version']        
        callback = content['callback']


        my_type =  self.getDBType()      
        if my_type == 'sonata':
            #print('this SP is a Sonata')  
            
            ### package operations
            service_id = self.getServiceId(name,vendor,version)
            package_id = self.getPackageIdfromServiceId(service_id)
            #package_id = self.getVnVPackagebyId(name,vendor,version)
            logging.debug (package_id)
            #download_pkg = self.downloadPackageTGO(package_id)
            #print (download_pkg)            
            #download_pkg_json = json.loads(download_pkg)
            #print (download_pkg_json)
            #package_path = download_pkg_json['package']
            #print (package_path)
            #upload_pkg = self.uploadPackage(package_path)
            #print (upload_pkg)

            time.sleep(15)
            
            ### service operations

            #service_id = self.getServiceId(name,vendor,version)
            time.sleep(5)
            try:
                instance_name = content['instance_name']
            except:
                #iname = download_pkg_json['package']
                #instance_name = iname[:-4]
                #print ("hi")
                logging.error("No instance name found")

            #instantiate_str = "{\"service_uuid\": \"" + service_id + "\", \"name\": \"" + instance_name + "\"}"
            #print (instantiate_str)
            #instantiate_str_replaced = instantiate_str.replace("'","\"")  
            #instantiate_json = json.loads(instantiate_str_replaced)
            #print (" - ")
            #print ("545454545454545454444444444444444444444444444444444444444444444444444444444")
            #print (" - ")
            #instantiate_json_replaced = instantiate_json.replace("'","\"")            
            #print (instantiate_json)
            #instantiation_call = self.instantiation(instantiate_str)       

            #try:
            #    _thread.start_new_thread(self.SonataInstantiateCallback, (callback,instantiation_call))
            #    print ("callback init")
            #    return (instantiation_call)	        
            #except:
            #    print ("callback init error")
            #    return (instantiation_call)

            #_thread.start_new_thread(self.SonataInstantiateCallback, (callback,instantiation_call))
            logging.debug(package_id)
            return (package_id)
            #return (instantiation_call)	

    def getPackageIdfromServiceId (self,service_id):
        logging.info("get package id from service id starts")
        package_id = None
        correct_package = None

        vnv_packages = self.getVnVPackages()
        #vnv_packages = self.getPreIntPackages()
        #print (vnv_packages)
        vnv_packages_json = json.loads(vnv_packages)
        logging.debug (vnv_packages_json)
        

        for package in vnv_packages_json:
            #logging.debug (package)
            package_pd = package['pd']
            #logging.debug (package_pd)
            
            package_content = package_pd['package_content']
            logging.debug (package_content)
            #package_content_json = json.loads(package_content)
            
            for pc in package_content:
                nsd_uuid = pc['uuid']
                logging.debug (nsd_uuid)

                if nsd_uuid == service_id:
                    correct_package = package

        
        package_id = correct_package['uuid']
        logging.debug (package_id)
        return package_id


    def getSPPackageIdfromServiceId (self,service_id):
        logging.info("get sp paclage id from service id starts")
        package_id = None
        correct_package = None

        vnv_packages = self.getPackages()
        #vnv_packages = self.getPreIntPackages()
        logging.debug (vnv_packages)
        vnv_packages_json = json.loads(vnv_packages)
        logging.debug (vnv_packages_json)
        

        for package in vnv_packages_json:
            logging.debug (package)
            package_pd = package['pd']
            logging.debug (package_pd)
            
            package_content = package_pd['package_content']
            logging.debug (package_content)
            #package_content_json = json.loads(package_content)
            
            for pc in package_content:
                nsd_uuid = pc['uuid']
                logging.debug (nsd_uuid)

                if nsd_uuid == service_id:
                    correct_package = package

        
        package_id = correct_package['uuid']
        logging.debug (package_id)
        return package_id


    def getPreIntPackages (self):    
        logging.info("pre int packages starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}
        url = 'http://pre-int-sp-ath.5gtango.eu:32002/api/v3/packages'
        response = requests.get(url, headers=JSON_CONTENT_HEADER)    
        if response.ok:        
            logging.debug(response.text)
            return (response.text)


    def getVnVServiceId(self,name,vendor,version):    
        logging.info("get vnv service id starts")
        uuid = None
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}  
        my_type =  self.getDBType()
        if my_type == 'sonata':                

            url = 'http://tng-cat:4011/api/catalogues/v2/network-services'  
            #print (name,vendor,version)
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            jjson = json.loads(response_json)
            for x in jjson:
                print(x)
                logging.debug(x)
                if ( x['nsd']['name'] == name and x['nsd']['vendor'] == vendor and x['nsd']['version'] == version ) :
                    print("same name")
                    uuid = x['uuid']
                    print(uuid)  

        logging.debug(uuid)
        return uuid           


    def deletePackagefromService(self,name,vendor,version):    
        logging.info("delete package from service starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        response = None
        print ("deletePackagefromService started")

        my_type =  self.getDBType()
        if my_type == 'sonata':    
            #sp_host_0 = self.getDBHost()
            #print (sp_host_0)
            #sp_host = sp_host_0.__str__()
            #print (sp_host)
            #print (self.getDBHost())
            #sp_host_1 = sp_host[4:]
            #print ("sp1 es: ")
            #print (sp_host_1)
            #sp_host_2 = sp_host_1[:-10]
            #print ("sp2 es: ")
            #print (sp_host_2)
            sp_host_2 = self.getHostIp()

            service_id = self.getServiceId(name,vendor,version)
            package_id = self.getSPPackageIdfromServiceId(service_id)            
            url = sp_host_2 + ':32002/api/v3/packages/' + package_id   
            logging.debug (url)     
            response = requests.delete(url,headers=JSON_CONTENT_HEADER)
            logging.debug (response)
    
        logging.debug (response.text)
        msg = '{\"msg\": \"package deleted\"}'
        logging.debug (msg)
        return msg
