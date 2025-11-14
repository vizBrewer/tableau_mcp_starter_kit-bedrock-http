import boto3
from dotenv import load_dotenv
load_dotenv()

client = boto3.client("bedrock-runtime", region_name="us-gov-west-1")
print(client.list_models())