from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Se modularizan las vistas de ciudades.
ciudadmod = Blueprint("ciudad", __name__, template_folder="templates")

@ciudadmod.route('/')
def index():
    return"Hola Mundo en ciudad"