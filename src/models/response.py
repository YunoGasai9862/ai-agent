from pydantic import BaseModel
from typing import List, Optional
from dataclasses import field

class Response(BaseModel):
    topic: Optional[str] = field(default_factory=str)
    summary : Optional[str] = field(default_factory=str)
    sources: Optional[List[str]] = field(default_factory=list)
    tools_used:Optional[List[str]] = field(default_factory=list)
