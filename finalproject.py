from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Building, BuildingInfo, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

engine = create_engine('sqlite:///buildinginfo1.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/buildingcatalog/')
def showContinents():
    continents = session.query(BuildingInfo).group_by(BuildingInfo.continent)
    return render_template('continents.html', continents=continents)

@app.route('/buildingcatalog/<string:continent>')
def showCountry(continent):
    buildings = session.query(BuildingInfo).filter(BuildingInfo.continent==continent).group_by(BuildingInfo.country)

    return render_template('country.html', buildings=buildings)

@app.route('/buildingcatalog/<string:continent>/<string:country>/building/')
def showBuildings(continent, country):
    buildings = session.query(BuildingInfo).filter(BuildingInfo.continent==continent, BuildingInfo.country==country).order_by(asc(BuildingInfo.name))
    return render_template('buildings.html', buildings=buildings)


@app.route('/building/<int:building_id>/')
@app.route('/building/<int:building_id>/details/')
def showInfo(building_id):
    building = session.query(Building).filter_by(id=building_id).one()
    # creator = getUserInfo(building.user_id)
    info = session.query(BuildingInfo).filter_by(building_id=building_id).all()
    #if 'username' not in login_session or creator.id != login_session['user_id']:
    #     return render_template('publicmenu.html', items=items, restaurant=restaurant, creator=creator)
    # else:
    return render_template('info.html', info=info, building=building)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
