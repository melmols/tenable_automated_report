#References: pytenable.readthedocs.io
#License: Mit
#Author: Melmols 

## 16/10/2019
## Description: 
## Get a list of scans, get the asset's list of that particular scan and the details within that asset list.

#---------------------------------------------------------#    

#Libs 
from tenable.io import TenableIO
import requests


class my_tenable:


    @classmethod
    def my_tenable(self):
        '''Authenticatation for pyTenable api''' 
        self.TIO_ACCESS_KEY = ''
        self.TIO_SECRET_KEY = ''

        self.tio = TenableIO(TIO_ACCESS_KEY, TIO_SECRET_KEY)
        print ('authenticating')
        

    #---------------------------------------------------------#    
    @classmethod
    def get_scan_list(self):
        ''' Get The list of scans that have been run on Tenable.io'''

        print ('running: get_scan_list')
        scan_list = []
        for scan in self.tio.scans.list():
           scan_list += ['{status}: {id} - {name}'.format(**scan)]

        return scan_list

    #---------------------------------------------------------# 
    
    @classmethod
    def list_assets(self,scan_id):
        '''Rewriting assets.list() so it lists for a particular scan after passing
            the scan's ID '''

        url = "https://cloud.tenable.com/app.html#/scans/reports/" + scan_id + "/assets"

        headers = {

                   'accept': 'application/json',
                   'x-ApiKeys': ('accessKey=%s; secretKey=%s'%self.TIO_ACCESS_KEY,self.TIO_SECRET_KEY)

                  }

        response = requests.request("GET", url, headers=headers)

        return response.text


    def get_asset_details(asset_list):

        return asset_list

    #---------------------------------------------------------#    

