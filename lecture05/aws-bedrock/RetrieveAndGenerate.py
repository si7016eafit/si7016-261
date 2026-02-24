import boto3, os

REGION = os.getenv("AWS_REGION", "us-east-1")

KB_ID = "XXX"
MODEL_ARN = "arn:aws:bedrock:us-east-1:12345678:inference-profile/global.amazon.nova-2-lite-v1:0"

client = boto3.client("bedrock-agent-runtime", region_name=REGION)

resp = client.retrieve_and_generate(
    input={"text": "Resume los puntos clave del documento sobre cafe."},
    retrieveAndGenerateConfiguration={
        "type": "KNOWLEDGE_BASE",
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": KB_ID,
            "modelArn": MODEL_ARN
        }
    }
)

print(resp["output"]["text"])

print(resp.get("citations", [])[:1])