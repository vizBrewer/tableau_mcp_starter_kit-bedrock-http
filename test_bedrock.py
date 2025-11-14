from langchain_aws import ChatBedrock
import os

from dotenv import load_dotenv

load_dotenv()
AWS_REGION = os.getenv("AWS_REGION", "us-gov-west-1")
AWS_MODEL_ID = os.getenv("AWS_MODEL_ID", "anthropic.claude-3-7-sonnet-20250219-v1:0")
llm = ChatBedrock(
    model_id=AWS_MODEL_ID,
    
    region_name=AWS_REGION,
    model_kwargs={"temperature": 0.6},
)

print(llm.invoke("Say hello in one short sentence."))