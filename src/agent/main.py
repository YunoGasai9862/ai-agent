from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from src.models.response import Response
from src.parser.output_parser import (OutputParser)
import os
from langchain.agents import create_tool_calling_agent, AgentExecutor

load_dotenv()

#using Chat Anthropic LLM
#os.environ[] throws an exception vs os.getenv()
llm = ChatOpenAI(model_name = os.environ['MODEL_NAME'],
                    temperature= 1,
                    timeout = None,
                    max_retries = os.environ['MAX_RETRIES'],
                    api_key = os.environ["OPEN_AI_API_KEY"])

output_parser = OutputParser()
prompt = output_parser.get_default_chat_prompt_template(response_model=Response)

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=[]
)

agent_executor = AgentExecutor(agent=agent, tools = [], verbose=True)

raw_response = agent_executor.invoke({"query": "Are blackholes a portal to different universes"})
print(raw_response)