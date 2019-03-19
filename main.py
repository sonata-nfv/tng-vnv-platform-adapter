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
@app.route('/service_platforms', methods=['GET','POST','OPTIONS','DELETE','PATCH'])
def sps():
    if request.method == 'GET':
        sp = serviceplatform.ServicePlatform("name","host","type","username","password","project_name","service_token","monitoring_urls")
        return sp.getServicePlatforms()

    if request.method == 'POST':
        print (request.is_json)
        content = request.get_json()
        print (content)  
        try:      
            mon_urls = content['monitoring_urls']
            print ("mon_url exists")
            try:
                pr = content['project_name']
                print ("project name exists")
                sp = serviceplatform.ServicePlatform(content['name'],content['host'],content['type'],content['username'],content['password'],content['project_name'],"service_token",content['monitoring_urls'])
                return sp.registerServicePlatform()
            except:
                sp = serviceplatform.ServicePlatform(content['name'],content['host'],content['type'],content['username'],content['password'],"project_name","service_token",content['monitoring_urls'])
                return sp.registerServicePlatform()
        except:
            print ("mon_url does not exists")
            try:
                pr = content['project_name']
                print ("project name exists")
                sp = serviceplatform.ServicePlatform(content['name'],content['host'],content['type'],content['username'],content['password'],content['project_name'],"service_token","monitoring_urls")
                return sp.registerServicePlatform() 
            except:
                print ("project name does not exists")
                sp = serviceplatform.ServicePlatform(content['name'],content['host'],content['type'],content['username'],content['password'],"project_name","service_token","monitoring_urls")
                return sp.registerServicePlatform()         

    if request.method == 'OPTIONS':
        return "Options", 200
    
    if request.method == 'DELETE':        
        return "delete", 200

    if request.method == 'PATCH':    
        print (request.is_json)
        content = request.get_json()
        print (content)  
        try:      
            mon_urls = content['monitoring_urls']
            print ("mon_url exists")
            try:
                pr = content['project_name']
                print ("project name exists")
                sp = serviceplatform.ServicePlatform(content['name'],content['host'],content['type'],content['username'],content['password'],content['project_name'],"service_token",content['monitoring_urls'])
                return sp.patchServicePlatform()
            except:
                sp = serviceplatform.ServicePlatform(content['name'],content['host'],content['type'],content['username'],content['password'],"project_name","service_token",content['monitoring_urls'])
                return sp.patchServicePlatform()
        except:
            print ("mon_url does not exists")
            try:
                pr = content['project_name']
                print ("project name exists")
                sp = serviceplatform.ServicePlatform(content['name'],content['host'],content['type'],content['username'],content['password'],content['project_name'],"service_token","monitoring_urls")
                return sp.patchServicePlatform() 
            except:
                print ("project name does not exists")
                sp = serviceplatform.ServicePlatform(content['name'],content['host'],content['type'],content['username'],content['password'],"project_name","service_token","monitoring_urls")
                return sp.patchServicePlatform() 



@app.route('/service_platforms/<service_platform>', methods=['GET','DELETE','PATCH'])
def sp(service_platform):
    if request.method == 'GET':
        sp = serviceplatform.ServicePlatform(service_platform,"host","type","username","password","project_name","service_token","monitoring_urls")
        return sp.getServicePlatform() 
    if request.method == 'DELETE':          
        sp = serviceplatform.ServicePlatform(service_platform,"host","type","username","password","project_name","service_token","monitoring_urls")
        return sp.deleteServicePlatform()
    if request.method == 'PATCH':    
        print (request.is_json)
        content = request.get_json()
        print (content)  
        try:      
            mon_urls = content['monitoring_urls']
            print ("mon_url exists")
            try:
                pr = content['project_name']
                print ("project name exists")
                sp = serviceplatform.ServicePlatform(service_platform,content['host'],content['type'],content['username'],content['password'],content['project_name'],"service_token",content['monitoring_urls'])
                return sp.patchServicePlatform()
            except:
                sp = serviceplatform.ServicePlatform(service_platform,content['host'],content['type'],content['username'],content['password'],"project_name","service_token",content['monitoring_urls'])
                return sp.patchServicePlatform()
        except:
            print ("mon_url does not exists")
            try:
                pr = content['project_name']
                print ("project name exists")
                sp = serviceplatform.ServicePlatform(service_platform,content['host'],content['type'],content['username'],content['password'],content['project_name'],"service_token","monitoring_urls")
                return sp.patchServicePlatform() 
            except:
                print ("project name does not exists")
                sp = serviceplatform.ServicePlatform(service_platform,content['host'],content['type'],content['username'],content['password'],"project_name","service_token","monitoring_urls")
                return sp.patchServicePlatform()           





##### ADAPTER GENERIC ROUTES #####

@app.route('/adapters/<service_platform>/get_username')
def adapter_get_username(service_platform):
    ad = adapter.Adapter(service_platform)
    return ad.getDBUserName()
 
