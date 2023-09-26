#!/usr/bin/env python3
from flask import Flask, make_response
from flask_migrate import Migrate
from models import db, Zookeeper, Enclosure, Animal
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)
db.init_app(app)
@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    return ''
    animal = Animal.query.get(id)
    if animal:
        return f'Animal ID: {animal.id}<br>Name: {animal.name}<br>Species: {animal.species}<br>Zookeeper ID: {animal.zookeeper_id}<br>Enclosure: {animal.enclosure_id}'
    else:
        return 'Animal not found'

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    return ''
    zookeeper = Zookeeper.query.get(id)
    if zookeeper:
        return f'Zookeeper ID: {zookeeper.id}<br>Name: {zookeeper.name}<br>Birthday: {zookeeper.birthday}'
    else:
        return 'Zookeeper not found'


@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    return ''
    enclosure = Enclosure.query.get(id)
    if enclosure:
        return f'Enclosure ID: {enclosure.id}<br>Environment: {enclosure.environment}<br>Open to Visitors: {enclosure.open_to_visitors}'
    else:
        return 'Enclosure not found'


if __name__ == '__main__':
    