from pydantic import BaseModel
from typing import List, Optional
from dataclasses import field

class Response(BaseModel):
    
    class Output(BaseModel):
        topic: Optional[str] = field(default_factory=str)
        summary : Optional[str] = field(default_factory=str)
        sources: Optional[List[str]] = field(default_factory=list)
        tools_used:Optional[List[str]] = field(default_factory=list)
    
    query: Optional[str] = field(default_factory=str)
    output: Optional[Output] = field(default_factory=Output)
