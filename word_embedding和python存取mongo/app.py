from flask import Flask, jsonify
import pymongo

#from flask_cors import CORS

app = Flask(__name__)  # __name__ 代表目前執行的模組
@app.route("/")  # 函式的裝飾 decorator:以函示為基礎 提供附加功能
def home():
    print("hello")
    return "Hello Flask"


@app.route("/time", methods=['GET'])  # 函式的裝飾 decorator:以函示為基礎 提供附加功能
def time():
    print('time')
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["test6"]
    mycol = mydb["coll6"]
    x = mycol.find()
    response = jsonify(x[6]['time'])
    return response


# 函式的裝飾 decorator:以函示為基礎 提供附加功能
@app.route("/relation_vector", methods=['GET'])
def relation_vector():
    print('relation_vector')
    #response = jsonify({'message': 'store  found'})
    # 對flask server進行跨域
    #response.headers.add('Access-Control-Allow-Origin', '*')
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["test6"]
    mycol = mydb["coll6"]
    x = mycol.find()
    # print(len(x[0]['relation_vector']))
    # print(len(x[1]['sub_vector']))
    # print(len(x[2]['obj_vector']))
    # print(len(x[3]['embed_sub']))
    # print(len(x[4]['embed_relation']))
    # print(len(x[5]['embed_obj']))
    response = jsonify(x[1]['relation_vector'])
    return response


@app.route("/sub_vector", methods=['GET'])  # 函式的裝飾 decorator:以函示為基礎 提供附加功能
def sub_vector():
    print('sub_vector')
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["test6"]
    mycol = mydb["coll6"]
    x = mycol.find()
    response = jsonify(x[0]['sub_vector'])
    return response


@app.route("/obj_vector", methods=['GET'])  # 函式的裝飾 decorator:以函示為基礎 提供附加功能
def obj_vector():
    print('obj_vector')
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["test6"]
    mycol = mydb["coll6"]
    x = mycol.find()
    response = jsonify(x[2]['obj_vector'])
    return response


@app.route("/embed_sub", methods=['GET'])  # 函式的裝飾 decorator:以函示為基礎 提供附加功能
def embed_sub():
    print('embed_sub')
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["test6"]
    mycol = mydb["coll6"]
    x = mycol.find()
    response = jsonify(x[3]['embed_sub'])
    return response


@app.route("/embed_relation", methods=['GET'])  # 函式的裝飾 decorator:以函示為基礎 提供附加功能
def embed_relation():
    print('embed_relation')
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["test6"]
    mycol = mydb["coll6"]
    x = mycol.find()
    response = jsonify(x[4]['embed_relation'])
    return response


@app.route("/embed_obj", methods=['GET'])  # 函式的裝飾 decorator:以函示為基礎 提供附加功能
def embed_obj():
    print('embed_obj')
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["test6"]
    mycol = mydb["coll6"]
    x = mycol.find()
    response = jsonify(x[5]['embed_obj'])
    return response


if __name__ == "__main__":  # 如果以主程式執行
    app.run(debug=True, host='0.0.0.0', port=3000)  # 立即啟動伺服器
#    CORS(app)
