# coding=utf-8

from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/health')
def show_health():
    # show health status for eurake
    health_status = {"status": "UP"}
    # 返回内容 html/text
    # return json.dumps(health_status)
    # 返回内容 html/json
    return jsonify(health_status)


if __name__ == '__main__':
    # threaded=True 开启多线程，防止卡死
    app.run('192.168.1.113', 8010, threaded=True)
