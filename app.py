from flask import Flask
app = Flask(__name__)
@app.route("/")
def welcome():
    return(
        '''
        welcome, not sure what goes here, sorry
        Available Route:
        /api/v1.0/june_list
        /api/v1.0/december_list
        ''')

       