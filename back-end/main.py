import mysql.connector
from flask import Flask, Response
from flask_cors import CORS

from airport import Airport
from martyr import Martyr
from geopy import distance
import random
import json

app = Flask(__name__)
CORS(app)

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'final_game',
    user = 'root',
    password = '16102006',
    autocommit = True
)

airports = []

def set_up():
    sql = """SELECT airport.name as 'airport_name', airport.iso_country as 'iso_country', airport.municipality as 'municipality', country.name as
'country_name', airport.ident as 'ident', airport.latitude_deg as 'latitude_deg', airport.longitude_deg as 'longitude_deg'
    FROM airport, country
    WHERE airport.iso_country = country.iso_country
    AND airport.continent = 'EU'
    AND airport.type = 'large_airport'
    AND airport.iso_country NOT IN (SELECT airport.iso_country FROM airport WHERE iso_country = 'RU')
    ORDER BY RAND();"""
    cursor = connection.cursor(dictionary = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    for each in result:
        airport_name = each['airport_name']
        iso_country = each['iso_country']
        municipality = each['municipality']
        country = each['country_name']
        ident = each['ident']
        latitude_deg = each['latitude_deg']
        longitude_deg = each['longitude_deg']
        airport = Airport(airport_name, iso_country, municipality, country, ident, latitude_deg, longitude_deg)
        airports.append(airport.combine_details())

set_up()

@app.route('/get_airports')
def get_airports():
    return airports

def get_airport_type():
    sql = """SELECT * FROM airport_type;"""
    cursor = connection.cursor(dictionary = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

@app.route('/find_target/base=<base>')
def find_target(base):
    base_latitude_deg = None
    base_longitude_deg = None
    for airport in airports:
        if airport['ident'] == base:
            base_latitude_deg = airport['latitude_deg']
            base_longitude_deg = airport['longitude_deg']

    for airport in airports:
        if airport['ident'] != base and distance.distance((airport['latitude_deg'], airport['longitude_deg']), (base_latitude_deg, base_longitude_deg)).km > 1137:
            return airport['ident']

@app.route('/set_up_airports/base=<base>&target=<target>')
def set_up_airports(base, target):
    airport_id = 0
    airport_type = get_airport_type()
    for each in airport_type:
        for i in range(each['number']):
            if airports[airport_id]['ident'] != base or airports[airport_id]['ident'] != target:
                airports[airport_id]['garrison'] = each['garrison']
                airports[airport_id]['storage'] = each['storage']
                airports[airport_id]['hide_garrison'] = bool(random.getrandbits(1))
                airports[airport_id]['hide_storage'] = bool(random.getrandbits(1))
                airport_id += 1

    return airports

@app.route('/get_monument_table')
def get_monument_table():
    martyrs = []
    sql = """SELECT * FROM monument;"""
    cursor = connection.cursor(dictionary = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    for each in result:
        martyr = Martyr(each['id'], each['martyr_name'], each['location'], each['total_enemy_killed'], each['distance_travelled'])
        martyrs.append(martyr.combine_details())
    return martyrs

@app.route('/get_distance/start=<start>&end=<end>')
def get_distance(start, end):
    start_x = None
    start_y = None
    end_x = None
    end_y = None
    for airport in airports:
        if airport['ident'] == start:
            start_x = airport['latitude_deg']
            start_y = airport['longitude_deg']
        if airport['ident'] == end:
            end_x = airport['latitude_deg']
            end_y = airport['longitude_deg']
    dist = distance.distance((start_x, start_y), (end_x, end_y)).km
    rounded_dist = round(dist, 1)
    response = {"Distance in km": rounded_dist}
    return response

@app.route('/get_details_of_specific_airport/airport=<code>')
def get_details_of_specific_airport(code):
    try:
        response = {}
        for airport in airports:
            if airport['ident'] == code:
                response = airport
        if response == {}:
            raise Exception(ValueError)
        else:
            return response
    except ValueError:
        response = {"message": "Invalid ICAO code",
                    "status": 400}
        json_response = json.dumps(response)
        http_response = Response(response = json_response, status = 400, mimetype = 'application/json')
        return http_response

@app.route('/details_of_loser/name=<name>&location=<location>&total_enemy_killed=<total_enemy_killed>&distance_travelled=<distance_travelled>')
def insert_details_of_loser(name, location, total_enemy_killed, distance_travelled):
    sql = """INSERT INTO monument(martyr_name, location, total_enemy_killed, distance_travelled) VALUES (%s, %s, %s, %s);"""
    cursor = connection.cursor(dictionary = True)
    cursor.execute(sql, (name, location, total_enemy_killed, distance_travelled))
    response = {"message": "Successfully inserted",
                "status": 200}

    return response

@app.route('/locate/code=<code>')
def locate(code):
    sql = """SELECT airport.name as 'name', airport.municipality as 'municipality', country.name as 'country'
    FROM airport, country
    WHERE airport.iso_country = country.iso_country
    AND airport.ident = %s;"""
    cursor = connection.cursor(dictionary = True)
    cursor.execute(sql, (code,))
    result = cursor.fetchone()
    response = {'Name': result['name'],
                'Municipality': result['municipality'],
                'Country': result['country']}
    return response

@app.errorhandler(404)
def page_not_found(e):
    response = {"message": "Invalid endpoint.",
                "status": 404}
    json_response = json.dumps(response)
    http_response = Response(response = json_response, status = 404, mimetype = 'application/json')
    return http_response

if __name__ == '__main__':
    app.run(use_reloader = True, host = '127.0.0.1', port = 5000)