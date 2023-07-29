from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/",methods = ['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/jjjson', methods = ['GET','POST'])
def jjjson():
    # json をもらってきてデコードしたい
    param = json.loads(request.data.decode('utf-8'))
    col1 = param.get('abc')
    print(col1)     # 123
    # return {"result": "OK"}
    # json エンコードして返却する
    return json.dumps(param).encode('utf-8')

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8888)
