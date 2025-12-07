# 🌍 AI Trip Planner - Agentic Travel Planning Made Easy

<div align="center">

[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green?style=for-the-badge)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red?style=for-the-badge)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-purple?style=for-the-badge)](https://python.langchain.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Latest-orange?style=for-the-badge)](https://langchain-ai.github.io/langgraph/)

**An intelligent AI-powered travel planning assistant that creates comprehensive, personalized trip itineraries with real-time data, cost breakdowns, and detailed recommendations.**

[🚀 Quick Start](#-quick-start) • [✨ Features](#-features) • [🏗️ Architecture](#-architecture) • [🔧 Configuration](#-configuration) • [📚 API Reference](#-api-reference)

</div>

---

## 🎯 Overview

AI Trip Planner is a sophisticated agentic application that leverages cutting-edge AI models and real-time data integration to create comprehensive travel plans. It combines the power of **LangChain**, **LangGraph**, and multiple AI providers (OpenAI, Groq, Gemini, Ollama) with specialized tools for weather forecasting, place discovery, expense calculation, and currency conversion.

Whether you're planning a quick weekend getaway or a month-long adventure, this intelligent assistant will craft detailed itineraries, recommend hidden gems, calculate budgets, and provide real-time weather updates.

---

## Screen Shots
![screenshot1](https://github.com/arnavbhatiamait/AI_TRIP_PLANNER/blob/master/ScreenShots/image.png?raw=true)

![screenshot2](https://github.com/arnavbhatiamait/AI_TRIP_PLANNER/blob/master/ScreenShots/image1.png?raw=true)

---
## ✨ Features

### 🤖 Intelligent Agent Architecture

- **ReAct Pattern Implementation**: Uses LangGraph's agentic workflow with conditional routing and dynamic tool selection
- **Multi-Model Support**: Seamlessly switch between OpenAI, Groq (DeepSeek), Gemini, and Ollama
- **Adaptive Planning**: Generates both mainstream tourist routes and off-beat local recommendations

### 🌐 Real-Time Data Integration

- **Weather Forecasts**: Current conditions and multi-day forecasts using OpenWeatherMap API
- **Place Discovery**: Google Places and Tavily integration for attractions, restaurants, and activities
- **Smart Fallbacks**: Automatic fallback to alternative data sources if primary fails

### 💰 Smart Financial Tools

- **Expense Calculator**: Break down costs for accommodation, dining, activities, and transportation
- **Currency Converter**: Real-time exchange rate conversion for international trips
- **Budget Planning**: Per-day expense estimates and comprehensive cost breakdowns

### 📱 Dual Interface

- **FastAPI Backend**: Production-ready REST API with CORS support
- **Streamlit Frontend**: Interactive, user-friendly web interface with session management

### 📋 Comprehensive Itineraries

Each travel plan includes:

- ✅ Day-by-day detailed itinerary
- ✅ Accommodation recommendations with pricing
- ✅ Tourist attractions and hidden gems
- ✅ Restaurant recommendations with costs
- ✅ Available activities and experiences
- ✅ Transportation options and modes
- ✅ Weather forecasts for your trip dates
- ✅ Detailed cost breakdown by category
- ✅ Daily and total budget estimates

---

## 🏗️ Architecture

### System Design

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface Layer                      │
│  ┌──────────────────────────────────────────────────────┐  │
│  │   Streamlit Web App (streamlit_app.py)              │  │
│  │   • Interactive trip planning chat                   │  │
│  │   • Real-time response streaming                    │  │
│  │   • Formatted markdown output                       │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────┬────────────────────────────────────────────────┘
             │ HTTP/JSON
             ▼
┌─────────────────────────────────────────────────────────────┐
│                    API Layer (FastAPI)                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │   main.py - REST Endpoints                          │  │
│  │   • POST /query - Process travel queries            │  │
│  │   • CORS-enabled for cross-origin requests          │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────┬────────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│                  Agentic Workflow Layer                      │
│  ┌──────────────────────────────────────────────────────┐  │
│  │   GraphBuilder (agent/agentic_workflow.py)          │  │
│  │   • LangGraph State Machine                         │  │
│  │   • Multi-agent orchestration                       │  │
│  │   • Tool routing and execution                      │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────┬────────────────────────────────────────────────┘
             │
     ┌───────┴────────┬──────────────┬──────────────┐
     ▼                ▼              ▼              ▼
┌─────────┐      ┌─────────┐   ┌──────────┐   ┌──────────┐
│  Weather│      │  Places │   │ Expense  │   │ Currency │
│  Tools  │      │  Tools  │   │ Tools    │   │ Tools    │
└────┬────┘      └────┬────┘   └────┬─────┘   └────┬─────┘
     │                │             │              │
     ▼                ▼             ▼              ▼
┌──────────┐    ┌──────────┐  ┌──────────┐  ┌──────────┐
│OpenWeather   │Google Places │Arithmetic  │Exchange  │
│API          │Tavily Search │Operations  │APIs      │
└──────────┘    └──────────┘  └──────────┘  └──────────┘
     │                │             │              │
     └────────────────┴─────────────┴──────────────┘
                      │
                      ▼
        ┌──────────────────────────┐
        │  LLM Models (Configurable)│
        │  • OpenAI (o1-mini)      │
        │  • Groq (DeepSeek)       │
        │  • Gemini (2.5-flash)    │
        │  • Ollama (local)        │
        └──────────────────────────┘
```

### Data Flow

1. **User Input** → Streamlit UI or API request
2. **Processing** → FastAPI receives query
3. **Agent Orchestration** → LangGraph coordinates agent decision-making
4. **Tool Selection** → Agent decides which tools to call
5. **Data Collection** → Tools fetch real-time data from APIs
6. **LLM Processing** → Model synthesizes data into comprehensive plan
7. **Output Formatting** → Results formatted as markdown
8. **User Display** → Rendered in Streamlit with styling

---

## 📂 Project Structure

```
AI_TRIP_PLANNER/
├── 📄 main.py                          # FastAPI application & REST endpoints
├── 📄 streamlit_app.py                 # Streamlit UI for trip planning
├── 📄 requirements.txt                 # Python dependencies
├── 📄 setup.py                         # Package configuration
├── 📄 pyproject.toml                   # Project metadata
│
├── 📁 agent/                           # Core agentic workflow
│   ├── __init__.py
│   └── agentic_workflow.py            # LangGraph implementation
│
├── 📁 tools/                           # Specialized AI tools
│   ├── __init__.py
│   ├── weather_info_tool.py           # Weather data integration
│   ├── places_search_tool.py          # Place discovery (Google/Tavily)
│   ├── expense_calculator_tool.py     # Expense calculation
│   ├── currrency_conversion_tool.py   # Currency conversion
│   └── arthamatic_op_tool.py          # Basic arithmetic operations
│
├── 📁 utils/                           # Utility modules
│   ├── __init__.py
│   ├── model_loader.py                # LLM model initialization
│   ├── weather_info.py                # Weather API client
│   ├── place_info_search.py          # Google Places & Tavily clients
│   ├── currency_converter.py          # Exchange rate fetching
│   ├── expense_calculator.py          # Financial calculations
│   ├── config_loader.py               # Configuration management
│   └── save_to_doccument.py          # Document export utilities
│
├── 📁 config/                          # Configuration files
│   ├── __init__.py
│   └── config.yaml                    # Model & API configurations
│
├── 📁 prompt_library/                 # AI prompts
│   ├── __init__.py
│   └── prompt.py                      # System prompts for the agent
│
├── 📁 exception/                       # Error handling
│   ├── __init__.py
│   └── exceptionhandling.py           # Custom exceptions
│
├── 📁 logger/                          # Logging configuration
│   ├── __init__.py
│   └── (logging setup)
│
└── 📁 notebook/                        # Jupyter notebooks
    ├── __init__.py
    └── experiments.ipynb              # Experimentation & prototyping
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+** installed
- **API Keys** for:
  - OpenWeatherMap (weather data)
  - Google Places API (place discovery)
  - Tavily API (fallback search)
  - LLM Provider (OpenAI, Groq, Gemini, or local Ollama)

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd AI_TRIP_PLANNER
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv trip_planner
   ```

3. **Activate the virtual environment**

   **Windows (PowerShell):**

   ```powershell
   .\trip_planner\Scripts\Activate.ps1
   ```

   **Windows (CMD):**

   ```cmd
   trip_planner\Scripts\activate.bat
   ```

   **macOS/Linux:**

   ```bash
   source trip_planner/bin/activate
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Configure API Keys**

   Create a `.env` file in the project root:

   ```env
   # LLM Configuration (choose one)
   OPENAI_API_KEY=your_openai_key_here
   GROQ_API_KEY=your_groq_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   
   # External APIs
   OPENWEATHERMAP_API_KEY=your_openweathermap_key
   GPLACES_API_KEY=your_google_places_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

### Running the Application

#### Option 1: Streamlit Web Interface (Recommended for Users)

```bash
streamlit run streamlit_app.py
```

Then open your browser and navigate to `http://localhost:8501`

#### Option 2: FastAPI Backend with Streamlit Frontend

**Terminal 1 - Start the API server:**

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Start the Streamlit app:**

```bash
streamlit run streamlit_app.py
```

#### Option 3: FastAPI Only (For Integration/Testing)

```bash
uvicorn main:app --reload
```

Access the API at `http://localhost:8000`

- API Documentation: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`

---

## 🔧 Configuration

### Model Provider Selection

Edit `config/config.yaml` to change the LLM provider:

```yaml
llm:
  openai:
    provider: "openai"
    model_name: "o1-mini"      # GPT-4 level performance
    
  groq:
    provider: "groq"
    model_name: "deepseek-r1-distill-llama-70b"  # Fast inference
    
  gemini:
    provider: "gemini"
    model_name: "gemini-2.5-flash"  # Latest Gemini
    
  ollama:
    provider: "ollama"
    model_name: "llama3-groq-tool-use:latest"    # Local execution
```

### Environment Variables Reference

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key | If using OpenAI |
| `GROQ_API_KEY` | Groq API key | If using Groq |
| `GOOGLE_API_KEY` | Google Gemini API key | If using Gemini |
| `OPENWEATHERMAP_API_KEY` | Weather data API key | Yes |
| `GPLACES_API_KEY` | Google Places API key | Yes |
| `TAVILY_API_KEY` | Tavily search API key | Yes |

---

## 📡 API Reference

### REST Endpoints

#### `POST /query`

Send a travel planning query to the AI agent.

**Request Body:**

```json
{
  "question": "Plan a 5-day trip to Goa with a budget of $1500"
}
```

**Response:**

```json
{
  "answer": "# 🌍 Your Personalized Goa Travel Plan\n\n## Day 1: Arrival & Relaxation\n..."
}
```

**Example with cURL:**

```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"question": "Plan a trip to Bali for 7 days"}'
```

**Example with Python:**

```python
import requests

url = "http://localhost:8000/query"
payload = {"question": "Plan a trip to Tokyo for 4 days"}
response = requests.post(url, json=payload)
print(response.json()["answer"])
```

---

## 🛠️ Tools & Integrations

### Weather Information Tool

Fetches current weather and forecasts using OpenWeatherMap API.

**Capabilities:**

- Current temperature and conditions
- Multi-day weather forecasts
- Real-time weather updates

### Places Search Tool

Discovers attractions, restaurants, and activities using Google Places and Tavily.

**Capabilities:**

- Tourist attractions discovery
- Restaurant recommendations
- Activity suggestions
- Fallback search (Google → Tavily)

### Expense Calculator Tool

Performs calculations for budget planning.

**Capabilities:**

- Cost aggregation
- Per-day budget breakdown
- Multi-currency calculations
- Expense categorization

### Currency Converter Tool

Real-time currency conversion for international trips.

**Capabilities:**

- Multi-currency support
- Live exchange rates
- Budget estimation in local currency

---

## 🔄 Workflow Execution

### How the Agent Works

```
1. User Input (Question)
   ↓
2. LangGraph Agent Receives Input
   ↓
3. Agent Analyzes Query
   ├─ Extract destination
   ├─ Extract duration
   ├─ Extract budget
   └─ Extract preferences
   ↓
4. Tool Selection & Execution
   ├─ Weather Tool → Get forecast
   ├─ Places Tool → Find attractions
   ├─ Expense Tool → Calculate costs
   └─ Currency Tool → Convert pricing
   ↓
5. Data Synthesis
   └─ LLM synthesizes all data
   ↓
6. Itinerary Generation
   ├─ Create day-by-day plan
   ├─ Format recommendations
   ├─ Calculate totals
   └─ Add helpful tips
   ↓
7. Output Formatting
   └─ Generate Markdown response
   ↓
8. User Display
   └─ Render in Streamlit/API
```

### System Prompt

The agent operates under a detailed system prompt that ensures:

- Comprehensive travel planning
- Dual itineraries (tourist + off-beat)
- Real-time data integration
- Complete cost breakdowns
- Professional formatting

---

## 🎨 User Interface

### Streamlit Features

- 🎯 **Clean Interface**: Intuitive chat-like interaction
- ⚡ **Real-time Responses**: Streaming outputs with loading spinners
- 📱 **Responsive Design**: Works on desktop and mobile
- 💾 **Session Management**: Maintains chat history
- 🎨 **Markdown Rendering**: Beautiful formatted travel plans
- 🌍 **Emoji Support**: Engaging visual indicators

### Sample Query Examples

1. "Plan a romantic weekend trip to Paris with a budget of 2000 EUR"
2. "5-day adventure tour in New Zealand for 2 people, budget $3000"
3. "Budget backpacking trip to Southeast Asia for 2 weeks under $2000"
4. "Luxury vacation in Maldives for 10 days with no budget constraint"
5. "Family trip to Disney World for 4 days with kids aged 5 and 8"

---

## 🧪 Development & Testing

### Running Experiments

```bash
jupyter notebook notebook/experiments.ipynb
```

### Testing the Agent

```python
from agent.agentic_workflow import GraphBuilder

# Initialize the graph builder
graph = GraphBuilder(model_provider="groq")
react_app = graph()

# Test a query
messages = {"messages": ["Plan a 3-day trip to Rome"]}
output = react_app.invoke(messages)
print(output["messages"][-1].content)
```

---

## 🐛 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **API Key errors** | Verify all keys in `.env` file and API quotas |
| **Port 8000 in use** | Use different port: `uvicorn main:app --port 8001` |
| **Weather API failures** | Check OpenWeatherMap API status and rate limits |
| **Places not found** | Verify Google Places API is enabled for your key |
| **Slow responses** | Consider using Groq (faster) over OpenAI |
| **CORS errors** | API CORS is already configured for all origins |

### Enable Debug Mode

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## 📊 Performance & Optimization

### Response Time Optimization

| Provider | Speed | Cost | Quality |
|----------|-------|------|---------|
| **Groq** | ⚡⚡⚡ Fast | 💰 Cheap | ✨ Good |
| **Gemini** | ⚡⚡ Medium | 💰 Moderate | ✨✨ Very Good |
| **OpenAI** | ⚡ Slower | 💰💰💰 Expensive | ✨✨✨ Excellent |
| **Ollama** | ⚡ Slower | 💰 Free | ✨ Good |

### Recommended Configuration

For **production**: Use Groq for speed and cost efficiency
For **quality**: Use OpenAI or Gemini
For **local**: Use Ollama for privacy

---

## 📜 Project Metadata

- **Project Name**: AI Trip Planner
- **Version**: 0.0.1
- **Author**: Arnav Bhatia
- **Email**: <arnavbhatiamait@gmail.com>
- **Python Version**: 3.11+
- **License**: MIT (recommended)

---

## 🤝 Contributing

Contributions are welcome! Areas for enhancement:

- [ ] Support for more hotel booking integrations
- [ ] Flight search and booking
- [ ] Travel insurance recommendations
- [ ] Visa requirement checker
- [ ] Carbon footprint calculator
- [ ] Social travel planning (group trips)
- [ ] Mobile app version
- [ ] Multi-language support
- [ ] Database for saved itineraries

---

## 📚 Dependencies

- **LangChain**: LLM framework and tools
- **LangGraph**: Agent orchestration and workflow management
- **FastAPI**: REST API framework
- **Streamlit**: Web UI framework
- **Pydantic**: Data validation
- **Python-dotenv**: Environment variable management
- **Requests/httpx**: HTTP client libraries
- **LangChain Integrations**:
  - `langchain-groq`: Groq LLM provider
  - `langchain-openai`: OpenAI integration
  - `langchain_google_community`: Google APIs
  - `langchain-tavily`: Web search integration

---

## 🚦 Getting Help

- 📖 Check the [troubleshooting section](#-troubleshooting)
- 🔗 Review API documentation at `/docs` when running FastAPI
- 📝 Check `notebook/experiments.ipynb` for usage examples
- 🐛 Report issues with detailed error messages and logs

---

## 🎉 What's Next?

1. **Set up your API keys** in `.env`
2. **Run the application** using Streamlit
3. **Ask the agent** to plan your dream trip
4. **Export and share** your itinerary
5. **Customize the prompts** for your use case

---

<div align="center">

### Made with ❤️ for Travel Enthusiasts & AI Builders

**Happy Trip Planning! 🌴✈️🗺️**

---

*Last Updated: December 2025*

</div>
