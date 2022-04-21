def createUrl(textStyle : str, characterWidth : str, characterHeight, text : str):
    """Function that will create URL from style and text

    Args:
        textStyle (str): the text style you want
        text (str): the text you want to convert to ASCII art

    Returns:
        str: the URL where will be scraped the ASCII art
    """
    
    widthOptions = {
        "Full" : 0,
        "Fitted" : 1,
        "Smush (R)" : 2,
        "Smush (U)" : 3,
        "Default" : None
    }
    
    heightOptions = {
        "Full" : 0,
        "Fitted" : 1,
        "Smush (R)" : 2,
        "Smush (U)" : 3,
        "Default" : None
    }
    
    
    widthOption = widthOptions[characterWidth]
    heightOption = heightOptions[characterHeight]
    
    return f"https://patorjk.com/software/taag/#p=display&h={widthOption}&v={heightOption}&f={textStyle}&t={text}"


if __name__ == "__main__":
    import webbrowser

    style = input("Enter text style : ")
    content = input("Enter text : ")
    
    testUrl = createUrl(textStyle=style, text=content)
    
    print(testUrl)
    webbrowser.open(testUrl)
