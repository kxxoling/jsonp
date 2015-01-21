# -*- coding: utf-8 -*-
from flask import Flask, request
import requests


app = Flask(__name__)


@app.route('/')
def jsonp_service():
    callback = request.args.get('callback')
    url = request.args.get('url')
    orig_req = requests.get(url)
    content = orig_req.content
    return 'try{%s(%s)}catch(e){alert(e)}' % (str(callback), content)      # callback 为 unicode 类型，需要先转换为 str 类型


if __name__ == '__main__':
    app.run(debug=True)
