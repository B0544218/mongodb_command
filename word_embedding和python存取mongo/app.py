from flask import Flask, jsonify
import pymongo

app = Flask(__name__)  # __name__ 代表目前執行的模組
@app.route("/")  # 函式的裝飾 decorator:以函示為基礎 提供附加功能
def home():
    print("hello")
    return "Hello Flask"


@app.route("/test", methods=['GET'])  # GET替代 POST
def test():
    print('test')
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
    response = jsonify(x[4]['embed_relation'])
    return response


if __name__ == "__main__":  # 如果以主程式執行
    app.run(host='127.0.0.1', port=3001)  # 立即啟動伺服器
