pip install -U streamlit boto3 python-dotenv

despliege en EC2+docker:

docker build -t rag-streamlit .
docker run -p 8501:8501 rag-streamlit
