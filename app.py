from flask import Flask
from MARKET_BASKET_PROJECT.logger import logging

app= Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():

    logging.info("Executing the code this is the test for log file")
    return "This is the project about market basket analysis"

if __name__=="__main__":
    app.run(debug=True)

