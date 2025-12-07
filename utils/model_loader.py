from pydantic import BaseModel, Field
import os
from langchain_groq import ChatGroq
# from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
# from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from utils.config_loader import load_config
from typing import Optional, Any, Literal
load_dotenv()
class ConfigLoader:
    def __init__(self):
        self.config = load_config()
        print(f"Loaded Config: {self.config}")
    def __getitem__(self, key):
        return self.config[key]

class ModelLoader(BaseModel):
    model_provider: Literal["groq","openai","ollama","gemini"]="groq"
    config: Optional[ConfigLoader]=Field(default=None,exclude=True)

    def model_post_init(self,__context:Any)->None:
        self.config = ConfigLoader()
    
    class Config:
        arbitrary_types_allowed = True
    
    def load_llm(self):
        """
        Load and return llm models
        """
        print("LLM Loading...")
        print(f"Model Provider: {self.model_provider}")
        if self.model_provider == "groq":
            print("Loading Groq model...")
            api_key=os.getenv("GROQ_API_KEY")
            model_name=self.config["llm"]["groq"]["model_name"]
            llm=ChatGroq(api_key=api_key, model_name=model_name)
            print(llm)
        elif self.model_provider == "openai":
            print("Loading OpenAI model...")
            api_key=os.getenv("OPENAI_API_KEY")
            model_name=self.config["llm"]["openai"]["model_name"]
            llm=ChatOpenAI(api_key=api_key, model_name=model_name)
        # elif self.model_provider == "ollama":
        #     print("Loading Ollama model...")
        #     model_name=self.config["llm"]["ollama"]["model_name"]
            # llm=ChatOllama(api_key=api_key, model_name=model_name)
        # elif self.model_provider == "gemini":
        #     print("Loading Gemini model...")
        #     api_key=os.getenv("GOOGLE_API_KEY")
        #     model_name=self.config["llm"]["gemini"]["model_name"]
        #     llm=ChatGoogleGenerativeAI(api_key=api_key, model_name=model_name)
        else:
            print("Unknown model provider.")

        return llm