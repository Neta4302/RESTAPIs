import json
from flask import Flask, jsonify, request

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok"},
    {"id": 2, "name": "Australia", "capital": "Canberra"},
    {"id": 3, "name": "USA", "capital": "LA"}
]

nextCountryId = 4

@app.route('/country', methods=['GET'])
def get_country():
  return jsonify(countries)

@app.route('/country/<int:id>', methods=['GET'])
def get_country_id(id: int):
  country = _find_next_id(id)
  return jsonify(countries)

def _find_next_id(id: int):
  return next((x for x in countries if x['id'] == id), None)

@app.route('/country', methods=['POST'])
def post_country():
  global nextCountryId
  country = json.loads(request.data)

  country['id'] = nextCountryId
  nextCountryId += 1
  countries.append(country)

  return '', 201, { 'location': f'/countries/{country["id"]}' }

@app.route('/country/<int:id>', methods=['PUT'])
def put_country(id: int):
  country = _find_next_id(id)
  if country is None:
    return jsonify({ 'error': 'Country does not exist.' }), 404

  updated_country = json.loads(request.data)
  country.update(updated_country)
  return jsonify(country)

@app.route('/country/<int:id>', methods=['PATCH'])
def patch_country(id: int):
  country = _find_next_id(id)
  if country is None:
    return jsonify({ 'error': 'Country does not exist.' }), 404

  updated_country = json.loads(request.data)
  country.update(updated_country)
  return jsonify(country)

@app.route('/country/<int:id>', methods=['DELETE'])
def delete_country(id: int):
  global countries
  country = _find_next_id(id)
  if country is None:
    return jsonify({ 'error': 'Country does not exist.' }), 404

  countries = [x for x in countries if x['id'] != id]
  return jsonify(country), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)