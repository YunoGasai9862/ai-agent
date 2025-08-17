from dataclasses import dataclass
from typing import Final

@dataclass(frozen=True)
class AgentConstants():
    OUTPUT : Final[str] = "output"
    