from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, session
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

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = 'Building Catalog Application'

# Connect to Database and create database session.
engine = create_engine('sqlite:///buildinginfo1.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create an anti-forgery state token.
@app.route('/login/')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)

# Signs in with your gmail account
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token.
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code.
    code = request.data

    try:
        # Upgrade authorization code into credentials object.
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID." ), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valaid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's"), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for late use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info.
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION.
    login_session['provider'] = 'google'

    # See if user exists, if it doesn't make a new one.
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px; border-radius: 150px; -webkit-border-radius: 150px; -moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

# I want one for github and linkedin.
# @app.route('/gitconnect', methods=['POST'])
# def gitconnect():
#
# @app.route('/lconnect', methods=['POST'])
# def lconnect():

# JSON APIs to view Building Information:
# 1. JSON for specific building info.
@app.route('/buildingcatalog/<int:building_id>/info/JSON')
def buildingInfoJSON(building_id):
    building = session.query(Building).filter_by(id=building_id).first()
    items = session.query(BuildingInfo).filter_by(
        building_id=building_id).all()
    return jsonify(BuildingInfo=[i.serialize for i in items])

# 2. JSON for all the buildings
@app.route('/buildingcatalog/JSON')
def buildingsJSON():
    buildings = session.query(Building).all()
    return jsonify(buildings=[r.serialize for r in buildings])


# User Helper FUnctions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session['email'],
                   picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).first()
    return user.id

def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    return user

def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user is not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(
            json.dumps('Failed to revoke given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response

# Route link in header.html shows all buildings in database by name
@app.route('/allbuildings/')
def showAllBuildings():
    buildings = session.query(BuildingInfo).order_by(BuildingInfo.name)
    return render_template('showallbuildings.html', buildings=buildings)

# Home route, creates a list of all possible contients in the database.
@app.route('/')
@app.route('/buildingcatalog/')
def showContinents():
    continents = session.query(BuildingInfo).group_by(BuildingInfo.continent)
    return render_template('continents.html', continents=continents)

# Once you click a continent this route lists all countries in that continent
# with buildings in the databse.
@app.route('/buildingcatalog/<string:continent>/')
def showCountry(continent):
    buildings = session.query(BuildingInfo).filter(BuildingInfo.continent==continent).group_by(BuildingInfo.country)

    return render_template('country.html', buildings=buildings)

# Once you click the country you want, this route lists all buildings in that
# country.
@app.route('/buildingcatalog/<string:continent>/<string:country>/building/')
def showBuildings(continent, country):
    buildings = session.query(BuildingInfo).filter(BuildingInfo.continent==continent, BuildingInfo.country==country).order_by(asc(BuildingInfo.name))
    return render_template('buildings.html', buildings=buildings)

# Once you click the building you want, this route will display the information
# in re to that building.
@app.route('/building/<string:building_name>/details/')
def showInfo(building_name):
    building = session.query(BuildingInfo).filter_by(name=building_name).first()
    # creator = getUserInfo(building.user_id)
    info = session.query(BuildingInfo).filter_by(name=building_name).all()
    #if 'username' not in login_session or creator.id != login_session['user_id']:
    #     return render_template('publicmenu.html', items=items, restaurant=restaurant, creator=creator)
    # else:
    return render_template('info.html', info=info, building=building)

# The route allows the user to create a new building.
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

# This route edits the building you selected with the showInfo route.
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

# This route lets you delete the building you selected int eh showInfo route.
@app.route('/building/<string:building_name>/details/delete/', methods=['GET', 'POST'])
def deleteBuilding(building_name):
    buildingToDelete = session.query(BuildingInfo).filter_by(name=building_name).first()
    if request.method == 'POST':
        session.delete(buildingToDelete)
        session.commit()
        return redirect(url_for('showBuildings', continent=buildingToDelete.continent, country=buildingToDelete.country))
    else:
        return render_template('deleteconfirmation.html', building=buildingToDelete)

# disconnect based on provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['picture']
            del login_session['user_id']
            del login_session['gplus_id']
            del login_session['access_token']
        del login_session['username']
        del login_session['email']
        # del login_session['picture']
        # del login_session['user_id']
        del login_session['provider']
        flash("You have Successfully been logged out.")
        return redirect(url_for('showContinents'))
    else:
        flash("You were not loggin in.")
        return redirect(url_for('showContients'))

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
