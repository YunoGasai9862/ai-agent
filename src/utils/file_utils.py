from datetime import datetime

class FileUtils:
    def __init__(self):
        pass
    
    def save_to_txt(self, data: str, filename: str = "research_output.txt"):
        formatted_text = f"---Research Output---\nTimestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n{data}\n\n"
        with open(filename, "a", encoding="utf-8") as file:
            file.write(formatted_text)
            
        return f"Data Successfully Written to {filename}!"