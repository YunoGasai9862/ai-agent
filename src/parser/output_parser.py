from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from models.response import Response

parser = PydanticOutputParser(pydantic_object = Response)

prompt = ChatPromptTemplate.from_template(
    
)