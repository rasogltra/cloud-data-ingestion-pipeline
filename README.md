## cloud-data-ingestion-pipeline

## Overview
This project implements a **cloud-based data engineering pipeline** that ingests, processes, and loads data from multiple sources into **Amazon Redshift** for analytics use cases.

The pipeline is designed to be **scalable, reliable, and production-oriented**, enabling analytics teams to track **campaign ad spend, campaign performance, and user engagement** across batch, streaming, and API-driven data sources.

## Features
### Data Ingestion
- Batch ingestion of **CSV and JSON files** into **Amazon S3**
- API-based ingestion for external campaign and performance data
- Automated metadata tracking (source, ingestion event timestamp, file validation)

### Streaming
- Real-time ingestion of event data using **Amazon Kinesis Firehose**
- Streaming data delivered to S3 for downstream use

### Data Loading & Transformation
- Loads raw data from S3 into **Amazon Redshift**
- SQL-based transformations usinf **dbt** to create analytics-ready models
- Supports raw, staging and analytics layers

### Data Quality
- Run data quality checks using **AWS Glue DataBrew**
- Performs schema validation, null checks, range checks, and value constraints
- Data quality results are written to S3 and evaluated before loading into Redshift

### Orchestration
- **Prefect** orchestrates batch and stream workflows
- Handles task dependencies, retries, scheduling and monitoring

### CI/CD
- **GitHub Actions** for automated testing and pipeline validation
- Ensures consistent deployment of ingestion and transformation layers
 
## Architecture
**Prefect (Orchestration)** 
→ **Python Ingestion (Batch / API / Streaming)** 
→ **Amazon S3 (Raw Landing Zone)** 
→ **AWS Glue DataBrew (Data Quality)** 
→ **Amazon Redshift (Raw Tables)** 
→ **dbt Transformations** 
→ **Amazon Redshift (BI & Analytics)**

---

## Tech Stack
- **Python** – batch, API and streaming ingestion
- **Prefect** – workflow orchestration and scheduling
- **Amazon S3** – raw data storage
- **AWS Glue DataBrew** – data quality checks
- **Amazon Kinesis Firehose** – real-time streaming ingestion
- **Amazon Redshift** – cloud data warehouse
- **dbt** – SQL-based transformations
- **GitHub Actions** – CI/CD 
