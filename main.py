#!/usr/bin/python

from flask import Flask, request, jsonify, render_template
import os, sys, logging, json, argparse 
from configparser import ConfigParser

import requests

from adapters import sonata
from adapters import osm
from adapters import adapter
from models import utils
from models import users
from models import serviceplatform

import psycopg2


app = Flask(__name__)


################### Login Tests ##################
#@app.route('/hello')
#def hello():
#   r = requests.get('http://www.google.com')
#   return r.text
@app.route('/login')
def login():
   #login = requests.post('http://tng-gtk-usr:4567/login')
   login = requests.post('http://172.18.0.3:4567/login')
   return jsonify(login)


################### get all users from DB ##################
@app.route('/users', methods=['GET'])
def getAllUsers():
    allusers = users.User("prueba","prueba","prueba")
    return allusers.getUsers()

################### get all SPs from DB ##################
@app.route('/sps', methods=['GET'])
def getAllServicePlatforms():
    sps = serviceplatform.ServicePlatform("name", "host", "type", "service_token")
    return sps.getServicePlatforms()

################### register user ##################
@app.route('/users', methods=['POST'])
def registerNewUser():    
    print (request.is_json)
    content = request.get_json()
    print (content)
    newUser = users.User(content['username'],content['password'],content['service_platform'])    
    return newUser.registerUser()

################### register service platform ##################
@app.route('/sps', methods=['POST'])
def registerNewServicePlatform():    
    print (request.is_json)
    content = request.get_json()
    print (content)
    newSP = serviceplatform.ServicePlatform(content['name'],content['host'],content['type'],content['service_token'])    
    return newSP.registerServicePlatform()

################### get 1 service platform by name ##################
@app.route('/sps/<name>', methods=['GET'])
def getServicePlatform(name):      
    newSP = serviceplatform.ServicePlatform(name,'host','type','service_token')
    return newSP.getServicePlatflorm()

################### get service platforms by type ##################
@app.route('/sps/type/<type>', methods=['GET'])
def getServicePlatformByType(type):     
    newSP = serviceplatform.ServicePlatform('name','host',type,'service_token')
    return newSP.getServicePlatflormsByType()    

################### get 1 user ##################
@app.route('/users/<username>', methods=['GET'])
def getUser(username):     
    newUser = users.User(username,'password','sp')
    return newUser.getUser()

################### get service platform token ##################
@app.route('/sps/<name>/token', methods=['GET'])
def getServicePlatformToken(name):     
    newSP = serviceplatform.ServicePlatform(name,'host','type','service_token')
    return newSP.getServicePlatformToken()    





########################################## API Actions #########################################
#Check the connection to the PM component
@app.route('/pings', methods=['GET'])
def getPings():
    ping_response  = {'alive_since': '2018-07-18 10:00:00 UTC'}
    return jsonify(ping_response), 200

########################################## API Actions #########################################
#GET the Platform Manager description
@app.route('/pm', methods=['GET'])
def getPm():
    pm_response  = {'Description': 'VnV Platform Manager'}
    return jsonify(pm_response), 200    


########################################## ADAPTERS Actions #########################################
#test for creating a new Adapter
@app.route('/adapters')
def getAdapters():
    prueba = adapter.Adapter("nameTest","localhostTest", "typeTest")
    prueba.host = "my_new_host"
    prueba.name = "my_new_name"
    prueba.type = "my_new_type"
    return prueba.host + " " + prueba.name + " " + prueba.type 

###### sonata gets ########
@app.route('/adapters/sonata/users', methods=['GET'])
def getSonUsers():
    sonatas = sonata.Sonata("nameTest","localhostTest", "typeTest")
    return sonatas.getUsers()
@app.route('/adapters/sonata/sps')
def getSonataSPs():
    sonatas = sonata.Sonata("nameTest","localhostTest", "typeTest")
    return sonatas.getSPs()
  

#sonata adapter test
@app.route('/sonata/services')
def getServices():
    prueba = sonata.Sonata("sonata-1","http://pre-int-sp-ath.5gtango.eu:32002/api/v3", "sonata")    
    return prueba.getServices()
@app.route('/sonata/packages')
def getPackages():
    prueba = sonata.Sonata("sonata-1","http://pre-int-sp-ath.5gtango.eu:32002/api/v3", "sonata")    
    return prueba.getPackages()

#osm adapter test
@app.route('/osm/services')
def getOSMServices():
    prueba = osm.Osm("osm-1","http://pre-int-sp-ath.5gtango.eu:32002/api/v3", "sonata")    
    return prueba.getServices()    
@app.route('/osm/packages')
def getOSMPackages():
    prueba = osm.Osm("osm-1","http://pre-int-sp-ath.5gtango.eu:32002/api/v3", "sonata")    
    return prueba.getPackages()    





#MAIN FUNCTION OF THE SERVER

if __name__ == '__main__':
    #READ CONFIG
    conf_parser = argparse.ArgumentParser( description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter, add_help=True )
    conf_parser.add_argument("-c", "--conf_file", help="Specify config file", metavar="FILE", default='config.cfg')
    args, remaining_argv = conf_parser.parse_known_args()
    config = ConfigParser()
    config.read(args.conf_file)
    #db.settings = config
    #createTableUsers()
    #createTableServicePlatforms()
    createUsersObj = utils.Utils()
    createUsersObj.createTableUsers()
    createUsersObj.createTableServicePlatforms()

    
    #RUN SERVER
    app.run(debug=True, host='0.0.0.0', port=os.environ.get("SLICE_MGR_PORT"))
