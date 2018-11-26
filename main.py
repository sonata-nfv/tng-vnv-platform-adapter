#!/usr/bin/python

from flask import Flask, request, jsonify, render_template
import os, sys, logging, json, argparse 
from configparser import ConfigParser

import requests

from adapters import sonata
from adapters import osm
from adapters import adapter as adapter
from adapters import serviceplatform as serviceplatform

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

##### SERVICE PLATFORMS ROUTES #####
@app.route('/service_platforms', methods=['GET'])
def get_sps():
    sp = serviceplatform.ServicePlatform("name","host","type","service_token")
    return sp.getServicePlatforms()

@app.route('/service_platforms', methods=['POST'])
def register_sp():
    #sp = serviceplatform.ServicePlatform("name","host","type","service_token")   
    print (request.is_json)
    content = request.get_json()
    print (content)
    sp = serviceplatform.ServicePlatform(content['name'],content['host'],content['type'],content['service_token'])
    return sp.registerServicePlatform()    



##### ADAPTER GENERIC ROUTES #####
@app.route('/adapters/<service_platform>/get_type')
def adapter_get_type(service_platform):
    ad = adapter.Adapter(service_platform)
    return ad.getDBType()
    

@app.route('/adapters/<service_platform>/get_host')
def adapter_get_host(service_platform):
    ad = adapter.Adapter(service_platform)
    return ad.getDBHost()
  

@app.route('/adapters/<service_platform>/services', methods=['GET'])
def adapter_get_services(service_platform):
    ad = adapter.Adapter(service_platform)
    return ad.getServices()

@app.route('/adapters/<service_platform>/services', methods=['POST'])
def adapter_upload_service(service_platform):
    print (request.is_json)
    content = request.get_json()
    print (content)
    ad = adapter.Adapter(service_platform)  
    print (ad.name)         
    return ad.uploadOSMService(content['service'])    

@app.route('/adapters/<service_platform>/functions', methods=['GET'])
def adapter_get_Functions(service_platform):
    ad = adapter.Adapter(service_platform)
    return ad.getFunctions()  

@app.route('/adapters/<service_platform>/functions', methods=['POST'])
def adapter_upload_function(service_platform):
    print (request.is_json)
    content = request.get_json()
    print (content)
    ad = adapter.Adapter(service_platform)  
    print (ad.name)         
    return ad.uploadOSMFunction(content['function'])    




@app.route('/adapters/<service_platform>/services/<name>/<vendor>/<version>', methods=['GET'])
def adapter_get_service(service_platform,name,vendor, version):
    ad = adapter.Adapter(service_platform)
    return ad.getService(name,vendor,version)   

@app.route('/adapters/<service_platform>/services/<name>/<vendor>/<version>/id', methods=['GET'])
def adapter_get_service_by_id(service_platform,name,vendor, version):
    ad = adapter.Adapter(service_platform)
    return ad.getServiceId(name,vendor,version)      

@app.route('/adapters/<service_platform>/services/<name>/<vendor>/<version>/instantiations', methods=['GET'])
def adapter_get_service_instantiations(service_platform,name,vendor, version):
    ad = adapter.Adapter(service_platform)
    return ad.getServiceInstantiations(name,vendor,version)       



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
    

#### SERVICES OPERATIONS #### 
@app.route('/adapters/<service_platform>/instantiations', methods=['GET'])
def serviceInstantiationsGetStatus(service_platform):
    ad = adapter.Adapter(service_platform)
    return ad.instantiationsStatus() 
 
   
@app.route('/adapters/<service_platform>/instantiations/<id>', methods=['GET'])
def serviceInstantiationGetStatus(service_platform,id):
    ad = adapter.Adapter(service_platform)
    return ad.instantiationStatus(id)

@app.route('/adapters/<service_platform>/instantiations', methods=['POST'])
def serviceInstantiation(service_platform):
    print (request.is_json)
    content = request.get_json()
    print (content)    
    ad = adapter.Adapter(service_platform)
    print (content['service_uuid'])         
    return ad.instantiation(request)    
    

@app.route('/adapters/<service_platform>/instantiations/delete', methods=['POST'])
def serviceInstantiationDelete(service_platform):
    print (request.is_json)
    content = request.get_json()
    print (content)    
    ad = adapter.Adapter(service_platform)
    print (content['service_uuid'])        
    return ad.instantiationDelete(request)      

    
##### OSM specific endpoints ####
@app.route('/adapters/<service_platform>/get_token', methods=['GET'])
def adapter_osm_get_token(service_platform):
    ad = adapter.Adapter(service_platform)
    return ad.getOSMToken()



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
