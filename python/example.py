from pytenable import my_tenable


if __name__ == "__main__":
    
    #variables

    access_key = '3d53008b63d89b20eec0b03bb1b2b10683c1f2b94ffb08d9a07af0d4a448f2d0'
    secret_key = 'fdd62df2bd06a38fb7421954675cc6b99a60029d95882af91731764a22a2d221'

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
