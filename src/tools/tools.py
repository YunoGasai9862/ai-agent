from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from src.utils.file_utils import FileUtils


duck_duck_go_search = DuckDuckGoSearchRun()

search_tool = Tool(
    name="duck_duck_go_search",
    func=duck_duck_go_search.run,
    description="Search the web for information"
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

save_tool = Tool(
    name="save_researched_text_to_file",
    func=FileUtils().save_to_txt,
    description="Save the researched output"
)