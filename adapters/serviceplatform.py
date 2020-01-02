#!/usr/bin/python

import psycopg2
import requests

from flask import Flask, request, jsonify, render_template
import os, sys, logging, json, argparse 
from configparser import ConfigParser
from logger import TangoLogger

LOG = TangoLogger.getLogger("adapter", log_level=logging.DEBUG, log_json=True)

LOG.setLevel(logging.DEBUG)



class ServicePlatform:

    def __init__(self, name, host, type, username, password, project_name,vim_account, service_token,monitoring_urls):
        self.name = name
        self.host = host
        self.type = type
        self.username = username
        self.password = password
        self.project_name = project_name
        self.vim_account = vim_account
        self.service_token = service_token
        self.monitoring_urls = monitoring_urls




    def getServicePlatformVimAccount(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_sp = "SELECT vim_account FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_sp)
            cursor.execute(get_sp)
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



    def getServicePlatformUser(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_sp = "SELECT username FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_sp)
            cursor.execute(get_sp)
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


    def getServicePlatformMonitoringUrls(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_sp = "SELECT monitoring_urls FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_sp)
            cursor.execute(get_sp)
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



    def getServicePlatformPassword(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_sp = "SELECT password FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_sp)
            cursor.execute(get_sp)
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


    def getServicePlatformToken(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_sp = "SELECT service_token FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_sp)
            cursor.execute(get_sp)
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



    def getServicePlatflormType(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_sp = "SELECT type FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_sp)
            cursor.execute(get_sp)
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



    def getServicePlatformOLD(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_sp = "SELECT * FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (get_sp)
            cursor.execute(get_sp)
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

    def registerServicePlatform(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")            
            print (self.name)
            new_sp = "INSERT INTO service_platforms (name, host, type, username, password, project_name, vim_account, service_token,monitoring_urls) VALUES (\'" +self.name+ "\',\'" +self.host+ "\',\'" +self.type+ "\',\'" +self.username+ "\',\'" +self.password+ "\',\'" +self.project_name+ "\',\'" +self.vim_account+ "\',\'" +self.service_token+ "\',\'" +self.monitoring_urls+ "\')"
            print (new_sp)                    
            cursor.execute(new_sp)
            connection.commit()
            create_text = "New service platform registered"
            return jsonify(create_text), 200

        except (Exception, psycopg2.Error) as error :
            #print ("Error while connecting to PostgreSQL", error)
            print (error)
            exception_message = str(error)
            return exception_message, 401
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")     


    def patchServicePlatform(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")            
            print (self.name)
            #new_sp = "INSERT INTO service_platforms (name, host, type, username, password, project_name, service_token,monitoring_urls) VALUES (\'" +self.name+ "\',\'" +self.host+ "\',\'" +self.type+ "\',\'" +self.username+ "\',\'" +self.password+ "\',\'" +self.project_name+ "\',\'" +self.service_token+ "\',\'" +self.monitoring_urls+ "\')"
            new_sp = "UPDATE service_platforms SET host=\'" +self.host+ "\',type=\'" +self.type+ "\',username=\'" +self.username+ "\',password=\'" +self.password+ "\',project_name=\'" +self.project_name+ "\',vim_account=\'" +self.vim_account+ "\',service_token=\'" +self.service_token+ "\',monitoring_urls=\'" +self.monitoring_urls+ "\' WHERE name=\'" +self.name+ "\'"                
            print ("patch_string")
            print (new_sp)                    
            cursor.execute(new_sp)
            connection.commit()
            create_text = "Service platform info updated"
            return jsonify(create_text), 200

        except (Exception, psycopg2.Error) as error :
            #print ("Error while connecting to PostgreSQL", error)
            print (error)
            exception_message = str(error)
            return exception_message, 401
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")   




    def getServicePlatflormsByType(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_sp = "SELECT * FROM service_platforms WHERE type=\'" +self.type+ "\'"
            print (get_sp)
            cursor.execute(get_sp)
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




    def getServicePlatforms(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()   
            print ( connection.get_dsn_parameters(),"\n")
            #cursor.execute("SELECT * FROM service_platforms")
            #cursor.execute("SELECT to_json(row) FROM (SELECT * FROM service_platforms) row")
            sql = "SELECT row_to_json(row) FROM (SELECT * FROM service_platforms) row"
            cursor.execute(sql)
            all = cursor.fetchall()

            print (all)

            #print (json.dumps(all))

            data_json = []

            for i in all:
                data_json.append(i)
                print (i)

            response0 = json.dumps(data_json).__str__()
            response1 = response0.replace("[{","{")
            response2 = response1.replace("}]","}")
            response3 = response2.replace("[[","[")
            response4 = response3.replace("]]","]")
            

            return response4, 200 
            #return json.dumps(list(all)), 200
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")   

    def get_runtime_policies(self, host):
        LOG.debug("Getting policies from {}".format(host))
        response = requests.get("{}/api/v3/policies".format(host), verify=False)
        return response.json()

    def get_policies_sonata(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            cursor.execute("SELECT name, host FROM service_platforms WHERE type = 'sonata';")
            sonata_sps = cursor.fetchall()
            # Saving the results
            connection.commit()
            LOG.debug("Sonata sps: {}".format(sonata_sps))

            policies = []
            for name, host in sonata_sps:
                policy = self.get_runtime_policies(host)
                LOG.debug("SP {} returns the policies: {}".format(name, policy))
                policies.append({"platform_name": name, "policies": policy})

            return policies

        except (Exception, psycopg2.Error) as error:
            if connection:
                connection.rollback()
            print("Error while connecting to PostgreSQL {}".format(error))

        finally:
            #closing database connection.
            if connection:
                cursor.close()
                connection.close()

    def countServicePlatforms(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()   
            print ( connection.get_dsn_parameters(),"\n")
            #cursor.execute("SELECT * FROM service_platforms")
            #cursor.execute("SELECT to_json(row) FROM (SELECT * FROM service_platforms) row")
            #sql = "SELECT row_to_json(row) FROM (SELECT * FROM service_platforms) row"
            #cursor.execute(sql)
            #all = cursor.fetchall()

            #print (all)
            onap = 0
            sonata = 0
            osm = 0
            sql = "SELECT count(*) from service_platforms WHERE type = \'sonata\';"
            cursor.execute(sql)
            results = cursor.fetchone()
            print (results)
            print (results[0])
            if results[0]:
                sonata = results[0]

            sql = "SELECT count(*) from service_platforms WHERE type = \'osm\';"
            cursor.execute(sql)
            results = cursor.fetchone()
            print (results)
            print (results[0])
            if results[0]:
                osm = results[0]

            sql = "SELECT count(*) from service_platforms WHERE type = \'onap\';"
            cursor.execute(sql)
            results = cursor.fetchone()
            print (results)
            print (results[0])
            if results[0]:
                onap = results[0]

            json = {
                'SONATA': sonata,
                'OSM': osm,
                'ONAP': onap
                }
            json_replaced = json.__str__().replace("\'","\"")
            print (json_replaced)

            return json_replaced, 200 
            #return json.dumps(list(all)), 200
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")                      




    def getServicePlatform(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_sp_string = "SELECT * FROM service_platforms WHERE name=\'" +self.name+ "\'"
            get_sp = "SELECT row_to_json(row) FROM (" + get_sp_string + ") row"
            print (get_sp)
            cursor.execute(get_sp)
            all = cursor.fetchall()
            #return jsonify(all), 200 

            data_json = []
            for i in all:
                data_json.append(i)
                print (i)
            response0 = json.dumps(data_json).__str__()
            response1 = response0.replace("[{","{")
            response2 = response1.replace("}]","}")
            response3 = response2.replace("[{","{")
            response4 = response3.replace("}]","}")            
            return response4, 200                

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


    def deleteServicePlatform(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            delete_sp = "DELETE FROM service_platforms WHERE name=\'" +self.name+ "\'"
            print (delete_sp)
            cursor.execute(delete_sp)
            connection.commit()
            create_text = "Service platform deleted"
            return jsonify(create_text), 200   
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