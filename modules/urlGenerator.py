def create_url(text_style : str, character_width : str, character_height : str, text : str):
    """Function that will create URL from style and text

    Args:
        text_style (str): the text style you want
        character_width (str): the character width
        character_height (str): the character height
        text (str): the text you want to convert to ASCII art

    Returns:
        str: the website's URL of which will be scraped the ASCII art
    """
    
    # Defining the options to simplify URL creation
    width_options = {
        "full" : '0',
        "fitted" : '1',
        "smush (r)" : '2',
        "smush (u)" : '3',
        "default" : ''
    }
    
    height_options = {
        "full" : '0',
        "fitted" : '1',
        "smush (r)" : '2',
        "smush (u)" : '3',
        "default" : ''
    }


    # Converting function parameters into URL parameters
    width_option = width_options[character_width.lower()]
    height_option = height_options[character_height.lower()]

    return f"https://patorjk.com/software/taag/#p=display&h={width_option}&v={height_option}&f={text_style}&t={text}"


if __name__ == "__main__":
    import webbrowser

    style = input("Enter text style : ")
    content = input("Enter text : ")
    
    testUrl = create_url(text_style=style, character_width='Default', character_height='Default',text=content)
    
    print(testUrl)
    webbrowser.open(testUrl)
