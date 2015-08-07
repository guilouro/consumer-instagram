# coding: utf8
from flask import Flask, render_template, request, session, redirect
from instagram import client
import os

app = Flask('consumer-instagram')
app.secret_key = '\xcb\xf0\x83"\xbe\xeb\x85\xa6rm\x95\xfe\x10\x920\xef\xaf&rs\xf1\x11}P'

CONFIG = {
    'client_id': 'CLIENT_ID',
    'client_secret': 'CLIENT_SECRET',
    'redirect_uri': 'http://localhost:5000/auth_callback'
}


auth = client.InstagramAPI(**CONFIG)


@app.route('/')
@app.route('/<username>')
def index(username=None):

    if is_authorized():
        try:
            api = client.InstagramAPI(
                access_token=session['access_token'],
                client_secret=CONFIG['client_secret']
            )

            if username is None:
                user_id = api.user().id
            else:
                user_id = api.user_search(username)[0].id

            media = request_media(
                api.user_recent_media, {'user_id': user_id})

        except Exception as e:
            return render_template('msg.html', msg=e)

        text = request.values['text'] if 'text' in request.values else None
        return render_template('index.html', media=media, text=text)

    try:
        url = auth.get_authorize_url(scope=["likes", "comments"])
        return render_template('auth.html', url=url)
    except Exception as e:
        return render_template('msg.html', msg=e)


@app.route('/tag/<tag_name>')
def tag(tag_name):
    if not is_authorized():
        return redirect('/')

    try:
        api = client.InstagramAPI(
            access_token=session['access_token'],
            client_secret=CONFIG['client_secret']
        )

        media = request_media(api.tag_recent_media, {'tag_name': tag_name})

    except Exception as e:
        return render_template('msg.html', msg=e)

    text = request.values['text'] if 'text' in request.values else None
    return render_template('index.html', media=media, tag='#%s' % tag_name, text=text)


@app.route('/popular')
def popular():

    if not is_authorized():
        return redirect('/')

    try:
        api = client.InstagramAPI(
            access_token=session['access_token'],
            client_secret=CONFIG['client_secret']
        )
        media = api.media_popular(count=100)

    except Exception as e:
        return render_template('msg.html', msg=e)

    text = request.values['text'] if 'text' in request.values else None
    return render_template('index.html', media=media, text=text)


@app.route('/auth_callback', methods=['GET'])
def callback():
    code = request.values['code']
    if not code:
        return render_template('msg.html', msg='Missing code')
    try:
        access_token, user_info = auth.exchange_code_for_access_token(code)
        if not access_token:
            return render_template('msg.html',
                                   msg='Could not get access token')
        api = client.InstagramAPI(
            access_token, client_secret=CONFIG['client_secret'])
        session['access_token'] = access_token
        session['user_info'] = user_info
    except Exception as e:
        return render_template('msg.html', msg=e)

    return redirect('/')


def request_media(method, params={}):
    try:
        media, next_ = method(count=100, **params)
        while next_ and len(media) < 100:
            more_medias, next_ = method(
                with_next_url=next_, count=100, **params)
            media.extend(more_medias)
    except Exception as e:
        return render_template('msg.html', msg=e)

    return media


def is_authorized():
    return False if 'access_token' not in session else True


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
