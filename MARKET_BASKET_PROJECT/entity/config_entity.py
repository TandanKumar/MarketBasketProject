from collections import namedtuple

DataIngestionConfig =  namedtuple("DataIngestionConfig",
                        [  "dataset_download_url","tgz_download_dir" , "raw_data_dir" ,"Ingested_train_dir","Ingested_test_dir"])
