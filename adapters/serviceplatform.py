#!/usr/bin/python

import psycopg2
import requests

from flask import Flask, request, jsonify, render_template
import os, sys, logging, json, argparse 
from configparser import ConfigParser




class ServicePlatform:

    def __init__(self, name, host, type, username, password, project_name,service_token,monitoring_urls):
        self.name = name
        self.host = host
        self.type = type
        self.username = username
        self.password = password
        self.project_name = project_name
        self.service_token = service_token
        self.monitoring_urls = monitoring_urls



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
            new_sp = "INSERT INTO service_platforms (name, host, type, username, password, project_name, service_token,monitoring_urls) VALUES (\'" +self.name+ "\',\'" +self.host+ "\',\'" +self.type+ "\',\'" +self.username+ "\',\'" +self.password+ "\',\'" +self.project_name+ "\',\'" +self.service_token+ "\',\'" +self.monitoring_urls+ "\')"
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