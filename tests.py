#!/usr/bin/python
import configparser
Config = configparser.ConfigParser()

Config.read("db-config.cfg")
user = Config.get('database','user')
password = Config.get('database','password')
host = Config.get('database','host')
port = Config.get('database','port')
database = Config.get('database','database')
print (user, password, host, port, database)