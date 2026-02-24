from configparser import ConfigParser

class Config:
    def __init__(self):
        self.config_path=r'E:\DS_GenAI\3_AgenticAI\5.AgenticAi_with_Langgraph\src\langgraphagenticai\ui\uiconfigfile.ini'
        self.config = ConfigParser()
        self.config.read(self.config_path)

    def get_llm_options(self):
        return self.config['DEFAULT'].get("LLM_OPTIONS").split(", ")

    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("MODEL_OPTIONS").split(", ")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")    