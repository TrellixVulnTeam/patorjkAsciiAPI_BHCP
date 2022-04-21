import json
import random
import calendar

from flask import Flask

import modules.webscrapGet as wG


app = Flask(__name__)


@app.route("/get-calendar/<year>/<month>", methods=['GET'])
def getCalendar(year, month):
    strCalendar = calendar.month(int(year), int(month))
    
    return json.dumps({'calendar' : strCalendar})




app.run(debug=True)
