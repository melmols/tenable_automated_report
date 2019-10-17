#example usage of my_tenable.py


from my_tenable import my_tenable


if __name__ == '__main__':
    
    #variables
    all_scans = {}
    list_of_assets = []
    
    
    #---------------------------------------------------------#    
    
    #variable definition
    
    all_scans = get_scan_list()
    list_of_assets = get_assets(all_scans, 'The_Scan_We_Want')
