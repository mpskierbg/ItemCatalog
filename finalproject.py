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

@app.route('/buildingcatalog/<string:continent>/')
def showCountry(continent):
    buildings = session.query(BuildingInfo).filter(BuildingInfo.continent==continent).group_by(BuildingInfo.country)

    return render_template('country.html', buildings=buildings)

@app.route('/buildingcatalog/<string:continent>/<string:country>/building/')
def showBuildings(continent, country):
    buildings = session.query(BuildingInfo).filter(BuildingInfo.continent==continent, BuildingInfo.country==country).order_by(asc(BuildingInfo.name))
    return render_template('buildings.html', buildings=buildings)

@app.route('/building/new/', methods=['GET', 'POST'])
def newBuilding():
    # if 'username' not in login_session:
    #     return redirect('/login')
    if request.method == 'POST':
        newBuilding = BuildingInfo(
            name=request.form['name'],
            #user_id=login_session['user_id'],
            continent=request.form['continent'],
            country=request.form['country'])
        session.add(newBuilding)
        flash('New Building %s Successfully Created' % newBuilding.name)
        session.commit()
        return redirect(url_for('showContinents'))
    else:
        return render_template('newBuilding.html')

@app.route('/building/<string:building_name>/details/')
def showInfo(building_name):
    building = session.query(BuildingInfo).filter_by(name=building_name).first()
    # creator = getUserInfo(building.user_id)
    info = session.query(BuildingInfo).filter_by(name=building_name).all()
    #if 'username' not in login_session or creator.id != login_session['user_id']:
    #     return render_template('publicmenu.html', items=items, restaurant=restaurant, creator=creator)
    # else:
    return render_template('info.html', info=info, building=building)

@app.route('/building/<string:building_name>/details/edit/', methods=['GET', 'POST'])
def editBuildingInfo(building_name):
    # if 'username' not in login_session:
    #     return redirect('/login')

    editedBuilding = session.query(BuildingInfo).filter_by(name=building_name).first()
    #if login_session['user_id'] != restaurant.user_id:
    #    return "<script>function myFunction() {alert('You are not authorized to edit menu items to this restaurant. Please create your own restaurant in order to edit items.');}</script><body onload='myFunction()'>"
    if request.method == 'POST':
        if request.form['name']:
            editedBuilding.name = request.form['name']
        if request.form['description']:
            editedBuilding.description = request.form['description']
        if request.form['style']:
            editedBuilding.style = request.form['style']
        if request.form['continent']:
            editedBuilding.continent = request.form['continent']
        if request.form['country']:
            editedBuilding.country = request.form['country']
        if request.form['year_completed']:
            editedBuilding.year_completed = request.form['year_completed']
        if request.form['height']:
            editedBuilding.height = request.form['height']
        if request.form['floors']:
            editedBuilding.floors = request.form['floors']
        if request.form['architect']:
            editedBuilding.architect = request.form['architect']
        # added toggles or radios for tallest building
        session.add(editedBuilding)
        session.commit()
        flash('Menu Item Successfully Edited')
        return redirect(url_for('showInfo', building_name=editedBuilding.name))
    else:
        return render_template('editbuildinginfo.html', building=editedBuilding)

@app.route('/building/<string:building_name>/details/delete/', methods=['GET', 'POST'])
def deleteBuilding(building_name):
    buildingToDelete = session.query(BuildingInfo).filter_by(name=building_name).first()
    if request.method == 'POST':
        session.delete(buildingToDelete)
        session.commit()
        return redirect(url_for('showBuildings', continent=buildingToDelete.continent, country=buildingToDelete.country))
    else:
        return render_template('deleteconfirmation.html', building=buildingToDelete)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
