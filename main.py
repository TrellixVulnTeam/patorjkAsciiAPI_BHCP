import json
import random
import calendar

from flask import Flask

import modules.webscrapGet as wG


app = Flask(__name__)


@app.route("/get-ascii/<style>/<character_width>/<character_height>/<text>", methods=['GET'])
def getCalendar(style : str, character_width : str, character_height : str, text : str):
    return wG.generateAscii(style=style, characterWidth=character_width, characterHeight=character_height, text=text)


app.run(debug=True)
