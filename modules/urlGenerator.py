def createUrl(textStyle : str, characterWidth : str, characterHeight : str, text : str):
    """Function that will create URL from style and text

    Args:
        textStyle (str): the text style you want
        text (str): the text you want to convert to ASCII art

    Returns:
        str: the URL where will be scraped the ASCII art
    """
    
    widthOptions = {
        "full" : '0',
        "fitted" : '1',
        "smush (r)" : '2',
        "smush (u)" : '3',
        "default" : ''
    }
    
    heightOptions = {
        "full" : '0',
        "fitted" : '1',
        "smush (r)" : '2',
        "smush (u)" : '3',
        "default" : ''
    }
    
    
    widthOption = widthOptions[characterWidth.lower()]
    heightOption = heightOptions[characterHeight.lower()]
    
    return f"https://patorjk.com/software/taag/#p=display&h={widthOption}&v={heightOption}&f={textStyle}&t={text}"


if __name__ == "__main__":
    import webbrowser

    style = input("Enter text style : ")
    content = input("Enter text : ")
    
    testUrl = createUrl(textStyle=style, text=content)
    
    print(testUrl)
    webbrowser.open(testUrl)
