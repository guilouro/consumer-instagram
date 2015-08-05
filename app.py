# coding: utf8
from flask import Flask, render_template
from instagram import client
import os

app = Flask('consumer-instagram')

CONFIG = {
    'client_id': '77da745ad09b49389fc1af582f4f9da2',
    'client_secret': '56bd0896031a4ac0830511c887199a94',
    'redirect_uri': 'http://localhost:5000/auth_callback'
}


auth = client.InstagramAPI(**CONFIG)


@app.route('/')
def index():
    try:
        url = auth.get_authorize_url(scope=["likes", "comments"])
        return render_template('auth.html', url=url)
    except Exception as e:
        print e

    return 'teste'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)