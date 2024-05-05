import boto3
import psycopg2
from io import BytesIO

# AWS credentials and region
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY'
aws_region = 'YOUR_AWS_REGION'

# S3 bucket and object key
s3_bucket_name = 'YOUR_S3_BUCKET_NAME'
s3_object_key = 'YOUR_S3_OBJECT_KEY'

# RDS credentials and connection details
rds_host = 'YOUR_RDS_HOST'
rds_port = 'YOUR_RDS_PORT'
rds_dbname = 'YOUR_RDS_DB_NAME'
rds_user = 'YOUR_RDS_USERNAME'
rds_password = 'YOUR_RDS_PASSWORD'

# Function to read data from S3 and push it to RDS
def transfer_data_s3_to_rds():
    # Initialize S3 client
    s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                             aws_secret_access_key=aws_secret_access_key,
                             region_name=aws_region)
    
    # Initialize RDS connection
    conn = psycopg2.connect(host=rds_host, port=rds_port, dbname=rds_dbname,
                            user=rds_user, password=rds_password)
    cursor = conn.cursor()
    
    # Read data from S3
    try:
        response = s3_client.get_object(Bucket=s3_bucket_name, Key=s3_object_key)
        data = response['Body'].read().decode('utf-8')
        
        # Example assumes CSV data, you might need to parse differently based on your data format
        data_lines = data.split('\n')
        
        # Insert data into RDS
        for line in data_lines:
            # Example assumes CSV data with comma-separated values
            values = line.split(',')
            # Example assumes a table called 'your_table' in your RDS
            cursor.execute("INSERT INTO your_table (column1, column2, ...) VALUES (%s, %s, ...)", values)
        
        conn.commit()
        print("Data transferred successfully.")
    except Exception as e:
        print("Error transferring data:", str(e))
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

# Call the function to transfer data
transfer_data_s3_to_rds()
