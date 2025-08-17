from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

duck_duck_go_search = DuckDuckGoSearchRun()

search_tool = Tool(
    name="duck_duck_go_search",
    func=duck_duck_go_search.run,
    description="Search the web for information"
)
