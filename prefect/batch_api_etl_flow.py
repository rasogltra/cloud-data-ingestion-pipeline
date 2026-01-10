import os, boto3
from prefect import flow, task
from dotenv import load_dotenv
from pathlib import Path
from datetime import date, datetime
import mock_api_generator

@task
def fetch_batch_files(p_dir: Path):
    # Return list of ingested batched files (JSON and CSV)
    files = [
        fi for fi in p_dir.iterdir() 
        if fi.is_file() and (fi.name.startswith('campaign_performance') or fi.suffix == '.csv')
        ]
    
    print(f"Found {len(files)} batch files")
    return files
    
@task
def fetch_api_data():
    # Return campaign performance data from API
    data = mock_api_generator.get_mock_api_data()
    print("Fetched API data")
    return data

@task
def upload_batch_to_s3(p_dir: Path):
    # Upload batch (CSV and JSON) files to s3
    REGION = 'us-east-1'
    
    run_ts = date.today().isoformat()
    load_dotenv("../data_generation/scripts/config.env")
    
    access_id=os.getenv("AWS_ACCESS_KEY")
    secret_key=os.getenv("AWS_SECRET_KEY")
    bucket_name=os.getenv("BUCKET_NAME")
    
    assert bucket_name is not None, "BUCKET_NAME is not set"
    assert access_id is not None, "AWS_ACCESS_KEY is not set"
    assert secret_key is not None, "AWS_SECRET_KEY is not set"
    
    s3_client = boto3.client(service_name="s3", 
                            region_name=REGION,
                            aws_access_key_id=access_id,
                            aws_secret_access_key=secret_key)

    for file in p_dir.iterdir():
        if file.is_file() and (file.name.startswith('campaign_performance') or file.suffix == '.csv'):
            s3_key = (
                f"ingest/batch-files/"
                f"dt={run_ts}"
                f"{file.name}"
            )
            
            s3_client.upload_file(
                Filename=str(file), 
                Bucket=bucket_name, 
                Key=s3_key
            )
            print(f"Loaded {file} to {bucket_name}")
        else:
            print(f"No files loaded for {file}.")

#@task
#def load_to_redshift():
    #print("Loading data to Redshift..")
    
@flow(name="devto_etl", log_prints=True)
def etl_flow():
    p_dir = Path("../data_generation/generated_data/")
    
    assert p_dir is not None, "Invalid Path"
    
    batch_files = fetch_batch_files(p_dir)
    api_data = fetch_api_data()
    
    upload_batch_to_s3(p_dir)
    
    print("No. of Batch files:", len(batch_files))
    print("API entries:", len(api_data))
   
if __name__ == "__main__":
    etl_flow()