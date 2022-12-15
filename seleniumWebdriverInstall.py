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




def download_file(link : str, output : str) -> None :
    """Downloads a file from a link and saves it to a given output path.

    Args:
        link (str): the link to the file to download
        output (str): the path to save the file to
    """
    
    response = requests.get(link, allow_redirects=True)
    
    with open(output, 'wb') as f:
        f.write(response.content)


def is_gecko_installed() -> bool :
    """Returns True if geckodriver is installed, False otherwise.

    Returns:
        bool: True if geckodriver is installed, False otherwise.
    """
    
    try:
        driver_options = webdriver.FirefoxOptions()
        driver_options.headless = True
        
        driver = webdriver.Firefox(options=driver_options)
        return True
    except selenium.common.exceptions.WebDriverException:
        return False


def untar_file(file : str) -> None:
    """Untars a file.

    Args:
        file (str): the path to the file to untar
    """
    
    with tarfile.open(file, 'r') as tarFile:
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tarFile, "/usr/local/bin")
    


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
