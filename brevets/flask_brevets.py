"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
from pymongo import MongoClient
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config
import logging
import os

###
# Globals
###
app = flask.Flask(__name__)

CONFIG = config.configuration()

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.brevets

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    # start of edited code
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    start_time = request.args.get('date', type=str)
    brevet_length = request.args.get('length', type=float)
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))

    open_time = acp_times.open_time(km, brevet_length, 
                arrow.get(start_time)).format('YYYY-MM-DDTHH:mm')
    close_time = acp_times.close_time(km, brevet_length, 
                arrow.get(start_time)).format('YYYY-MM-DDTHH:mm')
    
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)


###############
#
# Project 5
#   MongoDB interactions
#
###############
@app.route("/_submit", methods=["POST"])
def _insert():
    data = request.get_json()
    app.logger.debug(f"In MONGODB {data}")

    # update the one race named mybrevet - upsert = create if not found
    db.races.update_one({'name' : 'mybrevet'}, {'$set' : data}, upsert=True)

    return flask.jsonify({'success' : True})

@app.route("/_display")
def _display():
    
    query = db.races.find_one()
    app.logger.debug(f"Out MONGO DB {query}")

    if query is None:
        return flask.jsonify(result={})

    query.pop("_id") # mongodb id object is not serializable (important for jsonify)
    return flask.jsonify(result=query)

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
