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
                if(connection):
                    cursor.close()
                    connection.close()
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
            get_type = "SELECT type FROM service_platforms WHERE name=\'" +self.name+ "\'"            
            cursor.execute(get_type)
            all = cursor.fetchall()            
            type_0 = all.__str__()            
            type_1 = type_0[3:]                       
            type_2 = type_1[:-4]             
            return type_2
        except (Exception, psycopg2.Error) as error :
            logging.error(error)
            exception_message = str(error)
            return exception_message, 401
        finally:
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed") 

    def getVimAccount(self):
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
            get_type = "SELECT vim_account FROM service_platforms WHERE name=\'" +self.name+ "\'"            
            cursor.execute(get_type)
            all = cursor.fetchall()            
            type_0 = all.__str__()            
            type_1 = type_0[3:]                       
            type_2 = type_1[:-4]             
            return type_2
        except (Exception, psycopg2.Error) as error :
            logging.error(error)
            exception_message = str(error)
            return exception_message, 401
        finally:
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
            get_username = "SELECT username FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_username)
            cursor.execute(get_username)
            all = cursor.fetchall()
            type_0 = all.__str__()
            print(type_0)
            type_1 = type_0[3:]            
            print(type_1)            
            type_2 = type_1[:-4]            
            print(type_2)                  
            return type_2
        except (Exception, psycopg2.Error) as error :
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
            get_project_name = "SELECT project_name FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_project_name)
            cursor.execute(get_project_name)
            all = cursor.fetchall()
            type_0 = all.__str__()
            print(type_0)
            type_1 = type_0[3:]            
            print(type_1)            
            type_2 = type_1[:-4]            
            print(type_2)                  
            return type_2
        except (Exception, psycopg2.Error) as error :
            logging.error(error)
            exception_message = str(error)
            return exception_message, 401
        finally:
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
            get_password= "SELECT password FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_password)
            cursor.execute(get_password)
            all = cursor.fetchall()
            type_0 = all.__str__()
            print(type_0)
            type_1 = type_0[3:]            
            print(type_1)            
            type_2 = type_1[:-4]            
            print(type_2)                  
            return type_2
        except (Exception, psycopg2.Error) as error :
            logging.error(error)
            exception_message = str(error)
            return exception_message, 401
        finally:
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
            get_password= "SELECT project_name FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_password)
            cursor.execute(get_password)
            all = cursor.fetchall()
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
            print (self.name)
            get_host = "SELECT host FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_host)
            cursor.execute(get_host)
            all = cursor.fetchall()
            return all, 200    
        except (Exception, psycopg2.Error) as error :
            #print (error)
            logging.error(error)
            exception_message = str(error)
            return exception_message, 401
        finally:
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
            get_type = "SELECT monitoring_urls FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_type)
            cursor.execute(get_type)
            all = cursor.fetchall()
            type_0 = all.__str__()
            print(type_0)
            type_1 = type_0[3:]            
            print(type_1)            
            type_2 = type_1[:-4]            
            print(type_2)                  
            return type_2
        except (Exception, psycopg2.Error) as error :
            logging.error(error)
            exception_message = str(error)
            return exception_message, 401
        finally:
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")                     


    def getPackages(self):    
        logging.info("get packages starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()
        if my_type == 'sonata':               
            sp_host_2 = self.getHostIp()
            logging.info(sp_host_2)

            url = sp_host_2 + ':32002/api/v3/packages'
            
            response = requests.get(url, headers=JSON_CONTENT_HEADER)    
            if response.ok:        
            
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

            sp_host_2 = self.getHostIp()

            url = sp_host_2 + ':32002/api/v3/packages'  
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            jjson = json.loads(response_json)
            pkg = [x for x in jjson if x['pd']['name'] == name and x['pd']['vendor'] == vendor and x['pd']['version'] == version]
            
            if response.ok: 
                    logging.debug(pkg)
                    return jsonify(pkg)

    def deletePackage(self,name,vendor,version):    
        logging.info("delete package starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   

        my_type =  self.getDBType()
        if my_type == 'sonata':    
            sp_host_2 = self.getHostIp()
            url = sp_host_2 + ':32002/api/v3/packages'  
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            jjson = json.loads(response_json)
            pkg = [x for x in jjson if x['pd']['name'] == name and x['pd']['vendor'] == vendor and x['pd']['version'] == version]
            
            if pkg:
                logging.info (pkg)

                uuid_to_delete_1 = [obj['uuid'] for obj in jjson if(obj['pd']['name'] == name)]                            
                uuid_0 = uuid_to_delete_1.__str__()
                uuid_to_delete_2 = uuid_0[2:]
                uuid_to_delete_3 = uuid_to_delete_2[:-2]
                url_for_delete = url + '/' + uuid_to_delete_3
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
            sp_host_2 = self.getHostIp()
            url = sp_host_2 + ':32002/api/v3/packages'  
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            jjson = json.loads(response_json)
            pkg = [x for x in jjson if x['pd']['name'] == name and x['pd']['vendor'] == vendor and x['pd']['version'] == version]
            
            if pkg:
                logging.info(pkg)
                uuid_to_delete_1 = [obj['uuid'] for obj in jjson if(obj['pd']['name'] == name)]            
                
                uuid_0 = uuid_to_delete_1.__str__()
                uuid_to_delete_2 = uuid_0[2:]
                
                uuid_to_delete_3 = uuid_to_delete_2[:-2]
                

                url_for_delete = url + '/' + uuid_to_delete_3
                
                delete = requests.get(url_for_delete, headers=JSON_CONTENT_HEADER)

            if response.ok:                 
                    logging.debug(delete.text)
                    return (delete.text, delete.status_code, delete.headers.items())                

                

                



    def uploadPackage(self,package):
        logging.info("upload package starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()
        if my_type == 'sonata':               
            sp_host_2 = self.getHostIp()
            url = sp_host_2 + ':32002/api/v3/packages'
            logging.info("package info:")
            logging.info(package)
            logging.info(url)
            files = {'package': open(package,'rb')}
            upload = requests.post(url, files=files)
            
            logging.debug(upload.text)
            return upload.text


        if my_type == 'onap':               

            sp_host_2 = self.getHostIp()
            url = sp_host_2 + '/sdc/v1/catalog/services/{uuid}/resourceInstances/{resourceInstanceNormalizedName}/artifacts'            
            print(package)
            print(url)
            files = {'package': open(package,'rb')}
            upload = requests.post(url, files=files)
            if request.method == 'POST':
                return upload.text





    def uploadOSMService(self,request):  
        logging.info("upload osm service starts")
        my_type =  self.getDBType()
        if my_type == 'osm':               
            sp_host_2 = self.getHostIp()
            sp_host_3 = sp_host_2[7:]
            #content = request.get_json()
            #logging.info(content)          
            token = self.getOSMToken(request)
            logging.debug(token)
            #file_to_upload = content['service']
            file_to_upload = request
            file_composed = "@" + file_to_upload
            file = {'nsd-create': open(file_to_upload, 'rb')}           
            data = {'service':file_to_upload}

            HEADERS = {
                'Accept':'application/yaml',
                'Content-Type':'application/zip', 
                'Authorization':'Bearer ' +token+''                
            }
            print (HEADERS)
            #url = sp_host_2 + ':9999/osm/nsd/v1/ns_descriptors'
            url = sp_host_2 + ':9999/osm/nsd/v1/ns_descriptors_content'            
            url_2 = url.replace("http","https")
        
            upload_nsd = "curl -X POST --insecure -H \"Content-type: application/yaml\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            upload_nsd_2 = upload_nsd +token + "\" "
            upload_nsd_3 = upload_nsd_2 + " --data-binary "
            upload_nsd_4 = upload_nsd_3 + "\"@" +file_to_upload+ "\" " + url_2

            logging.debug(upload_nsd_4)
            upload = subprocess.check_output([upload_nsd_4], shell=True)
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
        print (request)
        my_type =  self.getDBType()
        if my_type == 'osm':               
            sp_host_2 = self.getHostIp()
            sp_host_3 = sp_host_2[7:]
            token = self.getOSMToken(request)
            logging.debug(token)
            #content = request.get_json()
            #file_to_upload = content['function']
            file_to_upload = request
            
            #url = sp_host_2 + ':9999/osm/vnfpkgm/v1/vnf_packages'
            url = sp_host_2 + ':9999/osm/vnfpkgm/v1/vnf_packages_content'
            url_2 = url.replace("http","https")

            upload_nsd = "curl -X POST --insecure -H \"Content-type: application/yaml\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            upload_nsd_2 = upload_nsd +token + "\" "
            upload_nsd_3 = upload_nsd_2 + " --data-binary "
            upload_nsd_4 = upload_nsd_3 + "\"@" +file_to_upload+ "\" " + url_2
            logging.debug(upload_nsd_4)
            upload = subprocess.check_output([upload_nsd_4], shell=True)
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
            sp_host_2 = self.getHostIp()
            url = sp_host_2 + ':32002/api/v3/services'
            logging.debug (url)
            response = requests.get(url, headers=JSON_CONTENT_HEADER)    
            if response.ok:        
                    logging.debug(response.text)
                    return (response.text, response.status_code, response.headers.items()) 

        if my_type == 'osm':                
            sp_host_2 = self.getHostIp()
            sp_host_3 = sp_host_2[7:]
            token = self.getOSMToken(request)
            logging.debug(token)
            url = sp_host_2 + ':9999/osm/nsd/v1/ns_descriptors'
            url_2 = url.replace("http","https")
            logging.debug (url_2)
            
            services_nsd = "curl --insecure -w \"%{http_code}\" -H \"Content-type: application/zip\"  -H \"Accept: application/yaml\" -H \"Authorization: Bearer "
            services_nsd_2 = services_nsd +token + "\" "  + url_2
            logging.debug (services_nsd_2)
            services = subprocess.check_output([services_nsd_2], shell=True)
            logging.debug(services)
            return (services) 




            

    def getFunctions(self):    
        logging.info("get functions starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}  
        my_type =  self.getDBType()
        if my_type == 'sonata':                
            sp_host_2 = self.getHostIp()
            url = sp_host_2 + ':32002/api/v3/functions'
            response = requests.get(url, headers=JSON_CONTENT_HEADER)    
            if response.ok:        
                    logging.debug(response.text)
                    return (response.text, response.status_code, response.headers.items()) 

        if my_type == 'osm':                
            sp_host_2 = self.getHostIp()
            sp_host_3 = sp_host_2[7:]
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
            sp_host_2 = self.getHostIp()
            url = sp_host_2 + ':32002/api/v3/services'  
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
            sp_host_2 = self.getHostIp()
            url = sp_host_2 + ':32002/api/v3/requests'  
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
            sp_host_2 = self.getHostIp()
            url = sp_host_2 + ':32002/api/v3/services'  
            #print (name,vendor,version)
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            logging.debug (response_json)
            jjson = json.loads(response_json)
            #pkg = [x for x in jjson if x['nsd']['name'] == name and x['nsd']['vendor'] == vendor and x['nsd']['version'] == version]
            
            for x in jjson:
                if x['nsd']['name'] == name and x['nsd']['vendor'] == vendor and x['nsd']['version'] == version :
                    logging.debug(x['uuid'])
                    return x['uuid']

            '''
            if pkg:
                logging.debug(pkg)
                #uuid_to_delete_1 = [obj['uuid'] for obj in jjson if(obj['nsd']['name'] == name)]            
                uuid_to_delete_1 = [obj['uuid'] for obj in jjson if(obj['nsd']['name'] == name)]
                logging.debug(uuid_to_delete_1)
                uuid_0 = uuid_to_delete_1.__str__()
                uuid_to_delete_2 = uuid_0[2:]
                print(uuid_to_delete_2)
                uuid_to_delete_3 = uuid_to_delete_2[:-2]
                url_for_delete = url + '/' + uuid_to_delete_3
                delete = requests.get(url_for_delete, headers=JSON_CONTENT_HEADER)
        
            if response.ok:                                        
                    logging.debug(uuid_to_delete_3)
                    return uuid_to_delete_3
            '''


    def getPackageId(self,name,vendor,version):    
        logging.info("get package id starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}  
        my_type =  self.getDBType()
        if my_type == 'sonata':                
            sp_host_2 = self.getHostIp()
            url = sp_host_2 + ':32002/api/v3/packages'  
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            logging.debug (response_json)
            jjson = json.loads(response_json)
            pkg = [x for x in jjson if x['pd']['name'] == name and x['pd']['vendor'] == vendor and x['pd']['version'] == version]
            
            if pkg:

                logging.debug(pkg)
                uuid_to_delete_1 = [obj['uuid'] for obj in jjson if(obj['pd']['name'] == name)]                            
                uuid_0 = uuid_to_delete_1.__str__()
                uuid_to_delete_2 = uuid_0[2:]                
                uuid_to_delete_3 = uuid_to_delete_2[:-2]                
                url_for_delete = url + '/' + uuid_to_delete_3                
                delete = requests.get(url_for_delete, headers=JSON_CONTENT_HEADER)        
            if response.ok:                                        
                    logging.debug(uuid_to_delete_3)
                    return uuid_to_delete_3



    def getPackageFile(self,pkg_id):    
        logging.info("get package file starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}  
        my_type =  self.getDBType()
        if my_type == 'sonata':                
            sp_host_2 = self.getHostIp()
            url = sp_host_2 + ':32002/api/v3/packages'  
            url_2 = url + "/" + pkg_id + "/package-file --output temp-file.tgo"
            logging.debug(url_2)          
            response = requests.get(url_2,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            logging.debug (response_json)
            if response.ok:    
                logging.debug(response.text)    
                return (response.text, response.status_code, response.headers.items())                  



    def instantiationStatus(self,request):    
        logging.info("instantiation status starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            sp_host_2 = self.getHostIp()

            url = sp_host_2 + ':32002/api/v3/requests/' +  request
            time.sleep(2)
            logging.debug (url)            
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            logging.debug (response) 
            logging.debug (response.text) 
            response_json = response.content
            logging.debug (response_json)            
            if response.ok:        
                logging.debug(response.text)
                return (response.text)

        if my_type == 'osm':
            sp_host_2 = self.getHostIp() 
            token = self.getOSMToken(request)
            logging.debug (token)
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
            sp_host_2 = self.getHostIp()
            url = sp_host_2 + ':32002/api/v3/requests'  
            logging.debug (url)            
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            logging.debug (response_json)
            if response.ok: 
                logging.debug(response.text)       
                return (response.text, response.status_code, response.headers.items())
        if my_type == 'osm':
            sp_host_2 = self.getHostIp()
            sp_host_3 = sp_host_2[7:]  
            url = sp_host_3                        
            token = self.getOSMToken(request)
            logging.debug (token)
            url = sp_host_2 + ':9999/osm/nslcm/v1/ns_instances'
            url_2 = url.replace("http","https")
            logging.debug (url_2)            
            instances_1 = "curl --insecure -H \"Content-type: application/json\"  -H \"Accept: application/json\" -H \"Authorization: Bearer "                    
            instances_2 = instances_1 +token + "\" "  + url_2
            logging.debug (instances_2)        
            ns_instances = subprocess.check_output([instances_2], shell=True)
            ns_instances = subprocess.check_output([instances_2], shell=True)
            return (ns_instances)         



    def instantiation(self,request):    
        logging.info("instantiation starts")
        logging.debug ("INSTANTIATION FUNCTION BEGINS")
        logging.debug (request)
        request_str = request.__str__()
        logging.debug (request_str)
        JSON_CONTENT_HEADER = {'content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'onap':
            '''
            print('this SP is ONAP')
            sp_host_2 = self.getHostIp()
            print ("sp2 es: ")
            print (sp_host_2)
            url = sp_host_2 + '}/serviceInstances/v4'
            print (url)
            print(request_str.get_json())
            data = request_str.get_json()
            print(url)
            print (data)
            instantiate = requests.post( url, data=json.dumps(data), headers=JSON_CONTENT_HEADER)            
            print (instantiate)
            if request.method == 'POST':
                return instantiate.text 
            '''           


        if my_type == 'sonata':
            sp_host_2 = self.getHostIp()
            url = sp_host_2 + ':32002/api/v3/requests'
            logging.debug(url)
            try:         
                instantiate = requests.post( url, data=request, headers=JSON_CONTENT_HEADER)                      
                logging.debug ("THIS IS THE INSTANTIATE RESPONSE:")
                logging.debug (instantiate)
                logging.debug (instantiate.text)
                return instantiate.text
            except:
                logging.error ("Error sending the request, check the connection and logs")
                msg = "{\"error\": \"error sending the request, check the connection and logs\"}"
                return msg                  

        if my_type == 'osm':
            print('this SP is a OSM')  
            sp_host_2 = self.getHostIp()
            sp_host_3 = sp_host_2[7:]
            url = sp_host_3
            #content = request.get_json()
            logging.debug ("REQUEST")
            logging.debug (request)
            content = json.loads(request.__str__())
            logging.debug ("CONTENT:")
            logging.debug(content)
            token = self.getOSMToken(request)
            logging.debug (token)
            #content = request.get_json()           
            url = sp_host_2 + ':9999/osm/nslcm/v1/ns_instances_content'
            url_2 = url.replace("http","https")
            logging.debug (url_2)
            vim_account = self.getVimAccount()
            vim_id = self.getVimId(vim_account)
            logging.debug (vim_id)
            logging.debug (content['nsd_name'])
            #nsd_id = self.getOSMNsdId(content['nsd_name'])
            nsd_id = content['nsd_name']
            ns_name = content['ns_name']
            logging.debug (nsd_id)


          



            HEADERS = {
                'Accept':'application/json',
                'Content-Type':'application/json', 
                'Authorization':'Bearer ' +token+''                
            }     

            data_inst = {
                'nsdId':''+nsd_id+'',
                'nsName':''+ns_name+'',
                'vimAccountId':''+vim_id+''
            }       
            
            instantiate_nsd = "curl -X POST --insecure -H \"Content-type: application/yaml\"  -H \"Accept: application/json\" -H \"Authorization: Bearer "                
            instantiate_nsd_2 = instantiate_nsd +token + "\" "
            instantiate_nsd_3 = instantiate_nsd_2 + " --data \"" + str(data_inst) + "\""
            instantiate_nsd_4 = instantiate_nsd_3 + " " + url_2
            logging.debug (instantiate_nsd_4)

            inst = subprocess.check_output([instantiate_nsd_4], shell=True)

            try:
                callback_url = content['callback']
                logging.debug ("Callback url specified")
                _thread.start_new_thread(self.OSMUploadServiceCallback, (token,url_2,callback_url,inst))
            except:
                logging.debug ("No callback url specified")                

            logging.debug(inst)
            return (inst)




    def instantiationDelete(self,request):    
        logging.info("instantiation delete starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()


        if my_type == 'onap':
            sp_host_2 = self.getHostIp()
            url = sp_host_2
            content = request.get_json()
            ns_instance_id = content['ns_instance_id']
            logging.debug (ns_instance_id) 
            url_2 = url + '/ns/' + ns_instance_id
            logging.debug (url_2)                    
            terminate = requests.delete(url_2,headers=JSON_CONTENT_HEADER) 
            if request.method == 'POST':
                logging.debug(terminate.text)
                return terminate.text

        if my_type == 'sonata':
            sp_host_2 = self.getHostIp()
            url = sp_host_2 + ':32002/api/v3/requests'
            logging.debug(url)
            logging.debug (request)            
            terminate = requests.post(url,data=request,headers=JSON_CONTENT_HEADER) 
            logging.debug (terminate)
            logging.debug (terminate.text)

            content = json.loads(request)
            ns_id = content['instance_uuid']
            logging.debug(ns_id)
            url_monitoring = self.getMonitoringURLs()
            terminate_string = "curl -X DELETE -H \"Content-type: application/json\" "  + url_monitoring + "/" + ns_id 
            logging.debug(terminate_string)    
            terminate_monitoring = subprocess.check_output([terminate_string], shell=True)

            return terminate.text

        if my_type == 'osm':
            sp_host_2 = self.getHostIp()
            sp_host_3 = sp_host_2[7:]
            url = sp_host_3
            logging.debug(request)
            logging.debug(url)
            token = self.getOSMToken(request)
            logging.debug (token)
            
            #url = sp_host_2 + ':9999/osm/nslcm/v1/ns_instances_content'
            url = sp_host_2 + ':9999/osm/nslcm/v1/ns_instances_content'
            url_2 = url.replace("http","https")
            
            content = json.loads(request)
            ns_id = content['instance_uuid']
            logging.debug(ns_id)
            
            
            logging.debug (ns_id)
            delete_ns = "curl -X DELETE --insecure -H \"Content-type: application/json\"  -H \"Accept: application/json\" -H \"Authorization: Bearer "
            delete_ns_2 = delete_ns +token + "\" "
            delete_ns_3 = delete_ns_2 + " " + url_2 + "/" + ns_id          
            logging.debug (delete_ns_3)

            # terminating the instance
            terminate = subprocess.check_output([delete_ns_3], shell=True)
            #terminate = "hola"

            # deleting the descriptors
            package_uploaded = content['package_uploaded']
            logging.debug(package_uploaded)
            if ( package_uploaded == True ) or ( package_uploaded == "true" ) or ( package_uploaded == "True" ):
                instance_status = self.OSMTerminateStatus(url_2,ns_id)
                print(instance_status)
                while instance_status != 'terminated':
                    time.sleep(2)
                    instance_status = self.OSMTerminateStatus(url_2,ns_id)
                delete_descriptors = self.deleteOSMDescriptors(ns_id)
                
                print (delete_descriptors)

            print (terminate)
            #_thread.start_new_thread(self.OSMUploadServiceCallback, (token,url_2,callback_url,content['ns_id']))
                                 
            logging.debug(terminate)
            return (terminate)            

                        
    def deleteOSMDescriptors(self,instance_id):
        logging.debug("deleteOSMDescriptors begins")
        sp_host_2 = self.getHostIp()
        logging.debug(sp_host_2)
        token = self.getOSMToken(request)
        logging.debug (token)        
        #url = sp_host_2 + ':9999/osm/nslcm/v1/ns_instances_content'
        url = sp_host_2 + ':9999/osm/nslcm/v1/ns_instances_content'
        url_2 = url.replace("http","https")
        logging.debug (url_2)

        #content = json.loads(request)
        ns_id = instance_id
        logging.debug(ns_id)
        
        logging.debug (ns_id)
        instance_ns = "curl --insecure -H \"Content-type: application/json\"  -H \"Accept: application/json\" -H \"Authorization: Bearer "
        instance_ns_2 = instance_ns +token + "\" "
        instance_ns_3 = instance_ns_2 + " " + url_2 + "/" + ns_id          
        logging.debug (instance_ns_3)

        instance = subprocess.check_output([instance_ns_3], shell=True)
        print(instance)
        instance_json = json.loads(instance)
        print(instance_json)
        nsdId = instance_json['instantiate_params']['nsdId']
        print (nsdId)

        vnfr_array = instance_json['constituent-vnfr-ref']


        vnfds = []

        logging.debug (vnfr_array)
        for vnfr_id in vnfr_array:
            logging.debug ("FUCNTIONS")
            logging.debug(vnfr_id)                
            function_request = self.functionRecordOSM(vnfr_id)
            function_request_json =  json.loads(function_request)
            print (function_request_json)
            vnfd_id = function_request_json['vnfd-id']
            print (vnfd_id)
            vnfds.append(vnfd_id)


        try:
            instance = None
            instance = subprocess.check_output([instance_ns_3], shell=True)
            print (instance)
            while instance is not None:
                instance = subprocess.check_output([instance_ns_3], shell=True)
                print (instance)
                instance_json = json.loads(instance)
                status = instance_json['status']
                if status == '404':
                    raise Exception('The instance has been terminated. Deleting descriptors...') 
        except:
            logging.debug("The instance has been terminated. Deleting descriptors...")
        
        deleteOSMService = self.deleteOSMService(nsdId)
        print (deleteOSMService)
        time.sleep(7)
        for vnfd_id in vnfds:
            deleteOSMFunction = self.deleteOSMFunction(vnfd_id)
            print (deleteOSMFunction)
        
        return "deleted"       
        


    def getOSMToken(self,request):        
        logging.info("get osm token starts")      
        JSON_CONTENT_HEADER = {'Accept':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'osm':
            sp_host_2 = self.getHostIp()
            url = sp_host_2 + ':9999/osm/admin/v1/tokens'
            url_2 = url.replace("http","https")
            logging.debug (url_2)
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

            logging.debug (project_id_for_token)
            username_for_token = self.getDBUserName()
            password_for_token = self.getDBPassword()

            admin_data = "{username: 'admin', password: 'admin', project_id: 'admin'}"
            logging.debug (admin_data)
            
            data_for_token= "{username: \'" +username_for_token+ "\', password: \'" +password_for_token+ "\', project_id: \'" +project_id_for_token+ "\'}"

            get_token = requests.post(url_2,data=data_for_token,headers=JSON_CONTENT_HEADER,verify=False)
            logging.debug (get_token.text)
            logging.debug (get_token.content)
            token_id = get_token.json()

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
            sp_host_2 = self.getHostIp()                   
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
            sp_host_2 = self.getHostIp()
            sp_host_3 = sp_host_2[7:]  
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
            logging.debug(vims)
            return (vims) 
   


    def getVimId(self,vim):    
        logging.info("get vim id starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        my_type =  self.getDBType()

        if my_type == 'sonata':
            sp_host_2 = self.getHostIp()
            url = sp_host_2 + ':32002/api/v3/requests'  
            logging.debug (url)
            return url

        if my_type == 'osm':
            sp_host_2 = self.getHostIp()
            sp_host_3 = sp_host_2[7:]  
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
            sp_host_2 = self.getHostIp()
            sp_host_3 = sp_host_2[7:]  
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
            logging.debug (s[start+21:end])
            vim_id = s[start+21:end]         
            logging.debug(vim_id)
            return vim_id            

    def downloadPackageSonata(self,package_id):
        logging.info("download package sonata starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}                              
        sp_host_2 = self.getHostIp()
        url = sp_host_2 + ':32002/api/v3/packages'        
        url2 = 'curl ' + url + '/' + package_id + '/package-file --output /app/packages/' + package_id + '.tgo'        
        logging.debug(url2)
        download = subprocess.check_output([url2], shell=True)
        msg = "Package downloaded to: " + "/app/packages/" + package_id + '.tgo' 
        logging.debug(msg)
        return (msg)

    def deleteOSMService(self,id_to_delete):
            logging.info("delete osm service starts")
            sp_host_2 = self.getHostIp()
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
            sp_host_2 = self.getHostIp()
            sp_host_3 = sp_host_2[7:]
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
            sp_host_2 = self.getHostIp()
            logging.debug ("sp2 es: ")
            logging.debug (sp_host_2)
            url = sp_host_2 + ':9999/osm/admin/v1/tokens'
            url_2 = url.replace("http","https")
            logging.debug (url_2)
            logging.debug(url_2)
            pr_name = self.getDBProjectName()
            logging.debug ("project name from DB:")
            logging.debug (pr_name)

            if pr_name:
                project_id_for_token = pr_name

            if not pr_name:
                project_id_for_token = self.getDBProject()
                logging.debug ("project name from json body:")
                logging.debug (pr_name)

            print (project_id_for_token)
            username_for_token = self.getDBUserName()
            password_for_token = self.getDBPassword()            
            admin_data = "{username: 'admin', password: 'admin', project_id: 'admin'}"
            logging.debug (admin_data)           
            data_for_token= "{username: \'" +username_for_token+ "\', password: \'" +password_for_token+ "\', project_id: \'" +project_id_for_token+ "\'}"
            get_token = requests.post(url_2,data=data_for_token,headers=JSON_CONTENT_HEADER,verify=False)
            logging.debug (get_token.text)
            logging.debug (get_token.content)
            token_id = get_token.json()
            logging.debug (token_id['id'])
            return token_id['id']            


    def getOSMInstaceStatus(self,service_id): 
            logging.info("get osm instance status starts")            
            sp_host_2 = self.getHostIp()
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

    def OSMInstantiateCallback(self, callback_url,inst_resp_yaml):

        token = self.getOSMToken(request)

        sp_host_2 = self.getHostIp()
        url = sp_host_2 + ':9999/osm/nslcm/v1/ns_instances_content'
        url_2 = url.replace("http","https")        

        logging.info("osm instantiate callback starts")
        logging.debug ("callback start")                
        response = yaml.load(inst_resp_yaml)
        service_id = response['id']
        logging.debug(service_id)
        #status_url = "curl --insecure -H \"Content-type: application/json\"  -H \"Accept: application/json\" -H \"Authorization: Bearer " + token + "\" " + url_2 + "/" + service_id + " > /app/temp.file"
        status_url = "curl --insecure -H \"Content-type: application/json\"  -H \"Accept: application/json\" -H \"Authorization: Bearer " + token + "\" " + url_2 + "/" + service_id 
        logging.debug(status_url)
        status_curl = subprocess.check_output([status_url], shell=True)
        logging.debug (status_curl)

        #instance_json = json.loads(status_curl.__str__())
        instance_json = json.loads(status_curl)

        config_status = instance_json['config-status']
        print (config_status)

        operational_status = instance_json['operational-status']
        print (operational_status)

        status = None
             
        while ( operational_status != 'running' and operational_status != 'error' ):               
            try:
                status = data['config-status']                    
                logging.debug (status)
            except:
                logging.debug("Retraying in 3 sec")
                logging.debug (status)
                time.sleep(3)
                status_curl = subprocess.check_output([status_url], shell=True)
                logging.debug (status_curl)
                instance_json = json.loads(status_curl)
                config_status = instance_json['config-status']
                logging.debug (config_status)
                operational_status = instance_json['operational-status']
                logging.debug (operational_status)

        status = config_status
        logging.debug (status)

        #callback_msg='{\"Message\":\"The service ' + service_id + ' is in status: ' + status + '\"}'

        callback_msg = self.instantiationInfoCurator(service_id)
        logging.debug (callback_msg)
        #callback_post = "curl -X POST --insecure -H 'Content-type: application/json' " + " --data '" + str(callback_msg) + "'" + " " + callback_url
        callback_post = "curl -X POST --insecure -H 'Content-type: application/json' " + " --data '" + callback_msg + "'" + " " + callback_url
        logging.debug (callback_post)
        call = subprocess.check_output([callback_post], shell=True)
        logging.debug(call)


        #Monitoring callback       
        callback_msg = self.instantiationInfoMonitoring(service_id)
        callback_url_monitoring = self.getMonitoringURLs()
        callback_post_monitoring = "curl -X POST --insecure -H 'Content-type: application/json' " + " --data '" + callback_msg + "'" + " " + callback_url_monitoring
        logging.debug (callback_post_monitoring)
        call_monitoring = subprocess.check_output([callback_post_monitoring], shell=True)
        logging.debug(call_monitoring)


        logging.debug ("callback ends")





    def OSMTerminateStatus(self,url_2,ns_id):
        logging.info("osm terminate status starts")        
        service_id = ns_id
        logging.debug(service_id)
        token = self.getOSMToken(ns_id)
        status_url = "curl --insecure -H \"Content-type: application/json\"  -H \"Accept: application/json\" -H \"Authorization: Bearer " + token + "\" " + url_2 + "/" + service_id + " > /app/temp.file"
        logging.debug(status_url)
        status_curl = subprocess.check_output([status_url], shell=True)
        logging.debug (status_curl)
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

        status = "terminated"  

        return status








    def OSMTerminateCallback(self,token,url_2,callback_url,ns_id):
        logging.info("osm terminate callback starts")
        logging.debug ("callback start")
        service_id = ns_id
        logging.debug(service_id)
        status_url = "curl --insecure -H \"Content-type: application/json\"  -H \"Accept: application/json\" -H \"Authorization: Bearer " + token + "\" " + url_2 + "/" + service_id + " > /app/temp.file"
        logging.debug(status_url)
        status_curl = subprocess.check_output([status_url], shell=True)
        logging.debug (status_curl)
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

        with open('/app/temp.file') as f:
            data = json.load(f)

        logging.debug (data)
        status = 'my_status'

        while status == 'my_status':                            
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
        with open('/app/temp.file') as f:
            data = json.load(f)
        logging.debug (data)
        status = 'my_status'

        while status == 'my_status': 
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
            current_string="date -u +\"%Y-%m-%dT%H:%M:%S.%3N\""          
            current_date = subprocess.check_output([current_string], shell=True)
            current_date_1 = current_date.__str__()
            current_date_2 = current_date_1.__str__()[2:25]
            yesterday_string="date -d \"1 days ago\" -u +\"%Y-%m-%dT%H:%M:%S.%3N\""
            yesterday_date = subprocess.check_output([yesterday_string], shell=True)
            yesterday_date_1 = yesterday_date.__str__()
            yesterday_date_2 = yesterday_date_1.__str__()[2:25]
            sp_host_2 = self.getHostIp()
            url = sp_host_2 + ':9091/api/v1/query_range?query=osm_'
            url_2 = url.replace("http","https")
            logging.debug (url_2) 
            monitoring_string = "curl \"" + url + monitoring_type + "&start="  + yesterday_date_2 + "Z&end=" + current_date_2 + "Z&step=15s\""
            logging.debug (monitoring_string)
            monitoring_curl = subprocess.check_output([monitoring_string], shell=True)
            logging.debug (monitoring_curl)
            return monitoring_curl

    def getSonataToken(self,request):            
        logging.info("get sonata token starts")
        JSON_CONTENT_HEADER = {'Content-type':'application/json'}   
        sp_host_2 = self.getHostIp()
        url = sp_host_2 + ':4567/login'
        url_2 = url.replace("http","https")
        logging.debug (url_2)
        username_for_token = self.getDBUserName()
        password_for_token = self.getDBPassword()        
        data_for_token= "{\"username\": \"" +username_for_token+ "\", \"password\": \"" +password_for_token+ "\"}"
        logging.debug (data_for_token)   
        get_token = "curl -i -X POST -H Content-type: application/json -d '" + data_for_token + "' " + url 
        logging.debug (get_token)
        token_curl = subprocess.check_output([get_token], shell=True)
        logging.debug (token_curl)
        string = token_curl.__str__()
        start = string.find('{')
        end = string.find('}', start)
        tok = string[start:end+1]
        logging.debug (tok)
        token_id_json = json.loads(tok)
        logging.debug (token_id_json['token'])
        return token_id_json['token']                   




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

        msg = "{\"package\": \"/app/packages/" + package_file_uuid + ".tgo\"}" 
        logging.debug(msg)
        return (msg)




    def osmInstantiationIPs(self,request):    
        logging.info("osm instantiation ips starts")
        sp_host_2 = self.getHostIp()
        sp_host_3 = sp_host_2[7:]           
        url = sp_host_3
        token = self.getOSMToken(request)
        logging.debug (token)
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
        logging.debug (json.loads(status))
        ns_instance_json = json.loads(status)
        vnfs_array_json = ns_instance_json['constituent-vnfr-ref']
        url_3 = url_2.replace("ns_instances","vnf_instances")
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
            return (response.text)

    def getSonataSPPackages(self):    
        logging.info("get sonata sp packages starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}
        host  = self.getHostIp()
        url =  'http://' + host + ':32002/api/v3/packages'
        response = requests.get(url, headers=JSON_CONTENT_HEADER)    
        if response.ok:        
            logging.debug(response.text)
            return (response.text)


    def getVnVPackagebyId(self,name,vendor,version):    
        logging.info("get vnv packagae id starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'} 
        
        url = 'http://tng-cat:4011/api/catalogues/v2/packages'  

        try:
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            jjson = json.loads(response_json)
            for x in jjson:
                if ( x['pd']['name'] == name and x['pd']['vendor'] == vendor and x['pd']['version'] == version ) :
                    uuid = x['uuid']
            logging.debug(uuid)
            return uuid                   
        except:
            msg = "{\"error\": \"error getting the package id from the VnV catalogue\"}"
            return msg  
    

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
                        logging.debug (cdu_reference)
                        cdu_reference_splitted = cdu_reference.split(":")
                        #cnf_name = cdu_reference[0: cdu_reference.find(":") ]
                        cnf_name = cdu_reference_splitted[1]
                        container_name = cnf_name
                        logging.debug (cnf_name)

                        response = response + "\"container_name\": \"" + cnf_name + "\","
                        response = response + "\"pod_name\": \"" + cdu_reference + "\","
                        #response = response + "\"pod_name\": \"" + cnf_name + "\","
                        #response = response + "\"pod_name\": \"" + cdu_reference + "\","
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

            response_2 = response_2 + "}"
            return response_2

        if my_type == 'osm':
            instance_request = self.instantiationStatus(id) 
            logging.debug (instance_request) 
            instance_request_json =  json.loads(instance_request)
            ns_id = instance_request_json['ns-instance-config-ref']
            logging.debug (ns_id)

            response = "{\"ns_instance_uuid\": \"" + ns_id + "\","
            response = response + "\"platform_type\": \"osm\","
            response = response + "\"functions\": ["

            vnfr_array = instance_request_json['constituent-vnfr-ref']
            logging.debug (vnfr_array)
            response_functions = " "
            for vnfr_id in vnfr_array:
                logging.debug ("FUCNTIONS")
                logging.debug(vnfr_id)
                response_function = "{\"vnfr_id\": \"" + vnfr_id + "\", \"function_type\": " + "\"vnf\","                

                function_request = self.functionRecordOSM(vnfr_id)
                function_request_json =  json.loads(function_request)
                logging.debug (function_request_json)
                vnfd_name = function_request_json['vnfd-ref']  

                vim_id = function_request_json['vim-account-id'] 

                response_function = response_function + "\"name\": \"" + vnfd_name + "\","
                response_function = response_function + "\"endpoints\": ["
                vdur = function_request_json['vdur']                                
                logging.debug (vdur)
                
                for vdu in vdur:
                    vc_id = vdu['vim-id']                                       
                    interfaces = vdu['interfaces']
                    logging.debug (interfaces)
                    for interface in interfaces:                       
                        logging.debug (interface)
                        address = interface['ip-address']
                        logging.debug (address)
                        name = interface['name']
                        type = interface['name']
                        logging.debug (name)
                        response_interface = "{\"name\": \"" + name + "\", \"type\": \"" + type + "\",\"address\":\"" + address + "\"" + "},"

                        response_function = response_function + response_interface

                response_function_2 = response_function[:-1]

                response_function = response_function_2 + "],"

                response_function = response_function + "\"vc_id\": \"" + vc_id + "\","
                response_function = response_function + "\"vim_id\": \"" + vim_id + "\","
                vim_info = self.getOSMVIMInfo(vim_id)
                vim_url = self.getOSMVIMInfoURL(vim_info)
                response_function = response_function + "\"vim_endpoint\": \"" + vim_url + "\","

                response_function_2 = response_function[:-1]
                response_function_2 = response_function_2 + "},"

                logging.debug (response_function_2)
                response_functions = response_functions + response_function_2

            response_functions_2 = response_functions[:-1] 

            response_functions = response_functions_2 + "],"
            
            
            response = response + response_functions
            response = response + "\"test_id\": \"null\""
            response = response + "}"
            logging.debug (response)
            return response            


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
        #return msg_response
        return package_string_2


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
            instance_request = self.instantiationStatus(id) 
            logging.debug (instance_request)               
            
            try:
                instance_request_json = json.loads(instance_request)
                instance_uuid = instance_request_json['instance_uuid']
                logging.debug (instance_uuid)
            except:
                error = "error in the request"
                logging.debug (error)
                msg = "{\"error\": \"error in the request, check the SP\"}"
                return msg

            url = self.getHostIp()
            logging.debug (url)
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
                response = response + ",{"
                url_records_functions = url + ':32002/api/v3/records/functions/' + function_record_uuid
                function_record = requests.get(url_records_functions,headers=JSON_CONTENT_HEADER)
                function_record_json = json.loads(function_record.text)
                logging.debug(function_record_json)
                try:
                    function_vdu_array = function_record_json['cloudnative_deployment_units']
                    function_type = "cnf" 
                    cnf_name = None
                    response = response + "\"id\": \"" + function_record_uuid + "\","
                    response = response + "\"function_type\": \"" + function_type + "\","                    
                    k8s = "k8s"
                    
                    logging.debug (function_vdu_array)
                    floating_ip = None
                    
                    for vdu in function_vdu_array:
                        logging.debug (vdu)
                        cdu_reference = vdu['cdu_reference']
                        cnf_name = cdu_reference[0: cdu_reference.find(":") ]
                        logging.debug (cnf_name)
                        logging.debug (response)
                        connection_points = vdu['connection_points']
                        logging.debug (connection_points)
                        ports = "\"ports\": ["
                        for c in connection_points:
                            port_id = c['id']
                            port_port = c['port']
                            port_type = c['type']
                            ports = ports + "{\"id\": \"" + port_id + "\",\"port\": \""
                            logging.debug(response)
                            ports = ports + port_port.__str__() + "\"},"

                        response_ports = ports[:-1]
                        ports = response_ports + "]"
                       
                        logging.debug(response)

                        try:
                            load_balancer_ip = vdu['load_balancer_ip']
                            logging.debug (load_balancer_ip)                              
                            load_balancer_ip_str =  load_balancer_ip.__str__()
                            load_balancer_ip_str_replaced = load_balancer_ip_str.replace("'","\"")
                            lb_json = json.loads(load_balancer_ip_str_replaced)
                            fip_fip = lb_json['floating_ip']
                            logging.debug (fip_fip)
                            logging.debug(lb_json)
                            load_balancer_ip_str_replaced = load_balancer_ip_str.replace("'","\"")
                            logging.debug (load_balancer_ip_str_replaced)
                            lb_1 = load_balancer_ip_str_replaced.split(",")
                            lb_2 = lb_1[1]
                            fip = "\"address\": \"" + fip_fip + "\""
                            logging.debug (fip)
                        except:
                            logging.debug ("no load balancer")

                        logging.debug(response)
                         
                    response = response + "\"name\": \"" + cnf_name + "\","
                    response = response + "\"endpoints\": [{"
                    response = response + "\"id\": \"" + "floating_ip" + "\"," 
                    response = response + "\"type\": \"" + "floating_ip" + "\","    
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
                                response = response + "{\"id\": \"" + port_id + "\","
                                response = response + "\"type\": \"" + port_type + "\","
                                response = response + "\"address\": \"" + port_ip + "\"},"                                    
                            response_port = response[:-1]
                            response = response_port + "]"
                response_2 = response[:-1]                
                response_2 = response_2 + "]}]}"

            if k8s == "k8s":
                logging.debug (k8s)
                response_k8s_2 = response_k8s[:-1]
                response_2 = response_k8s[:-1]
                response = response_2 + "]}"
                response_str_replaced = response.replace("[,","[") 
                response_str_replaced_2 = response_str_replaced.replace("},,","},") 
                logging.debug (response_str_replaced_2)
                return response_str_replaced_2

            response_str_replaced = response_2.replace("[,","[") 
            response_str_replaced_2 = response_str_replaced.replace("],","]},") 
            logging.debug (response_str_replaced_2)
            return response_str_replaced_2
        
        if my_type == 'osm':
            instance_request = self.instantiationStatus(id) 
            logging.debug (instance_request) 
            instance_request_json =  json.loads(instance_request)
            ns_id = instance_request_json['ns-instance-config-ref']
            logging.debug (ns_id)

            response = "{\"ns_instance_uuid\": \"" + ns_id + "\","
            response = response + "\"platform_type\": \"osm\","
            response = response + "\"functions\": ["

            vnfr_array = instance_request_json['constituent-vnfr-ref']
            logging.debug (vnfr_array)
            response_functions = " "
            for vnfr_id in vnfr_array:
                logging.debug ("FUCNTIONS")
                logging.debug(vnfr_id)
                response_function = "{\"id\": \"" + vnfr_id + "\", \"function_type\": " + "\"vnf\","                

                function_request = self.functionRecordOSM(vnfr_id)
                function_request_json =  json.loads(function_request)
                logging.debug (function_request_json)
                vnfd_name = function_request_json['vnfd-ref']                
                response_function = response_function + "\"name\": \"" + vnfd_name + "\","
                response_function = response_function + "\"endpoints\": ["
                vdur = function_request_json['vdur']                                
                logging.debug (vdur)
                for vdu in vdur:
                    interfaces = vdu['interfaces']
                    logging.debug (interfaces)
                    for interface in interfaces:                       
                        logging.debug (interface)
                        address = interface['ip-address']
                        logging.debug (address)
                        
                        #name = interface['name']
                        name = interface['ns-vld-id']

                        type = interface['name']
                        logging.debug (name)
                        response_interface = "{\"name\": \"" + name + "\", \"type\": \"" + type + "\",\"address\":\"" + address + "\"" + "},"

                        response_function = response_function + response_interface

                response_function_2 = response_function[:-1]
                response_function_2 = response_function_2 + "]},"

                logging.debug("function-----function")
                logging.debug (response_function_2)
                response_functions = response_functions + response_function_2

            response_functions_2 = response_functions[:-1] 

            response_functions = response_functions_2 + "]"
            
            response = response + response_functions
            response = response + "}"
            logging.debug (response)
            return response

    def functionRecordOSM(self, vnfr_id):
        url = self.getHostIp()
        token = self.getOSMToken(vnfr_id)
        logging.debug (token)
        url = url + ':9999/osm/nslcm/v1/vnf_instances'
        url_2 = url.replace("http","https")
        status_ns = "curl  --insecure  -H \"Content-type: application/yaml\"  -H \"Accept: application/json\" -H \"Authorization: Bearer "
        status_ns_2 = status_ns +token + "\" "
        status_ns_3 = status_ns_2 + " " + url_2 + "/" + vnfr_id          
        logging.debug (status_ns_3)
        vnfr = subprocess.check_output([status_ns_3], shell=True)
        vnfr = subprocess.check_output([status_ns_3], shell=True)
        logging.debug (vnfr)
        return (vnfr)                  

    def wait_for_instantiation(self,id):
        logging.info("wait for instantiation starts")
        time.sleep(2)
        status = None
        while status == None:
            status =  self.getRequestStatus(id)
            logging.debug (status)
            if status == None:
                time.sleep(7)
        while status == 'NEW':
            status =  self.getRequestStatus(id)
            logging.debug (status)
            if status == 'NEW':
                time.sleep(7)        
        while status == 'INSTANTIATING':
            status =  self.getRequestStatus(id)
            logging.debug (status)
            if status == 'INSTANTIATING':
                time.sleep(7)  
        if status == 'ERROR':
            status =  self.getRequestError(id)
        logging.debug(status)
        return status
        
    def getRequestError(self,id):
        logging.info("get request status starts")        
        status_call = self.instantiationStatus(id)
        logging.debug(status_call)
        instantiation_request_json_dumps = json.dumps(status_call)
        logging.debug (instantiation_request_json_dumps)
        instantiation_request_json = json.loads(status_call)
        try:
            status = instantiation_request_json['error']
            logging.debug(status)
            return (status)
        except:
            msg = "{\"error\": \"the record's status has no value\"}"
            return (msg) 


    def getRequestStatus(self,id):
        logging.info("get request status starts")        
        status_call = self.instantiationStatus(id)
        logging.debug(status_call)
        instantiation_request_json_dumps = json.dumps(status_call)
        logging.debug (instantiation_request_json_dumps)
        instantiation_request_json = json.loads(status_call)
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
        logging.debug (content)
        name = content['service_name']
        vendor = content['service_vendor']
        version = content['service_version']        
        callback = content['callback']
        package_id = self.getVnVPackagebyId(name,vendor,version)        
        download_pkg = self.downloadPackageTGO(package_id)
        download_pkg_json = json.loads(download_pkg)        
        package_path = download_pkg_json['package']        
        upload_pkg = self.uploadPackage(package_path)  
        logging.debug(upload_pkg)
        return upload_pkg     


    def uploadPackageStatus(self,process_uuid):

        status = None
        logging.info("uploadPackageStatusstarts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   

        sp_host_2 = self.getHostIp()
        url = sp_host_2 + ':32002/api/v3/packages/status/' + process_uuid            
        logging.info(process_uuid)
        logging.info(url)           
        try:
            upload_status_curl = requests.get(url, headers=JSON_CONTENT_HEADER) 
            logging.debug(upload_status_curl)
            logging.debug (upload_status_curl.text)
            upload_status_curl_json = json.loads(upload_status_curl.text)        
            logging.debug(upload_status_curl_json)
            status = upload_status_curl_json['package_process_status']
            return status
        except:
            msg = "{\"error\": \"error checking the status of the uploaded package\"}"
            return msg  

    def instantiateService(self,request): 
        logging.info("instantiate service starts")
        content = request.get_json()
        logging.debug (content)
        name = content['service_name']
        vendor = content['service_vendor']
        version = content['service_version']        
        callback = content['callback']
        vnv_service_id = None
        package_id = None
        download_pkg = None
        package_path = None
        thing = None
        service_id = None
        upload_pkg = None
        package_uploaded = False

        my_type =  self.getDBType()      
        if my_type == 'sonata':
            
            ### package operations
            try:
                vnv_service_id = self.getVnVServiceId(name,vendor,version)
            except:
                msg = "{\"error\": \"error getting the service from the VnV Catalog\"}"
                return msg   

            try: 
                package_id = self.getPackageIdfromServiceId(vnv_service_id)
                logging.debug (package_id)
            except:
                msg = "{\"error\": \"error getting the package from the VnV Catalog\"}"
                return msg   
            
            try:
                download_pkg = self.downloadPackageTGO(package_id)
                logging.debug (download_pkg)            
                download_pkg_json = json.loads(download_pkg)
                logging.debug (download_pkg_json)
                package_path = download_pkg_json['package']
                logging.debug (package_path)
            except:
                msg = "{\"error\": \"error downloading the package from the VnV Catalog\"}"
                return msg                  
            
            ###### commented for try test ffor when the service already exists in the SP
            try:
                service_id = self.getServiceId(name,vendor,version)
                if service_id:
                    logging.debug("The Service is already in the SP")
            except:
                logging.debug("The Service is not in the SP  ") 
                upload_pkg = self.uploadPackage(package_path)
                package_uploaded = True
                logging.debug (upload_pkg)
                upload_pkg_json =  json.loads(upload_pkg)
                upload_pkg_json_process_uuid =  upload_pkg_json['package_process_uuid']
                upload_pkg_status = self.uploadPackageStatus(upload_pkg_json_process_uuid)
                logging.debug (upload_pkg_status)

                while upload_pkg_status == 'running':
                    upload_pkg_status = self.uploadPackageStatus(upload_pkg_json_process_uuid)                    
                    logging.debug (upload_pkg_status)
                    if upload_pkg_status == 'running':
                        time.sleep(3)  

   

            ### service operations
            try:
                upload_pkg = self.uploadPackage(package_path)  
                package_uploaded = True
                logging.debug (upload_pkg)
                upload_pkg_json =  json.loads(upload_pkg)
                upload_pkg_json_process_uuid =  upload_pkg_json['package_process_uuid']
                upload_pkg_status = self.uploadPackageStatus(upload_pkg_json_process_uuid)
                
                while upload_pkg_status == 'running':
                    upload_pkg_status = self.uploadPackageStatus(upload_pkg_json_process_uuid)                    
                    logging.debug (upload_pkg_status)
                    if upload_pkg_status == 'running':
                        time.sleep(3)                 
            except:
                logging.error ("Error uploading package to the SP")
            try:
                service_id = self.getServiceId(name,vendor,version)
                logging.debug (service_id)
            except:
                logging.error ("The service is not in the SP. Was the package uploaded?")

            time.sleep(5)
            try:
                instance_name = content['instance_name']
            except:
                logging.debug("No instance name found")

            instantiate_str = "{\"service_uuid\": \"" + service_id + "\", \"name\": \"" + instance_name + "\"}"
            logging.debug (instantiate_str)

            instantiation_call = None
            try:
                instantiation_call = self.instantiation(instantiate_str)  
                logging.debug (instantiation_call)     
            except:
                msg = "{\"error\": \"error in the instantiation process, check the SP logs\"}"
                return msg  
            
            logging.debug (instantiation_call)
            try:
                _thread.start_new_thread(self.SonataInstantiateCallback, (callback,instantiation_call))
            except:
                msg = "{\"error\": \"error in the instantiation process, callback aborted\"}"
                return msg                 
            
            instantiation_call_str = instantiation_call.__str__()
            instantiation_call_str_replaced = instantiation_call_str.replace("'","\"")
            instantiation_call_str_replaced_2 = instantiation_call_str_replaced[1:]

            #package_id = self.getSPPackageIdfromServiceId(service_id)
            string_inicial = "{\"package_id\": \"" + package_id + "\","
            string_inicial = string_inicial + "\"package_uploaded\" : \"" + package_uploaded.__str__() + "\","
            logging.debug(string_inicial)

            request_response = string_inicial + instantiation_call_str_replaced_2

            logging.debug(request_response)   
            return (request_response)	
	

        if my_type == 'osm':
            logging.debug("This SP is osm")
            service_id = None
            package_id = None
            package_path = None
            vnv_service_id = None

            logging.debug ("instantion for osm SPs stars")

            ### package operations
                        
            vnv_service_id = self.getVnVOSMServiceId(name,vendor,version)
            package_id = self.getPackageIdfromServiceId(vnv_service_id)            
            logging.debug (package_id)
            download_pkg = self.downloadPackageTGO(package_id)
            logging.debug (download_pkg)            
            download_pkg_json = json.loads(download_pkg)
        
            download_pkg = self.downloadPackageTGO(package_id)
            download_pkg_json = json.loads(download_pkg)        
            package_path_downloaded = download_pkg_json['package'] 

            unzip = self.unzipPackage(package_path_downloaded)  

            logging.debug(unzip)       
            
            #package_path = '/app/packages/' + package_id
            package_path = unzip
            
            #package_path = '/home/luis/Escritorio/cirros/tgos_osm/basic_osm'
            logging.debug (package_path)
            
            try:
                # verify if the service is in the SP
                service_id = self.getOSMServiceId(name,vendor,version)
                logging.debug (service_id)
                if service_id == 'error':
                    logging.debug("The Service is already in the SP")
                    raise Exception('The Service descriptor is in the SP or the list is empty') 
            except:
                logging.debug:("The Service is not in the SP  ") 
                # if the service is not in the SP, we need to upload it
                functions_array = self.createFunctionsArray(package_path)
                services_array = self.createServicesArray(package_path)
                
                for function in functions_array:
                    function_str = "{\"function\": \"" + function + "\"}"
                    logging.debug (function_str)                                        
                    function_json = json.loads(function_str.__str__())
                    logging.debug (function_json)
                    logging.debug (function_json['function'])
                    function_file_path = function_json['function']
                   
                    upload_function = self.uploadOSMFunction(function_file_path)
                    logging.debug (upload_function)
                
                for service in services_array:
                    service_str = "{\"service\": \"" + service + "\"}"

                    logging.debug (service_str)                                        
                    service_json = json.loads(service_str.__str__())
                    logging.debug (service_json)
                    logging.debug (service_json['service'])
                    service_file_path = service_json['service']

                    upload_service = self.uploadOSMService(service_file_path)
                    logging.debug (upload_service)
                    
                    service_id = self.getUploadedOSMServiceId(upload_service)
                    logging.debug ("THIS IS THE NEW UPLOADED SERVICE ID")
                    logging.debug (service_id)
                    #return service_id
                
                package_uploaded = True
                
            time.sleep(2)
            

            #return "hola"
            
            ## INSTANCIANDO
            nsd_name = service_id
            ns_name = service_id
            vim_account = self.getVimAccount()

            logging.debug (nsd_name)
            logging.debug (ns_name)
            logging.debug (vim_account)            

            instantiate_str = "{\"nsd_name\": \"" + nsd_name + "\", \"ns_name\": \"" + ns_name + "\", \"vim_account\": \"" + vim_account + "\"}"
            logging.debug ("THIS IS THE INSTANTIATE STRING FOR OSM")
            logging.debug ("aaaaaaaaaaa")

            
            logging.debug(instantiate_str)


            logging.debug ("aaaaaaaaaaa")

            instantiation_call = self.instantiation(instantiate_str)    
            logging.debug (instantiation_call)

            _thread.start_new_thread(self.OSMInstantiateCallback, (callback,instantiation_call))

            instantiation_call_str = instantiation_call
            logging.debug (instantiation_call_str)   
            instantiation_call_json = json.loads(instantiation_call_str)  
            logging.debug (instantiation_call_json)
            instantiation_id = instantiation_call_json['id']
            logging.debug (instantiation_id) 

            string_inicial = "{\"package_id\": \"" + package_id + "\","                
            string_inicial = string_inicial + "\"package_uploaded\" : \"" + package_uploaded.__str__() + "\","                            
            request_response = string_inicial + "\"id\": \"" + instantiation_id + "\"}"

            logging.debug (request_response)
            logging.debug(request_response)   
            return (request_response)	            
            
            


    def SonataInstantiateCallback(self,callback,instantiation_call):
        logging.info("sonata instantiate callback starts")
        logging.debug (instantiation_call)
        instance_status = None

        try:
            instantiation_request_json_dumps = json.dumps(instantiation_call)
            logging.debug (instantiation_request_json_dumps)
            instantiation_request_json = json.loads(instantiation_call)
            logging.debug (instantiation_request_json)
            logging.debug (instantiation_request_json['id'])
            instantiation_request_id = instantiation_request_json['id']        
            logging.debug (instantiation_request_id)
            time.sleep(2)
            instance_status = self.wait_for_instantiation(instantiation_request_id)
            logging.debug (instance_status)
        except:
            msg = "{\"error\": \"error getting request status\"}"

            msg_str = msg.__str__()
            callback_post = "curl -X POST --insecure -H 'Content-type: application/json'" + " --data '" +  msg_str  +  "' " + callback        
            logging.debug (callback_post)		
            call = subprocess.check_output([callback_post], shell=True)
            logging.debug(call)	

            return msg  
            

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
            logging.debug (info_monitoring) 
            info_monitoring_str = info_monitoring.__str__()
            monitoring_string_replaced = info_monitoring_str.replace("'","\"")        
            monitoring_callback_post = "curl -X POST --insecure -H 'Content-type: application/json'" + " --data '" +  monitoring_string_replaced  +  "' " + monitoring_callback        
            logging.debug (monitoring_callback_post)		
            call_mon = subprocess.check_output([monitoring_callback_post], shell=True)            



        if instance_status == 'ERROR': 
            instantiation_request_json_dumps = json.dumps(instantiation_call)
            logging.debug (instantiation_request_json_dumps)
            instantiation_request_json = json.loads(instantiation_call)
            logging.debug (instantiation_request_json)
            logging.debug (instantiation_request_json['id'])
            instantiation_request_id = instantiation_request_json['id']        
            logging.debug (instantiation_request_id)
            time.sleep(2)
            inst_error = self.getRequestError(instantiation_request_id)    

            logging.error ("The request is in error status")
            logging.error (inst_error)
            error_string = inst_error.__str__()
            logging.error (error_string)
            try:
                callback_post = "curl -X POST --insecure -H 'Content-type: application/json'" + " --data '{\"error\": \"" + error_string + "\"}' " + callback        
                logging.debug (callback_post)		
                call = subprocess.check_output([callback_post], shell=True)
                logging.debug(call)

                monitoring_callback = self.getMonitoringURLs()
                monitoring_callback_post = "curl -X POST --insecure -H 'Content-type: application/json'" + " --data '{\"error\": \"" + inst_error + "\"}' " + monitoring_callback	                        
                logging.debug (monitoring_callback_post)		
                call_mon = subprocess.check_output([monitoring_callback_post], shell=True)  

            except:
                logging.error ("error sending the instantiation error callbacks")

        logging.info ("sonata instantiate callback ends")        


    def instantiateServiceTest(self,request): 
        logging.info("instantiate service starts")
        content = request.get_json()        
        logging.debug (content)
        name = content['service_name']
        vendor = content['service_vendor']
        version = content['service_version']        
        callback = content['callback']
        my_type =  self.getDBType()  
        package_uploaded = False

        service_id = None   
        if my_type == 'sonata':
               ### service operations
            service_id = self.getServiceId(name,vendor,version)
            logging.debug ("this is the service_id")
            logging.debug (service_id)
            time.sleep(5)
            try:
                instance_name = content['instance_name']
            except:
                logging.debug("No instance name found")

            instantiate_str = "{\"service_uuid\": \"" + service_id + "\", \"name\": \"" + instance_name + "\"}"
            logging.debug (instantiate_str)

            instantiation_call = None
            try:
                instantiation_call = self.instantiation(instantiate_str)  
                logging.debug (instantiation_call)     
            except:
                msg = "{\"error\": \"error in the instantiation process, check the SP logs\"}"
                return msg  
            
            logging.debug (instantiation_call)
            _thread.start_new_thread(self.SonataInstantiateCallback, (callback,instantiation_call))
            
            instantiation_call_str = instantiation_call.__str__()
            instantiation_call_str_replaced = instantiation_call_str.replace("'","\"")
            instantiation_call_str_replaced_2 = instantiation_call_str_replaced[1:]

            package_id = self.getSPPackageIdfromServiceId(service_id)
            string_inicial = "{\"package_id\": \"" + package_id + "\","
            request_response = string_inicial + instantiation_call_str_replaced_2

            logging.debug(request_response)   
            return (request_response)

        if my_type == 'osm':
            logging.debug("This SP is osm")
            service_id = None
            package_id = None
            package_path = None
            vnv_service_id = None

            print ("instantion for osm SPs stars")

            ### package operations
            '''          
            vnv_service_id = self.getVnVOSMServiceId(name,vendor,version)
            package_id = self.getPackageIdfromServiceId(vnv_service_id)            
            logging.debug (package_id)
            download_pkg = self.downloadPackageTGO(package_id)
            logging.debug (download_pkg)            
            download_pkg_json = json.loads(download_pkg)
        
            download_pkg = self.downloadPackageTGO(package_id)
            download_pkg_json = json.loads(download_pkg)        
            package_path_downloaded = download_pkg_json['package'] 

            unzip = self.unzipPackage(package_path_downloaded)  

            print(unzip)       
            
            #package_path = '/app/packages/' + package_id
            package_path = unzip
            '''
            package_path = '/home/luis/Escritorio/cirros/tgos_osm/basic_osm'
            logging.debug (package_path)
            
            try:
                # verify if the service is in the SP
                service_id = self.getOSMServiceId(name,vendor,version)
                logging.debug (service_id)
                if service_id == 'error':
                    logging.debug("The Service is already in the SP")
                    raise Exception('The Service descriptor is in the SP or the list is empty') 
            except:
                logging.debug:("The Service is not in the SP  ") 
                # if the service is not in the SP, we need to upload it
                functions_array = self.createFunctionsArray(package_path)
                services_array = self.createServicesArray(package_path)
                
                for function in functions_array:
                    function_str = "{\"function\": \"" + function + "\"}"
                    logging.debug (function_str)                                        
                    function_json = json.loads(function_str.__str__())
                    logging.debug (function_json)
                    logging.debug (function_json['function'])
                    function_file_path = function_json['function']
                   
                    upload_function = self.uploadOSMFunction(function_file_path)
                    logging.debug (upload_function)
                
                for service in services_array:
                    service_str = "{\"service\": \"" + service + "\"}"

                    logging.debug (service_str)                                        
                    service_json = json.loads(service_str.__str__())
                    logging.debug (service_json)
                    logging.debug (service_json['service'])
                    service_file_path = service_json['service']

                    upload_service = self.uploadOSMService(service_file_path)
                    logging.debug (upload_service)
                    
                    service_id = self.getUploadedOSMServiceId(upload_service)
                    logging.debug ("THIS IS THE NEW UPLOADED SERVICE ID")
                    logging.debug (service_id)
                    #return service_id
                package_uploaded = True
                
            time.sleep(2)
            

            #return "hola"
            
            ## INSTANCIANDO
            nsd_name = service_id
            ns_name = service_id
            vim_account = self.getVimAccount()

            logging.debug (nsd_name)
            logging.debug (ns_name)
            logging.debug (vim_account)            

            instantiate_str = "{\"nsd_name\": \"" + nsd_name + "\", \"ns_name\": \"" + ns_name + "\", \"vim_account\": \"" + vim_account + "\"}"
            logging.debug ("THIS IS THE INSTANTIATE STRING FOR OSM")
            logging.debug ("aaaaaaaaaaa")
            
            logging.debug(instantiate_str)

            instantiation_call = self.instantiation(instantiate_str)    
            logging.debug (instantiation_call)

            _thread.start_new_thread(self.OSMInstantiateCallback, (callback,instantiation_call))

            instantiation_call_str = instantiation_call
            logging.debug (instantiation_call_str)   
            instantiation_call_json = json.loads(instantiation_call_str)  
            logging.debug (instantiation_call_json)
            instantiation_id = instantiation_call_json['id']
            logging.debug (instantiation_id)
            
            string_inicial = "{\"package_id\": \"" + "111111111111" + "\","                
            string_inicial = string_inicial + "\"package_uploaded\" : \"" + package_uploaded.__str__() + "\","
            string_replaced = string_inicial.replace("\"True\"","true")                            
            request_response = string_replaced + "\"id\": \"" + instantiation_id + "\"}"            
            
            logging.debug (request_response)     

            logging.debug(request_response)   
            return (request_response)	            
                 

    def getOSMServiceId(self,name,vendor,version):
        logging.info("get OSM service id starts")
        service_id = None 
        exists = 'NO'   
        sp_host_2 = self.getHostIp()
        token = self.getOSMToken(request)
        logging.debug (token)        
        url = sp_host_2 + ':9999/osm/nsd/v1/ns_descriptors_content'
        url_2 = url.replace("http","https")
        logging.debug (url_2)        
        nsds = "curl  --insecure -H \"Content-type: application/json\"  -H \"Accept: application/json\" -H \"Authorization: Bearer "
        nsds_2 = nsds +token + "\"  " + url_2 
        logging.debug (nsds_2)
        response = None

        try:
            logging.debug ("loading descriptrs list:")
            response = subprocess.check_output([nsds_2], shell=True)
            logging.debug (response)
        except:
            service_id = "error"
            return service_id        

        jjson = json.loads(response)
        logging.debug (jjson)

        logging.debug (name)
        logging.debug (vendor)
        logging.debug (version)

        for x in jjson:
            logging.debug (x)
            logging.debug (x['name'])
            logging.debug (x['vendor'])
            logging.debug (x['version'])
            logging.debug (x['_id'])
        
            if ( x['name'] == name and x['vendor'] == vendor and x['version'] == version ):
                logging.debug(x['name'])
                service_id = x['_id']
                exists = 'YES' 
        
        if service_id == None: 
            service_id = "error"

        return service_id

    def getUploadedOSMServiceId(self,upload_service):
        logging.debug ("This is the upload service response:")
        logging.debug (upload_service)
        service_id = None
        json = yaml.load(upload_service) 
        service_id = json['id']
        logging.debug (service_id)
        return service_id

    def createFunctionsArray(self,package_path):
        functions_array = None
        files = []
        functions_array = []
        services_array = []
        for r,d,f in os.walk(package_path):
            for file in f:
                    if '.yaml' in file:
                        files.append(os.path.join(r,file))
                    if '.yml' in file:
                        files.append(os.path.join(r,file))                  
        for f in files:
            logging.debug (f)
            with open(f) as file_in_array:
                    file = yaml.load(file_in_array)      
                    #print (file)
                    try:
                        vnfd = file['vnfd:vnfd-catalog']
                        #print ("this file is an osm vnfd")
                        functions_array.append(f)
                    except:
                        try:
                                nsd = file['nsd:nsd-catalog']
                                #print ("this file is an osm nsd")
                                services_array.append(f)                  
                        except:
                                logging.debug ("this files is not an OSM vnfd or nsd")
        logging.debug ("osm functions list:")
        for func in functions_array:
            logging.debug (func)
        logging.debug ("osm services list:")
        for serv in services_array:
            logging.debug (serv)                
        return functions_array

    def createServicesArray(self,package_path):
        services_array = None
        files = []
        functions_array = []
        services_array = []
        for r,d,f in os.walk(package_path):
            for file in f:
                    if '.yaml' in file:
                        files.append(os.path.join(r,file))
                    if '.yml' in file:
                        files.append(os.path.join(r,file))                  
        for f in files:
            logging.debug (f)
            with open(f) as file_in_array:
                    file = yaml.load(file_in_array)      
                    #print (file)
                    try:
                        vnfd = file['vnfd:vnfd-catalog']
                        #print ("this file is an osm vnfd")
                        functions_array.append(f)
                    except:
                        try:
                                nsd = file['nsd:nsd-catalog']
                                #print ("this file is an osm nsd")
                                services_array.append(f)                  
                        except:
                                logging.debug ("this files is not an OSM vnfd or nsd")
        logging.debug ("osm functions list:")
        for func in functions_array:
            logging.debug (func)
        logging.debug ("osm services list:")
        for serv in services_array:
            logging.debug (serv)                
        return services_array



    def getPackageIdfromServiceId (self,service_id):
        logging.info("get package id from service id starts")
        package_id = None        
        vnv_packages = self.getVnVPackages()
        vnv_packages_json = json.loads(vnv_packages)
        logging.debug (vnv_packages_json)        

        for package in vnv_packages_json:
            logging.debug (package['uuid'])
            package_pd = package['pd']
            package_content = package_pd['package_content']
            #logging.debug (package_content)
            for pc in package_content:
                nsd_uuid = pc['uuid']
                logging.debug (nsd_uuid)
                if nsd_uuid == service_id:                    
                    package_id = package['uuid']

                    logging.debug (package_id)
                    logging.info("get package id from service id finishing")
                    return package_id
        
        if package_id == None:
            msg = "error getting the id from the packages list"
            return msg
        

    def backupgetPackageIdfromServiceId (self,service_id):
        logging.info("get package id from service id starts")
        package_id = None
        correct_package = None
        vnv_packages = self.getVnVPackages()
        vnv_packages_json = json.loads(vnv_packages)
        logging.debug (vnv_packages_json)        

        for package in vnv_packages_json:
            package_pd = package['pd']
            package_content = package_pd['package_content']
            #logging.debug (package_content)
            for pc in package_content:
                nsd_uuid = pc['uuid']
                #logging.debug (nsd_uuid)
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
        logging.debug (vnv_packages)
        vnv_packages_json = json.loads(vnv_packages)
        logging.debug (vnv_packages_json)        

        for package in vnv_packages_json:
            logging.debug (package)
            package_pd = package['pd']
            logging.debug (package_pd)            
            package_content = package_pd['package_content']
            logging.debug (package_content)
            
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
            response = requests.get(url,headers=JSON_CONTENT_HEADER)
            response_json = response.content
            jjson = json.loads(response_json)
            for x in jjson:
                logging.debug(x)
                logging.debug(x)
                try:
                    if ( x['nsd']['name'] == name and x['nsd']['vendor'] == vendor and x['nsd']['version'] == version ) :
                        logging.debug("same name")
                        uuid = x['uuid']
                        logging.debug(uuid)  
                except:
                    logging.debug("this descriptor is not a Sonata one")

        logging.debug(uuid)
        return uuid     

    def getVnVOSMServiceId(self,name,vendor,version):    
        logging.info("get vnv service id starts")
        uuid = None
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}  
                 
        url = 'http://pre-int-vnv-bcn.5gtango.eu:32002/api/v3/services'  
        response = requests.get(url,headers=JSON_CONTENT_HEADER)
        logging.debug (response)
        response_json = response.content
        jjson = json.loads(response_json)
        for x in jjson:
            print(x)
            logging.debug(x)
            try:
                osm_name = x['nsd']['nsd:nsd-catalog']['nsd']['name']
                logging.debug("OSM service descriptor, checking if is the one we are searching:") 
                if ( x['nsd']['nsd:nsd-catalog']['nsd']['name'] == name and x['nsd']['nsd:nsd-catalog']['nsd']['vendor'] == vendor and x['nsd']['nsd:nsd-catalog']['nsd']['version'] == version ) :
                    logging.debug("same name")
                    uuid = x['uuid']
                    logging.debug(uuid)  
            except:
                logging.debug("this descriptor is not a OSM one")       

        logging.debug(uuid)
        return uuid    


    def getVnVOSMServiceIdTEST(self,name,vendor,version):    
        logging.info("get vnv service id starts")
        uuid = None
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}  
                 
        url = 'http://pre-int-vnv-bcn.5gtango.eu:32002/api/v3/services'  
        response = requests.get(url,headers=JSON_CONTENT_HEADER)
        logging.debug (response)
        response_json = response.content
        jjson = json.loads(response_json)
        for x in jjson:
            print(x)
            logging.debug(x)
            try:
                osm_name = x['nsd']['nsd:nsd-catalog']['nsd']['name']
                logging.debug("OSM service descriptor, checking if is the one we are searching:") 
                if ( x['nsd']['nsd:nsd-catalog']['nsd']['name'] == name and x['nsd']['nsd:nsd-catalog']['nsd']['vendor'] == vendor and x['nsd']['nsd:nsd-catalog']['nsd']['version'] == version ) :
                    logging.debug("same name")
                    uuid = x['uuid']
                    logging.debug(uuid)  
            except:
                logging.debug("Sonata services descriptor, trying next")        

        logging.debug(uuid)
        return uuid          


    def deletePackagefromService(self,name,vendor,version):    
        logging.info("delete package from service starts")
        JSON_CONTENT_HEADER = {'Content-Type':'application/json'}   
        response = None        
        my_type =  self.getDBType()
        if my_type == 'sonata':    
            try:
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
            except:
                msg = "{\"error\": \"error deleting the package in the SP from the service info\"}"
                return msg              
        

    def getOSMVIMInfo(self,vim_id):
        logging.info("get OSM get vim info starts")
        service_id = None 
        exists = 'NO'   
        sp_host_2 = self.getHostIp()
        token = self.getOSMToken(request)
        logging.debug (token)  
        url = sp_host_2.replace("http","https")      
        url_2 = url + ':9999/osm//admin/v1/vim_accounts/' + vim_id      
        vim_info = "curl  --insecure -H \"Content-type: application/json\"  -H \"Accept: application/json\" -H \"Authorization: Bearer "
        vim_info_2 = vim_info +token + "\"  " + url_2 
        logging.debug (vim_info_2)       

        response = subprocess.check_output([vim_info_2], shell=True)
        logging.debug (response)
        return response

    def getOSMVIMInfoURL(self,vim_info):
        logging.info("get OSM get vim info url starts")
        
        content = json.loads(vim_info)
        logging.debug (content)
        vim_url_full = content['vim_url']
        vim_url_array = vim_url_full.split(":")
        vim_url_center = vim_url_array[1]
        return vim_url_center[2:]

        