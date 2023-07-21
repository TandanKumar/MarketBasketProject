from flask import Flask
from MARKET_BASKET_PROJECT.logger import logging
import os
from MARKET_BASKET_PROJECT.exception import MARKET_BASKET_PROJECT_Exception
import sys
app= Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():

    try:
        raise Exception ("We are testing the custom exception")
    
    except Exception as e:
        mbp = MARKET_BASKET_PROJECT_Exception(e,sys)
        logging.info(mbp.error_message)
        logging.info("Executing the code this is the test for log file")
        return "This is the project about market basket analysis"
    


if __name__=="__main__":
    app.run(debug=True)

