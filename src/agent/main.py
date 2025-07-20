from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from models.response import Response
import os

load_dotenv()

#using Chat Anthropic LLM
#os.environ[] throws an exception vs os.getenv()
llm = ChatOpenAI(model_name = os.environ['MODEL_NAME'],
                    temperature= 1,
                    timeout = None,
                    max_retries = os.environ['MAX_RETRIES'],
                    api_key = os.environ["OPEN_AI_API_KEY"])

