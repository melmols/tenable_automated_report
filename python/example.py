from pytenable import my_tenable


if __name__ == "__main__":
    
    #variables

    access_key = ''
    secret_key = ''

    tio = my_tenable.authenticate_tenable(access_key,secret_key)

    #get the list of ids
    list_of_ids = []
    list_of_ids = my_tenable.list_assets_with_vulns()
    asset_info = {}

    #iterate through asset_ids and get their asset info
    for asset_id in list_of_ids:
        asset_info.update(my_tenable.get_asset_details(asset_id))

        print(asset_info)
        break
