import os 
from typing import List
from dotenv import load_dotenv
from utils.weather_info import WeatherForecastTool
from langchain.tools import tool

class WeatherInfoTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENWEATHERMAP_API_KEY")
        self.weather_service = WeatherForecastTool(api_key=self.api_key)
        self.weather_tool_list = self._setup_tools()

    def _setup_tools(self) -> List[tool]:
        """Sets up the weather information tools."""
        @tool 
        def get_current_weather(city:str)->str:
            """Get current weather information for a city."""
            weather_data=self.weather_service.get_current_weather(city)
            if weather_data:
                temp = weather_data.get("main", {}).get("temp","N/A")
                desc= weather_data.get("weather", [{}])[0].get("description", "N/A")
                return f"The current temperature in {city} is {temp}°C."
            return f"could not find the weather for the {city}."

        @tool
        def get_weather_forecast(city: str) -> str:
            """Get weather forecast information for a city."""
            forecast_data = self.weather_service.get_weather_forecast(city)
            if forecast_data and "list" in forecast_data:
                forecast_summary=[]
                for i in range(len(forecast_data["list"])):
                    item = forecast_data["list"][i]
                    date= item['dt_txt'].split(' ')[0]
                    temp=item['main']['temp']
                    desc=item['weather'][0]['description']
                    forecast_summary.append(f"Date: {date}, Temp: {temp}°C, Description: {desc}")
                return f"Weather forecast for {city}:\n" + "\n".join(forecast_summary)
            return f"could not find the weather forecast for the {city}."

        return [get_current_weather, get_weather_forecast]