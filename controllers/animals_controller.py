from models.cat import Cat
from models.dog import Dog
from models.boa_constrictor import BoaConstrictor
from models.ferret import Ferret
from flask import jsonify, Blueprint, redirect, request

animals_bp = Blueprint('animals', __name__, url_prefix='/animals')

@animals_bp.route('/')
def index():
    return redirect('/')

@animals_bp.route('/cat')
def cat():
    if request.method == 'GET':
        cat = Cat( 'Misifus', 8.3, 6)

        return jsonify({"sound": cat.make_sound()}), 201
    
@animals_bp.route('/dog')
def dog():
    if request.method == 'GET':
        dog = Dog( 'Kaiser', 13.6, 8)

        return jsonify({"sound": dog.make_sound()}), 201

@animals_bp.route('/boa_constrictor')
def boa_constrictor():
    if request.method == 'GET':
        boa_constrictor = BoaConstrictor(name='Eleonora', age=12,weight=20.4, originCountry='Colombia',taxes=12000.1)

        return jsonify({"sound": boa_constrictor.make_sound()}), 201

@animals_bp.route('/ferret')
def ferret():
    if request.method == 'GET':
        ferret = Ferret(name='Hugo', age=2,weight=0.4, originCountry='Mexico',taxes=1230.12)

        return jsonify({"sound": ferret.make_sound()}), 201
