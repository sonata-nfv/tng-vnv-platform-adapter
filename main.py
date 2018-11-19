#!/usr/bin/python

from flask import Flask, request, jsonify, render_template
import os, sys, logging, json, argparse 
from configparser import ConfigParser

import requests

from adapters import sonata
from adapters import osm
from adapters import adapter as adapter

from models import utils
from models import users


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



  







##### ADAPTER GENERIC ROUTES #####
@app.route('/adapters/<service_platform>/get_token')
def adapter_get_token(service_platform):
    if service_platform == 'sonata':
        adapter = "asasas"
        return adapter
    if service_platform == 'osm':
        token = osmclient.Client().get_token()
        return token

@app.route('/adapters/<service_platform>/ns')
def adapter_ns(service_platform):
    if service_platform == 'sonata':
        adapter = "asasas"
        return adapter
    if service_platform == 'osm':
        list = osmclient.Client().ns.list()
        return list

@app.route('/adapters/<service_platform>/ns/<name>')
def adapter_ns_name(service_platform,name):
    if service_platform == 'sonata':
        adapter = "asasas"
        return adapter
    if service_platform == 'osm':
        ns = osmclient.Client().ns.get(name)
        return ns

@app.route('/adapters/<service_platform>/ns/alarm')
def adapter_ns_alarm(service_platform):
    if service_platform == 'sonata':
        adapter = "asasas"
        return adapter
    if service_platform == 'osm':
        alarma = "aaa"
        alarm = osmclient.Client().ns.create_alarm(alarma)
        #return alarm

@app.route('/adapters/<service_platform>/nsd')
def adapter_nsd(service_platform):

    if service_platform == 'sonata':
        adapter = "asasas"
        return adapter
    if service_platform == 'osm':
        nsd = osmclient.Client().nsd.list()
        return nsd


@app.route('/adapters/<service_platform>/services')
def adapter_services(service_platform):
    if service_platform == 'sonata':
        adapter = "asasas"
        return adapter
    if service_platform == 'osm':
        nsd = 'services'
        return nsd    


##### ADAPTER GENERIC ROUTES #####
@app.route('/adapters/<service_platform>/get_type')
def adapter_get_type(service_platform):
    ad = adapter.Adapter(service_platform)
    return ad.getDBType()
    

@app.route('/adapters/<service_platform>/get_host')
def adapter_get_host(service_platform):
    ad = adapter.Adapter(service_platform)
    return ad.getDBHost()
  

@app.route('/adapters/<service_platform>/packages', methods=['GET'])
def adapter_get_packages(service_platform):
    ad = adapter.Adapter(service_platform)
    return ad.getPackages()

@app.route('/adapters/<service_platform>/packages/<name>/<vendor>/<version>', methods=['GET'])
def adapter_get_package(service_platform,name,vendor, version):
    ad = adapter.Adapter(service_platform)
    return ad.getPackage(name,vendor,version)    

@app.route('/adapters/<service_platform>/packages/<name>/<vendor>/<version>', methods=['DELETE'])
def adapter_delete_package(service_platform,name,vendor, version):
    ad = adapter.Adapter(service_platform)
    return ad.deletePackage(name,vendor,version)   

@app.route('/adapters/<service_platform>/packages/<name>/<vendor>/<version>/id', methods=['GET'])
def adapter_get_package_by_id(service_platform,name,vendor, version):
    ad = adapter.Adapter(service_platform)
    return ad.getPackagebyId(name,vendor,version)  
    

@app.route('/adapters/<service_platform>/packages', methods=['POST'])
def adapter_upload_package(service_platform):
    print (request.is_json)
    content = request.get_json()
    print (content)
    ad = adapter.Adapter(service_platform)  
    print (ad.name)         
    return ad.uploadPackage(content['package'])
    

    






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
    #createUsersObj = utils.Utils()
    #createUsersObj.createTableUsers()
    #createUsersObj.createTableServicePlatforms()

    
    #RUN SERVER
    app.run(debug=True, host='0.0.0.0', port=os.environ.get("SLICE_MGR_PORT"))