@app.route('/adapters/<service_platform>/get_password')
def adapter_get_password(service_platform):
    ad = adapter.Adapter(service_platform)
    return ad.getDBPassword() 

@app.route('/adapters/<service_platform>/get_type')
def adapter_get_type(service_platform):
    ad = adapter.Adapter(service_platform)
    return ad.getDBType()

@app.route('/adapters/<service_platform>/get_project_name')
def adapter_get_project_name(service_platform):
    ad = adapter.Adapter(service_platform)
    return ad.getDBProjectName()    

@app.route('/adapters/<service_platform>/get_host')
def adapter_get_host(service_platform):
    ad = adapter.Adapter(service_platform)
    return ad.getDBHost()
  

@app.route('/adapters/<service_platform>/services', methods=['GET'])
def adapter_get_services(service_platform):
    ad = adapter.Adapter(service_platform)
    return ad.getServices()
    #return ad.getDBType()
   

@app.route('/adapters/<service_platform>/functions', methods=['GET'])
def adapter_get_Functions(service_platform):
    ad = adapter.Adapter(service_platform)
    return ad.getFunctions()  


@app.route('/adapters/packages/unzip-package', methods=['POST'])
def adapter_unzip_package():
    content = request.get_json()
    print (content)
    ad = adapter.Adapter("service_platform")   
    return ad.unzipPackage(content['package']) 



@app.route('/adapters/<service_platform>/services/<name>/<vendor>/<version>', methods=['GET'])
def adapter_get_service(service_platform,name,vendor, version):
    ad = adapter.Adapter(service_platform)
    return ad.getService(name,vendor,version)   

@app.route('/adapters/<service_platform>/services/<name>/<vendor>/<version>/id', methods=['GET'])
def adapter_get_service_id(service_platform,name,vendor, version):
    ad = adapter.Adapter(service_platform)
    return ad.getServiceId(name,vendor,version)      

@app.route('/adapters/<service_platform>/services/<name>/<vendor>/<version>/instantiations', methods=['GET'])
def adapter_get_service_instantiations(service_platform,name,vendor, version):
    ad = adapter.Adapter(service_platform)
    return ad.getServiceInstantiations(name,vendor,version)       


@app.route('/adapters/<service_platform>/packages/<name>/<vendor>/<version>/id', methods=['GET'])
def adapter_get_package_id(service_platform,name,vendor, version):
    ad = adapter.Adapter(service_platform)
    return ad.getPackageId(name,vendor,version) 

@app.route('/adapters/<service_platform>/packages/<pkg_id>/package-file', methods=['GET'])
def adapter_get_package_file(service_platform, pkg_id):
    ad = adapter.Adapter(service_platform)
    return ad.getPackageFile(pkg_id)   




@app.route('/adapters/<service_platform>/packages', methods=['GET'])
def adapter_get_packages(service_platform):
    ad = adapter.Adapter(service_platform)
    return ad.getPackages()

@app.route('/adapters/packages', methods=['GET'])
def adapter_get_vnv_packages():
    ad = adapter.Adapter("service_platform")
    return ad.getVnVPackages()   

@app.route('/adapters/packages/<name>/<vendor>/<version>/id', methods=['GET'])
def adapter_get_vnv_package_by_id(name,vendor, version):
    ad = adapter.Adapter("service_platform")
    return ad.getVnVPackagebyId(name,vendor,version)  

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


@app.route('/adapters/packages/<package_id>/download', methods=['GET'])
def adapter_download_package(package_id):
    ad = adapter.Adapter("service_platform")   
    return ad.downloadPackageTGO(package_id) 
	

    

#### SERVICES OPERATIONS #### 
@app.route('/adapters/<service_platform>/instantiations', methods=['GET'])
def serviceInstantiationsGetStatus(service_platform):
    ad = adapter.Adapter(service_platform)
    return ad.instantiationsStatus() 
 
   
@app.route('/adapters/<service_platform>/instantiations/<id>', methods=['GET'])
def serviceInstantiationGetStatus(service_platform,id):
    ad = adapter.Adapter(service_platform)
    return ad.instantiationStatus(id)

@app.route('/adapters/<service_platform>/instantiations/<id>/monitoring', methods=['GET'])
def serviceInstantiationInfoMonitoring(service_platform,id):
    ad = adapter.Adapter(service_platform)
    return ad.instantiationInfoMonitoring(id)    

@app.route('/adapters/<service_platform>/instantiations/<id>/ips', methods=['GET'])
def OSMInstantiationGetIPs(service_platform,id):
    ad = adapter.Adapter(service_platform)
    return ad.osmInstantiationIPs(id)


@app.route('/adapters/<service_platform>/instantiations', methods=['POST'])
def serviceInstantiation(service_platform):
    print (request.is_json)
    content = request.get_json()
    print (content)    
    ad = adapter.Adapter(service_platform)
    #print (content['service_uuid'])         
    return ad.instantiation(request)    
    

