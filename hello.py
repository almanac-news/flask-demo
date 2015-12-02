# import the Flask class here, an instance will be our WSGI application
from flask import Flask
# create an instance of this class, use naming convention if single module
app = Flask(__name__)

# route() decorator used to tell Flask what URL should trigger the function
@app.route('/')
# function is given a name which is also used to generate URLs
def hello_world():
    return 'Hello World!'

# only call run after making sure the script is executed directly from the Python interpreter
if __name__ == '__main__':
    app.run()

# other: default is in debugging mode a user of the app
# if debug is disabled, you can simply change the call to look like
# app.run(host='0.0.0.0') - so your OS will listen on all public IPs
