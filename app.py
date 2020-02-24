import os
import json

from flask import Flask, make_response, send_from_directory, render_template, request

"""
GLOBAL VARIABLES ########################################################################################################
"""
app = Flask(__name__)
app.debug = False
app.config.update({
    "SECRET_KEY": "6w_#w*~AVts3!*yd&C]jP0(x_1ssd]MVgzfAw8%fF+c@|ih0s1H&yZQC&-u~O[--"  # For the session
})


config = {
    "okta_org": "https://mr2.oktapreview.com",
    "okta_issuer": "https://mr2.oktapreview.com/oauth2/default",
    "okta_client_id": "0oaptjqrjbqnsGCFL0h7",
    "okta_redirect_uri": "https://64ce115419584bd0ab36357c1b42c00b.vfs.cloud9.us-east-1.amazonaws.com/"
}


"""
ROUTES ##################################################################################################################
"""


@app.route('/<path:filename>')
def serve_static_html(filename):
    """ serve_static_html() generic route function to serve files in the 'static' folder """
    root_dir = os.path.dirname(os.path.realpath(__file__))
    return send_from_directory(os.path.join(root_dir, 'static'), filename)


@app.route('/')
def index():
    """ handler for the root url path of the app """
    print("index()")
    message = ""

    response = make_response(render_template("index.html", app_config=config, message=message))

    return response


@app.route('/token_exp_hook', methods=["POST"])
def token_exp_hook():
    print("token_exp_hook()")
    print("request.form: {0}".format(request.form))
    request_json = request.get_json()
    print("request.get_json(): {0}".format(request_json))
    
    response = {}
    return response
    
    
"""
MAIN ##################################################################################################################
"""
if __name__ == "__main__":
    # This is to run on c9.io.. you may need to change or make your own runner
    print( "config.app: {0}".format(json.dumps(config, indent=4, sort_keys=True)) )
    app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)))