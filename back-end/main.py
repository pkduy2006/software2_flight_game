import mysql.connector
from flask import Flask
from airport import Airport
from martyr import Martyr

app = Flask(__name__)

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'version1',
    user = 'root',
    password = '16102006',
    autocommit = True
)

@app.route('/get_airports')
def get_airports():
    airports = []
    sql = """SELECT airport.name as 'airport_name', airport.iso_country as 'iso_country', airport.municipality as 'municipality', country.name as 'country',
airport.ident as 'ident', airport.latitude_deg as 'latitude_deg', airport.longitude_deg as 'longitude_deg'
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
        airport = Airport(each['airport_name'], each['iso_country'], each['municipality'], each['country'], each['ident'], each['latitude_deg'], each['longitude_deg'])
        airports.append(airport.combine_details())
    return airports

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
