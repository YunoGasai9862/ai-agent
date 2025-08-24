from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from src.models.response import Response
from src.parser.output_parser import (OutputParser)
import os
from langchain.agents import create_tool_calling_agent, AgentExecutor
from src.constants.agent_constants import AgentConstants
from src.tools.tools import (
    search_tool,
    wiki_tool
)

load_dotenv()

#using Chat Anthropic LLM
#os.environ[] throws an exception vs os.getenv()
llm = ChatOpenAI(model_name = os.environ['MODEL_NAME'],
                temperature= 1,
                timeout = None,
                max_retries = os.environ['MAX_RETRIES'],
                api_key = os.environ["OPEN_AI_API_KEY"])

output_parser = OutputParser(response_model=Response)
prompt = output_parser.get_default_chat_prompt_template()

tools = [search_tool, wiki_tool]

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

user_query = input("What can i help you with today, good sir? ")

raw_response = agent_executor.invoke({"query": user_query})

try:
    structured_response = output_parser.parser.parse(raw_response.get(AgentConstants.OUTPUT))
    print(structured_response)
except Exception as e:
    print(f"Exception occured while parsing the response: {e} - raw_response: {raw_response}")
