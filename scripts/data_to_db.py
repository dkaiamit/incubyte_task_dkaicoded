import pandas as pd
from google.cloud import bigquery
import pyarrow
from google.oauth2 import service_account
import db_dtypes
import os

# Path to service account key file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_PATH = os.path.join(BASE_DIR, "credentials", "credentials.json")
key_path = CREDENTIALS_PATH
dataset_path=os.path.join(BASE_DIR,"dataset","assessment_dataset.csv")

# Initialize BigQuery client
credentials = service_account.Credentials.from_service_account_file(key_path)
client =  bigquery.Client(credentials=credentials, project=credentials.project_id)

# Define BigQuery table details
project_id = str(credentials.project_id)
datasets = list(client.list_datasets())
for dataset in datasets:
    dataset_id = str(dataset.dataset_id)
table_id = "sales_table"
table_path = f"{project_id}.{dataset_id}.{table_id}"

df=pd.read_csv(dataset_path)
query = f"SELECT DISTINCT(TransactionID) FROM `{project_id}.{dataset_id}.{table_id}`"
existing_df = client.query(query).to_dataframe()


df = df[~df["TransactionID"].isin(existing_df["TransactionID"])]


job_config = bigquery.LoadJobConfig(
    autodetect=True, 
    write_disposition=bigquery.WriteDisposition.WRITE_APPEND,  #Appending Data 
    # schema_update_options=[bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION]
)

# Upload DataFrame to BigQuery
if not df.empty:
    job = client.load_table_from_dataframe(df, table_path, job_config=job_config)
    job.result()  # Wait for job to complete
    print("New data uploaded successfully!")
else:
    print("No new data to upload.")