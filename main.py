import requests as re
import json

def get_latest_version():
    version_list = re.get("https://updater.factorio.com/get-available-versions")
    versions = json.loads(version_list.content)
    print(f"Found latest 'core-linux_headless64' stable version: {versions['core-linux_headless64'][-1]['stable']}")
    return versions['core-linux_headless64'][-1]['stable']

def get_download_url(from_version:str,to_version:str):
    initial_url = f"https://updater.factorio.com/updater/get-download?package=core-linux_headless64&from={from_version}&to={to_version}"
    try:
        response_url = re.head(initial_url)        
        return response_url.headers["Location"]
    except:
        print(f"Possible version error, please retry.\n")

def get_version():
    version = input(f"Please give your current version number in the format listed in https://updater.factorio.com/get-available-versions\n\t> ")
    try:
        test_1 = version.split(".",maxsplit=1)
        if (test_1[0].isnumeric() is not True): raise Exception
        test_2 = test_1[1].split(".",maxsplit=1)
        if (test_2[0].isnumeric() is not True): raise Exception
        if (test_2[1].isnumeric() is not True): raise Exception
        return version
    except:
        print(f"Invalid version format.\n")
        get_version()

def download_update(from_version, to_version):
    download_url = get_download_url(from_version, to_version)
    file = re.get(download_url)
    with open(f"update-{from_version}-{to_version}.zip",'wb') as f:
        f.write(file.content)

latest_version = get_latest_version()
from_version = get_version()
to_version = f'{from_version.split(".")[0]}.{from_version.split(".")[1]}.{int(from_version.split(".")[2])+1}'
if (from_version == latest_version):
    print(f"Already updated to latest stable release.")
else:
    print(f"Now downloading update for 'core-linux_headless64' version from {from_version} to {to_version}")
    while(True):
        try:
            download_update(from_version, to_version)
            from_version = to_version
            to_version = f'{from_version.split(".")[0]}.{from_version.split(".")[1]}.{int(from_version.split(".")[2])+1}'
            if (from_version == latest_version):
                print(f"Finished downloading all updates.")
                break
            else:
                print(f"Now downloading update for 'core-linux_headless64' version from {to_version} to {to_version.split('.')[0]}.{to_version.split('.')[1]}.{int(to_version.split('.')[2])+1}")
        except:
            print(f"Unknown error. Please retry.")
            break