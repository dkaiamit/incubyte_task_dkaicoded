import pandas as pd
from pandas_gbq import to_gbq

###loading the data
df=pd.read_csv('assessment_dataset.csv')

###EDA on dataset


###pushing data to cloud data warehouse in this case Bigquery
###directly pushing it using to_gbq but for production we can use gcloud auth with credentials file

#####for production we can use this method just need to provide credentials file along with project id
# credentials = service_account.Credentials.from_service_account_file("service_account.json")
# client = bigquery.Client(credentials=credentials, project='test-74ac1')
# table_id = "'test-74ac1.sales_data.sales_table"
# job = client.load_table_from_dataframe(df, table_id, job_config=bigquery.LoadJobConfig(schema=schema))
# job.result()


project='test-74ac1'
dataset='sales_data.sales_table'
df.to_gbq(dataset, project_id=project, if_exists='replace')
