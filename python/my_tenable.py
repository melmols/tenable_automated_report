# References: pytenable.readthedocs.io

# License: Mit

# Author: Melmols 

## 16/10/2019

## Description: (script under construction)

## Get a list of scans, get the asset's list of that particular scan and the details within that asset list.

#---------------------------------------------------------# 

#Libs 

from tenable.io import TenableIO
import requests
import json

class my_tenable:
    #(*)this works if there are no network restrictions, otherwise do the same in get_all_vulns
    
    @classmethod
    def authenticate_tenable(self,access_key,secret_key):

        '''Authenticatation for pyTenable api''' 
        TIO_ACCESS_KEY = access_key     
        TIO_SECRET_KEY = secret_key

        #set the header
        self.headers = {
            'accept': 'application/json',
            'x-ApiKeys': 'accessKey=%s; secretKey=%s'%(TIO_ACCESS_KEY,TIO_SECRET_KEY)
        }
        
        #tell it to go through a proxy
#         self.proxies = {
#             "http": "http://gateway.zscloud.net:80",
#             "https": "https://gateway.zscloud.net:80",

#         }

        self.session = requests.Session()

        print ('authenticating')

    #---------------------------------------------------------# 

    @classmethod
    def get_scan_list(self):
        ''' Get The list of scans that have been run on Tenable.io'''
        
        print ('running: get_scan_list')

        #(*)
        scan_list = []

        for scan in self.tio.scans.list():
            scan_list += ['{status}: {id} - {uuid} - {name}'.format(**scan)]

        return scan_list

    #---------------------------------------------------------# 

    @classmethod
    def get_all_vulns(self):
        '''Rewriting vulns.list() so it lists for all vulnerabilities'''

        #url for the api
        url = ("https://cloud.tenable.com/workbenches/vulnerabilities")

        #start a session with requests and then set the trust_env to false for no cert checks
        

        #make the call and set verify to false so it doesn't check for certs (not the best but oh well...)
        response = self.session.get(url, proxies=self.proxies, headers=self.headers, verify=False)

        #make it a json formatted response
        self.vulns_response = json.loads(response.text)

        # return response.text
        return print('getting all vulnerabilities...')
    #---------------------------------------------------------# 
   
    @classmethod
    def list_assets_with_vulns (self):
        '''retrieves a list of all assets with vulnerabilities*, and creates an id list'''
        
        url = "https://cloud.tenable.com/workbenches/assets/vulnerabilities"
        
        response =  self.session.get(url, proxies=self.proxies, headers=self.headers, verify=False)

        json_response = json.loads(response.text)

        asset_dict = {}
        asset_id_list = []
        
        for k, v in json_response.items():
            if k == 'assets': 
                for elements in v:
                    asset_dict.update(elements)
                    #create a list with the ids of the assets
                    asset_id_list.append(asset_dict['id'])
        return asset_id_list
    
    @classmethod
    def get_asset_details (self,asset_id):
        '''retrieves individual asset details based on their id'''

        
        url = ("https://cloud.tenable.com/workbenches/assets/"+asset_id+"/vulnerabilities")

        response =  self.session.get(url, proxies=self.proxies, headers=self.headers, verify=False)

        json_response = json.loads(response.text)

        return json_response
            

                

        

