import json

from flask import Flask

import modules.webscrapGet as wG


app = Flask(__name__)


@app.route("/get-ascii/<style>/<character_width>/<character_height>/<text>", methods=['GET'])
def getAscii(style : str, character_width : str, character_height : str, text : str) -> str() :
    """Function that permite to get ASCII from website

    Args:
        textStyle (str): the text style you want
        characterWidth (str): the character width
        characterHeight (str): the character height
        text (str): the text you want to convert to ASCII art

    Returns:
        str: ASCII art got from the website
    """
    
    return wG.generateAscii(style=style, characterWidth=character_width, characterHeight=character_height, text=text)


app.run(debug=True)
