#!/usr/bin/python

import psycopg2
import requests

from flask import Flask, request, jsonify, render_template
import os, sys, logging, json, argparse 
from configparser import ConfigParser

import configparser
Config = configparser.ConfigParser()
Config.read("db-config.cfg")



class Database:

    def __init__(self, file):
        Config.read("db-config.cfg")
        self.user = Config.get('database','user')
        self.password = Config.get('database','password')
        self.host = Config.get('database','host')
        self.port = Config.get('database','port')
        self.database = Config.get('database','database')

    def getUser(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table Service Platforms
            get_user = "SELECT * FROM pm_users WHERE username=\'" +self.username+ "\'"
            print (get_user)
            cursor.execute(get_user)
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
    
    def registerUser(self):
        #return self.username
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")
            #create table PM-USERS  
            #new_user = "INSERT INTO pm_users (username, password, service_platform) VALUES ('\'+ self.username + '\','\' + self.password + '\','\'+self.service_platform + '\')"
            print (self.username)
            new_user = "INSERT INTO pm_users (username, password, service_platform) VALUES (\'" +self.username+ "\',\'" +self.password+ "\',\'" +self.service_platform+ "\')"
            print (new_user)                    
            cursor.execute(new_user)
            connection.commit()
            create_text = "New user registered"
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




    def getUsers(self):
        try:
            connection = psycopg2.connect(user = "sonatatest",
                                        password = "sonata",
                                        host = "son-postgres",
                                        port = "5432",
                                        database = "gatekeeper")
            cursor = connection.cursor()   
            print ( connection.get_dsn_parameters(),"\n")
            cursor.execute("SELECT * FROM PM_USERS;")
            all = cursor.fetchall()
            return jsonify(all), 200
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")       



