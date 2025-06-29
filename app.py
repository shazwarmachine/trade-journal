from flask import Flask, request
from Login import login_init
import webbrowser
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'


@app.route('/loginUrl')
def login_url():
    """
    This route is used to get the login URL for Kite Connect.
    It should return the URL that the user should visit to log in.
    """
    return { "login_url": login_init.kite.login_url() }
@app.route('/login')
def login():
    # return "ascasca"
    return login_init.login_init()

@app.route('/redirect')
def redirect():
    """
    This route is used to handle the redirect after login.
    It should capture the request token and generate the access token.
    """
    login_init.generate_session_using_request_token(request.args.get('request_token'))
    webbrowser.open('http://localhost:9003/')
    return {"userDetails":  login_init.kite.profile()}

@app.route('/holdingsDetails')
def holdings_details():
    """
    This route is used to get the holdings details of the user.
    It should return the holdings information.
    """
    return {"holdings": login_init.kite.holdings()}
if __name__ == '__main__':
    app.run()
