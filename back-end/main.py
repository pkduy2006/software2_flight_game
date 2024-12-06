import mysql.connector
from flask import Flask
from airport import Airport
from martyr import Martyr
from geopy import distance
import random

app = Flask(__name__)

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'final_game',
    user = 'root',
    password = '16102006',
    autocommit = True
)

def get_airports():
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
    return result

def set_up_base_and_target(airports):
    x_base = airports[0]['latitude_deg']
    y_base = airports[0]['longitude_deg']

    x_target = airports[1]['latitude_deg']
    y_target = airports[1]['longitude_deg']

    while distance.distance((x_base, y_base), (x_target, y_target)).km <= 1136:
        random.shuffle(airports)

        x_base = airports[0]['latitude_deg']
        y_base = airports[0]['longitude_deg']

        x_target = airports[1]['latitude_deg']
        y_target = airports[1]['longitude_deg']

    return airports

def get_airport_type():
    sql = """SELECT * FROM airport_type;"""
    cursor = connection.cursor(dictionary = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

@app.route('/set_up_airports')
def set_up_airports():
    airports = get_airports()

    airports = set_up_base_and_target(airports)

    airport_id = 0
    final_airports = []
    airport_type = get_airport_type()
    for each in airport_type:
        for i in range(each['number']):
            airport_name = airports[airport_id]['airport_name']
            iso_country = airports[airport_id]['iso_country']
            municipality = airports[airport_id]['municipality']
            country = airports[airport_id]['country_name']
            ident = airports[airport_id]['ident']
            latitude_deg = airports[airport_id]['latitude_deg']
            longitude_deg = airports[airport_id]['longitude_deg']
            garrison = each['garrison']
            storage = each['storage']
            airport = Airport(airport_name, iso_country, municipality, country, ident, latitude_deg, longitude_deg, garrison, storage)
            final_airports.append(airport.combine_details())
            airport_id += 1

    return final_airports

@app.route('/get_monument_table')
def get_monument_table():
    martyrs = []
    sql = """SELECT * FROM monument;"""
    cursor = connection.cursor(dictionary = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    for each in result:
        martyr = Martyr(each['id'], each['name'], each['location'], each['total_enemy_killed'])
        martyrs.append(martyr.combine_details())
    return martyrs

if __name__ == '__main__':
    app.run(use_reloader = True, host = '127.0.0.1', port = 5000)
