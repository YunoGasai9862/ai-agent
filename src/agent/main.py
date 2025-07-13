from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
import os

load_dotenv()

#using Chat Anthropic LLM
#os.environ[] throws an exception vs os.getenv()
llm = ChatOpenAI(model_name = os.environ['MODEL_NAME'],
                    temperature= 0,
                    timeout = None,
                    max_retries = os.environ['MAX_RETRIES'],
                    api_key = os.environ["OPEN_AI_API_KEY"])

response = llm.invoke("For how long homosexuality has existed?")
print(response)