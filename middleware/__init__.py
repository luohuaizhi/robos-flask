from flask import make_response
from application import app


@app.after_request
def aft_resp(response):
    resp = make_response(response)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTION'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp
