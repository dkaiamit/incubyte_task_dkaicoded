# BigQuery Data Ingestion with Airflow and Docker

This project reads a CSV file and writes its data to Google BigQuery using Apache Airflow. The project is containerized using Docker and is fully managed through Airflow.

## Project Structure

. ├── dags/ # Contains Airflow DAGs for orchestrating tasks 
  │ ├── mainDAG.py # DAG to read CSV and push data to BigQuery 
  ├── scripts/ # Contains Python scripts for data processing 
  │ ├── data_to_db.py # Script to read CSV and push to BigQuery 
  ├── dataset/ # Contains the CSV file that is ingested into BigQuery 
  │ ├── assessment_dataset.csv # Sample dataset file 
  ├── credentials/ # (User needs to create) Contains Google Cloud credentials for authentication 
  │ ├──credentials.json 
  ├── docker-compose.yml # Defines the Docker environment 
  ├── requirements.txt # List of dependencies for the project 
  ├── README.md # Project documentation


## Prerequisites

Before running the project, ensure you have:

1. **Docker & Docker Compose** installed.  
2. **Google Cloud Account** with BigQuery API enabled.  
3. **Google Cloud Credentials** JSON file for authentication.

## Setup Guide

### Step 1: Clone the Repository

```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```


### Step 2: Set Up Google Cloud Credentials

Create a folder named **credentials** inside the project root.
Place your **credentials.json** file inside this folder.

### Step 3: Update Airflow Environment Variables (Optional)

If needed, update the AIRFLOW and other environment variables in the docker-compose.yml file.

### Step 4: Start the Docker Containers

Run the following command to start Airflow and the necessary services:

```sh
docker-compose up -d
```

### Step 5: Access Airflow UI

Once the containers are running, open your browser and go to:
```sh
http://localhost:8080
```

Login with the default credentials:

```sh 
Username: admin
Password: admin
```
### Step 6: Install Dependencies

Enter the Airflow scheduler container and install the required dependencies:

```sh
docker exec -it <container_id> bash
pip install -r requirements.txt
```

### Step 7: Upload Data to BigQuery
Ensure the DAG mainDAG.py is present in the dags/ folder.
Navigate to the Airflow UI → DAGs → Trigger the DAG.
This will read the CSV from dataset/assessment_dataset.csv and push it to BigQuery.

### Step 8: Verify Data in BigQuery
Open Google Cloud Console.
Navigate to BigQuery.
Check if the data is successfully uploaded to the specified dataset and table.

### Troubleshooting
If there are permission errors, ensure your Google Cloud service account has BigQuery Data Editor and Storage Admin roles.
Check logs in Airflow UI if the DAG fails.

### Scope of Imporvement
Although this Data is Synthetically generated we can still handle null values in efficient ways,like using mean,median and mode(for categorical values such as productname) to populate data.But leaving at as a scope of improvement,we can also establish cicd pipelines.


