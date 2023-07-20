"""import logging
from datetime import datetime
import os
import pandas as pd
from MARKET_BASKET_PROJECT.constant import get_current_time_stamp 

LOG_DIR="MARKET_BASKET_PROJECT_logs"

def get_log_file_name():
    return f"log_{get_current_time_stamp()}.log"

LOG_FILE_NAME=get_log_file_name()

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

print("This is the logger file")
print(LOG_FILE_PATH)

logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s] %(levelname)s - %(name)s - %(message)s',
level=logging.INFO
)

logging.info("Inside logger")

def get_log_dataframe(file_path):
    data=[]
    with open(file_path) as log_file:
        for line in log_file.readlines():
            data.append(line.split("^;"))

    log_df = pd.DataFrame(data)
    columns=["Time stamp","Log Level","line number","file name","function name","message"]
    log_df.columns=columns
    
    log_df["log_message"] = log_df['Time stamp'].astype(str) +":$"+ log_df["message"]

    return log_df[["log_message"]]

"""



import logging
import os
from datetime import datetime

LOG_DIR ="MARKETBASKET_log"
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename= LOG_FILE_PATH,
filemode="w",
format = '[%(asctime)s] %(name)s  -  %(levelname)s - %(message)s',
level = logging.INFO

)