@app.route('/adapters/<service_platform>/instantiations/<service_id>', methods=['GET'])
def serviceInstantiationStatus(service_platform,service_id):
    print (request.is_json)
    content = request.get_json()
    print (content)    
    ad = adapter.Adapter(service_platform)
    #print (content['service_uuid'])        
    return ad.instantiationStatus(service_id)      




@app.route('/adapters/<service_platform>/instantiations/delete', methods=['POST'])
def serviceInstantiationDelete(service_platform):
    print (request.is_json)
    content = request.get_json()
    print (content)    
    ad = adapter.Adapter(service_platform)
    #print (content['service_uuid'])        
    return ad.instantiationDelete(request)      

@app.route('/adapters/<service_platform>/vims', methods=['GET'])
def getVims(service_platform):
    ad = adapter.Adapter(service_platform)      
    return ad.getVims()  

@app.route('/adapters/<service_platform>/vims/<vim_name>', methods=['GET'])
def getVimInfo(service_platform,vim_name):
    ad = adapter.Adapter(service_platform)      
    return ad.getVim(vim_name)    

@app.route('/adapters/<service_platform>/vims', methods=['GET'])
def getWims(service_platform):
    ad = adapter.Adapter(service_platform)      
    return ad.getWims()  

@app.route('/adapters/<service_platform>/vims/<wim_name>', methods=['GET'])
def getWimInfo(service_platform,wim_name):
    ad = adapter.Adapter(service_platform)      
    return ad.getWim(wim_name)      

    
##### OSM specific endpoints ####
@app.route('/adapters/<service_platform>/get_token', methods=['POST'])
def adapter_osm_get_token(service_platform):
    print (request.is_json)
    content = request.get_json()
    print (content) 
    ad = adapter.Adapter(service_platform)   
    my_type = ad.getDBType()
    if my_type == 'sonata':
        print("illllooo")
        print ("this SP is a sonata")
        print("illllooo")
        return ad.getSonataToken(request)    
    if my_type == 'osm':
        return ad.getOSMToken(request)   
       


@app.route('/adapters/<service_platform>/services', methods=['POST'])
def adapter_upload_service(service_platform):
    print (request.is_json)
    content = request.get_json()
    print (content)
    ad = adapter.Adapter(service_platform)  
    print (ad.name)         
    return ad.uploadOSMService(request)       


@app.route('/adapters/<service_platform>/functions', methods=['POST'])
def adapter_upload_function(service_platform):
    print (request.is_json)
    content = request.get_json()
    print (content)
    ad = adapter.Adapter(service_platform)  
    print (ad.name)         
    return ad.uploadOSMFunction(request)  

@app.route('/adapters/<service_platform>/functions/<id_to_delete>/delete', methods=['DELETE'])
def adapter_delete_function(service_platform,id_to_delete):
    ad = adapter.Adapter(service_platform)  
    return ad.deleteOSMFunction(id_to_delete)    

@app.route('/adapters/<service_platform>/services/<id_to_delete>/delete', methods=['DELETE'])
def adapter_delete_service(service_platform,id_to_delete):
    ad = adapter.Adapter(service_platform)  
    return ad.deleteOSMService(id_to_delete)  

@app.route('/callback_tests', methods=['POST'])
def adapter_callback_tests():      
    print (request.is_json)
    content = request.get_json()
    print (content)
    return content.__str__()

@app.route('/adapters/<service_platform>/monitoring', methods=['GET'])
def monitoring_tests(service_platform):        
    ad = adapter.Adapter(service_platform)  
    return ad.monitoringTests("cpu_utilization")  

@app.route('/adapters/<service_platform>/monitoring', methods=['POST'])
def monitoring(service_platform):  
    print (request.is_json)
    content = request.get_json()
    print (content)      
    ad = adapter.Adapter(service_platform)  
    return ad.monitoringTests(content['metric'])
    






from flask_cors import CORS
#app = Flask(__name__)
CORS(app)


@app.after_request
def after_request(response):
  #response.headers.add('Access-Control-Allow-Origin', '*')
  #response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,PATCH')
  return response



#MAIN FUNCTION OF THE SERVER

if __name__ == '__main__':
    #READ CONFIG
    conf_parser = argparse.ArgumentParser( description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter, add_help=True )
    conf_parser.add_argument("-c", "--conf_file", help="Specify config file", metavar="FILE", default='config.cfg')
    args, remaining_argv = conf_parser.parse_known_args()
    config = ConfigParser()
    config.read(args.conf_file)
    createUsersObj = utils.Utils()
    createUsersObj.createTableUsers("db-config.cfg")
    createUsersObj.createTableServicePlatforms("db-config.cfg")

    
    #RUN SERVER
    #app.run(debug=True, host='0.0.0.0', port=os.environ.get("SLICE_MGR_PORT"))
    app.run(debug=True,host='0.0.0.0',port=5001)

