#Source: pytenable.readthedocs.io
#License: Mit
#Author: Melmols 

## 16/10/2019
## Description: 
## Get a list of scans, get the asset's list of that particular scan and the details within that asset list.


#Libs and Packs
from tenable.io import TenableIO
import requests

#---------------------------------------------------------#    
#Global Libraries



def my_tenable():
    '''Authenticatation for pyTenable api''' 
    TIO_ACCESS_KEY = '7100f224be6f9d6cd4f16335ef21c878d8c1aea376c2991c39fd7ecb45c01230'
    TIO_SECRET_KEY = 'ff4ff70972b6cff53fb73b548001f4af8c835c780fb2540688a09055c841f3dd'
    
    tio = TenableIO(TIO_ACCESS_KEY, TIO_SECRET_KEY)
    print ('authentication complete')
    return tio

#---------------------------------------------------------#    
    
def get_scan_list():
    ''' Get The list of scans that have been run on Tenable.io'''
    
    print ('running: get_scan_list')
    scan_list = []
    for scan in my_tenable().scans.list():
       scan_list += ['{status}: {id} - {name}'.format(**scan)]
        
    return scan_list

#---------------------------------------------------------# 

def list_assets(scan_id):
    '''Rewriting assets.list() so it lists for a particular scan after passing
        the scan's ID '''
    
    url = "https://cloud.tenable.com/app.html#/scans/reports/" + scan_id + "/assets"

    headers = {
        
               'accept': 'application/json',
               'x-ApiKeys': accessKey=TIO_ACCESS_KEY;secretKey=TIO_SECRET_KEY   
                
              }

    response = requests.request("GET", url, headers=headers)

    return response.text


def get_asset_details(asset_list):
    
    return asset_list

#---------------------------------------------------------#    



if __name__ == '__main__':
    
    #variables
    all_scans = [] 
    list_of_assets = []
    
    
    #---------------------------------------------------------#    
    
    #variable definition
    
    all_scans = get_scan_list()
    list_of_assets = list_assets('1063')
    
    print (all_scans)
    print (list_of_assets)
