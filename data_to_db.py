import pandas as pd
from pandas_gbq import to_gbq

###loading the data
df=pd.read_csv('assessment_dataset.csv')

###EDA on dataset


###pushing data to cloud data warehouse in this case Bigquery
###directly pushing it using to_gbq but for production we can use gcloud auth with credentials file
project='test-74ac1'
dataset='sales_data.sales_table'
df.to_gbq(dataset, project_id=project, if_exists='replace')
