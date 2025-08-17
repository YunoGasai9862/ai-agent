from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from typing import Any
from abc import ABC

class OutputParser(ABC) :
    
    def __init__(self, response_model: Any):
        super().__init__()
        self.parser = PydanticOutputParser(pydantic_object = response_model)
        
    def get_default_chat_prompt_template(self) -> ChatPromptTemplate:
        return ChatPromptTemplate.from_messages(
                [("system",
                    "Yuno's personal research assistance! Wrap the output in this format and provide no other text\n{format_instructions}" 
                ),
                (
                    "placeholder", "{chat_history}"
                ),
                (
                    "human", "{query}"
                ),
                (
                    "placeholder", "{agent_scratchpad}"
                )]
            ).partial(format_instructions=self.parser.get_format_instructions())
        