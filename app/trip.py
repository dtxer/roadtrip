import os
from flask import render_template
from app import app
import simplejson as json

TRIPDIR = "trips/"

@app.route('/trip/<tripname>')
def trip(tripname):
    trip = parseTrip(tripname)
    return render_template("trip.html", title = trip["name"], trip = trip)

def parseTrip(pTripFile):
    with open("".join([TRIPDIR, pTripFile])) as tripfile:
         return json.load(tripfile)


