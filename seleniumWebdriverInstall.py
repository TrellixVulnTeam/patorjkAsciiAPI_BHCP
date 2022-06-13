import os
import sys
import time
import shutil
import distro
import tarfile
import requests

import termcolor
import selenium
from selenium import webdriver


CURRENT_VERSION = 'v0.31.0'
LINK = f"https://github.com/mozilla/geckodriver/releases/download/{CURRENT_VERSION}"



print("""
██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗        ██████╗ ██╗   ██╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║        ██╔══██╗╚██╗ ██╔╝
██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║        ██████╔╝ ╚████╔╝ 
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║        ██╔═══╝   ╚██╔╝  
██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗██╗██║        ██║   
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚═╝        ╚═╝   
""")




def download_file(link : str, output : str):
    response = requests.get(link, allow_redirects=True)
    
    with open(output, 'wb') as f:
        f.write(response.content)


def is_gecko_installed():
    try:
        driver_options = webdriver.FirefoxOptions()
        driver_options.headless = True
        
        driver = webdriver.Firefox(options=driver_options)
        return True
    except selenium.common.exceptions.WebDriverException:
        return False


def untar_file(file : str):
    with tarfile.open(file, 'r') as tarFile:
        tarFile.extractall('/usr/local/bin')
    


if is_gecko_installed():
    print("[+] Geckodriver is already installed on your system, exiting...\n")
    os.remove('geckodriver.log')
    sys.exit()


os_name = distro.name()


installer_link = {
    "Debian" : (f'{LINK}/geckodriver-{CURRENT_VERSION}-linux64.tar.gz', f'geckodriver-{CURRENT_VERSION}-linux64.tar.gz'),
    "Kali linux" : (f'{LINK}/geckodriver-{CURRENT_VERSION}-linux64.tar.gz', f'geckodriver-{CURRENT_VERSION}-linux64.tar.gz'),
    "Parrot OS" : (f'{LINK}/geckodriver-{CURRENT_VERSION}-linux64.tar.gz', f'geckodriver-{CURRENT_VERSION}-linux64.tar.gz'),
    "Ubuntu" : (f'{LINK}/geckodriver-{CURRENT_VERSION}-linux64.tar.gz', f'geckodriver-{CURRENT_VERSION}-linux64.tar.gz'),
    "Arch" : (f'{LINK}/geckodriver-{CURRENT_VERSION}-linux64.tar.gz', f'geckodriver-{CURRENT_VERSION}-linux64.tar.gz'),
    "Manjaro" : (f'{LINK}/geckodriver-{CURRENT_VERSION}-linux64.tar.gz', f'geckodriver-{CURRENT_VERSION}-linux64.tar.gz'),
    "Endeavour" : (f'{LINK}/geckodriver-{CURRENT_VERSION}-linux64.tar.gz', f'geckodriver-{CURRENT_VERSION}-linux64.tar.gz'),
    "Garuda" :(f'{LINK}/geckodriver-{CURRENT_VERSION}-linux64.tar.gz', f'geckodriver-{CURRENT_VERSION}-linux64.tar.gz'),

    "Mac OS" : ('{LINK}/geckodriver-{CURRENT_VERSION}-macos.tar.gz', f'geckodriver-{CURRENT_VERSION}-macos.tar.gz'),
}


for distro in installer_link.keys():
    link, filename = installer_link[distro]
    
    if distro.lower() in os_name.lower():        
        os.mkdir('Geckodriver')
        
        download_file(link, f"./Geckodriver/{filename}")
        untar_file(f'./Geckodriver/{filename}')
        break
else:
    time.sleep(2)
    error_text = termcolor.colored("[/!\\] Your OS has not been recognized, please see manually_install_geckodriver.txt\n", 'red')
    print(error_text)
    sys.exit()


try:
    shutil.rmtree('./Geckodriver')
    os.remove('geckodriver.log')
except FileNotFoundError:
    pass


print("\n[+] Geckodriver has successfully been installed on your system\n")
