#!flask/bin/python
# -- coding: utf-8 --

__author__ = 'methodot'

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return "测试代码提交触发自动构建"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
