from flask import Blueprint, jsonify
from os import listdir
from os.path import isfile, join, splitext

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.get("/models")
def index():
    path = "./models/"
    return jsonify(
        models=[splitext(f)[0] for f in listdir("./models/") if isfile(join(path,f))]
    )