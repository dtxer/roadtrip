import os
from flask import render_template, Response, request
from app import app
import subprocess

TRIPDIR = "trips/"
SCRIPTDIR = "scripts/"

@app.route('/runner')
def runner():
    def inner(pScript):
        proc = subprocess.Popen(
            ["".join([SCRIPTDIR, pScript])],
            shell=True,
            stdout=subprocess.PIPE,
	    universal_newlines=True 
        )

        for line in iter(proc.stdout.readline,''):
            yield line.rstrip() + '<br/>\n'

    res = "".join(["".join([a, "\t", request.args.get(a), "<BR>\n"]) for a in request.args if a != "script"])
    return res
#    return Response(inner("demo.sh"), mimetype='text/html')


