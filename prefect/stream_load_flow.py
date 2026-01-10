from prefect import flow, task

@task
def load_to_redshift():
    print("Loading data to Redshift..")
    
    
@flow(name="devto_etl", log_prints=True)
def etl_flow():


if __name__ == "__main__":
    etl_flow()