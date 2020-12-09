#!flask/bin/python
# -- coding: utf-8 --

__author__ = 'cloudtogo'

from flask import Flask


app = Flask(__name__)

# 请您来修正Hello, word的拼写错误吧！
# 请在修改完成后，通过主菜单 Git/Commit ... 菜单项完成代码的Commit 和 Push。
# Push完成后回到Factory ( http://factory.cloudtogo.cn/project/blueprint?id=last )，用同样的方法发布一个新实例即可看到修改后的效果。
#  测试这个自动触发水电费水电费第三方的额外aaaaaaadfdf  fdsfdsfdsfsaaaaa啊啊啊多福多寿双方都啊啊啊



@app.route('/')
def hello():
    return "测试代码提交触发自动构建"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
