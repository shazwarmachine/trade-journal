import logging
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

kite = KiteConnect(api_key="35msa178vtcy64ws")


# Redirect the user to the login url obtained
# from kite.login_url(), and receive the request_token
# from the registered redirect url after the login flow.
# Once you have the request_token, obtain the access_token
# as follows.
print(kite.login_url())
# data = kite.generate_session("USY5sK47LqE5b8zylt4FDQ2XY1aTY2Rv", api_secret="o816jxsbhtrcz0z163242ahvgvtd6w6w")
# print(data)
# kite.set_access_token("USY5sK47LqE5b8zylt4FDQ2XY1aTY2Rv")
# kite.holdings()
# kite.trades()
# kite.profile()

def generate_session_using_request_token(request_token):
    """
    Generates a session using the request token.
    Returns the access token and user ID.
    """

    data = kite.generate_session(request_token, api_secret="o816jxsbhtrcz0z163242ahvgvtd6w6w")
    kite.set_access_token(data["access_token"])
    print(data["access_token"])


def login_init():
    """
    Authenticates a user with the given username and password.
    Returns True if authentication is successful, False otherwise.
    """
    # TODO: Implement authentication logic
    return kite.holdings()
    
