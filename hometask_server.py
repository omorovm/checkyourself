from flask import Flask, jsonify, request
from hometask import *

app = Flask(__name__)

@app.route('/get_items/', methods= ['GET'])
def get_items():
    items = get_item()
    return jsonify({"data":items})

@app.route('/create_items/', methods= ['POST'])
def create_item_rq():
    data = request.get_json()
    create_item(data)
    return jsonify({'message':'created successfully'})

@app.route('/retrieve_items/<int:item_id>/', methods= ['GET'])
def get_one_item(item_id):
    item = retrieve(item_id)
    if item:
        return jsonify({'data': item})
    return jsonify({'message': 'not found'})   

@app.route("/update_items/<int:item_id>/",methods = ['PUT'])
def update_items(item_id):
    try:
        data = request.get_json()
        update_item(item_id,data)
        return f'Успешно,поле с id = {item_id} изменилось на {data}'
    except:
        return f'Ошибка, неверные входные данные'
    

@app.route("/delete_items/<int:item_id>/",methods = ['DELETE'])
def delete_items(item_id):
    try:
        delete_item(item_id)
        return f'Успешно удалено поле с id = {item_id}'
    except:
        return 'Ошибка' 

app.run(host = 'localhost', port = 8000)