from flask import Flask
from flask import request, jsonify, send_from_directory
from flask_cors import CORS
from id_front import *
import base64
import numpy as np
import cv2
import json
import traceback
import sys
import requests

app = Flask(__name__)
app = Flask(__name__, static_folder='public')
app.config['JSON_AS_ASCII'] = False
CORS(app)


processor_dict = {"idfront":IdFrontProcessor, "idback":None}

@app.route("/health",methods=["GET"])
def health():
    return "Healthy", 200

@app.route('/read', methods=["Post"])
def process():
    response_err = "Bad Request"
    debug = False
    try:
        image = None
        image = request.get_data()
        if "image" in request.files:
            image = request.files["image"].read()
        if not image:
            response_err = "Image is Empty"
            raise Exception()
        if "debug" in request.form:
            debug = True
        image = np.asarray(bytearray(image), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        reader = IdFrontProcessor(debug=debug)
        fields = ["photo", "name_ge", "name_en", "last_name_ge", "last_name_en", "person_id", "card_id", "exp_date", "birth_date", "nation", "sex"]
        response = reader.process(image, fields)
        if debug:
            if 'photo' in response:
                success, image_string = cv2.imencode(".png", response["photo"])
                if success:
                    response["photo"] = base64.b64encode(image_string).decode("ascii")

            success, image_string = cv2.imencode(".png", response["detected_rect"])
            if success:
                response["detected_rect"] = base64.b64encode(image_string).decode("ascii")

            for field, field_img in response["field"].items():
                success, image_string = cv2.imencode(".png", field_img)
                if success:
                    response["field"][field] = base64.b64encode(image_string).decode("ascii")

        response_code = 200
        
    except Exception as exp:
        traceback.print_exc(file=sys.stdout)
        image = None
        response = response_err
        response_code = 400

    return jsonify(response), response_code



@app.route('/<string:page_name>', methods = ["GET"])
def render_static(page_name):
    return send_from_directory(app.static_folder, page_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=True)

