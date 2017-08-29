import os
from flask import render_template
from app import app
import simplejson as json

TRIPDIR = "trips/"

@app.route('/')
def index():
    return render_template("index.html", title = "RoadTrip Home", trips = parseTrips())

def parseTrips():
    files = [f for f in os.listdir(TRIPDIR)]
    #trips = [{"name":  str(f), "status" : "ok"} for f in files]
    trips = [parseTripFile(f) for f in files]
    return trips

def parseTripFile(pTripFile):
    with open("".join([TRIPDIR, pTripFile])) as tripfile:
        try:
            t = json.load(tripfile)
            t["status"] = "OK"
            t["filename"] = pTripFile
            return t
        except:
            return json.loads("{\"name\" : \" %s \", \"status\" :  \"Error while parsing \"}" % pTripFile)
