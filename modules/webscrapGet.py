import requests

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

import modules.urlGenerator as urlGenerator


def get_ascii(url : str) -> str :
    """Function to get ASCII art from a link

    Args:
        url (str): the link where the function will take
                        the ASCII art

    Returns:
        str: the ASCII art the program got from the website
    """

    # Setting headless mode
    driver_options = webdriver.FirefoxOptions()
    driver_options.headless = True
    
    driver = webdriver.Firefox(options=driver_options)
    driver.get(url)
    
    # Getting the ASCII art
    ascii_art = driver.find_element(By.ID, "taag_output_text")

    # If no ASCII art has been got, the program will return an empty string
    if not ascii_art:
        return ""
        
    # Returns ASCII art without HTML balises
    return ascii_art.text


def get_font_list() -> str :
    """Function that returns all ASCII styles availible

    Returns:
        str: The ASCII styles list
    """

    with open('./modules/textPolices.txt', 'r') as f:
        fontList = f.read()
    
    return fontList


def style_exists(style : str) -> bool :
    fontList = get_font_list().split('\n')

    return style in fontList


def generate_ascii(style : str, character_width : str = 'Default', character_height : str = 'Default', text : str = 'Joe Mama') -> str :
    """Function that use previouses to generate ASCII art

    Args:
        textStyle (str): the text style you want
        characterWidth (str): the character width
        characterHeight (str): the character height
        text (str): the text you want to convert to ASCII art
    
    Returns:
        asciiArt (str): The ASCII art generated
    """

    # Creating the URL and webscrap the ASCII art generated
    link = urlGenerator.create_url(text_style=style, character_width=character_width, character_height=character_height, text=text)
    ascii_art = get_ascii(link)

    return ascii_art


if __name__ == "__main__":
    asciiArt = generate_ascii('Big', 'default', 'default', 'Jemla')
    print(asciiArt)
