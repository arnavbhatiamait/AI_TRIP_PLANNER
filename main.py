from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent.agentic_workflow import GraphBuilder
# from utils.save_to_document import save_document
from starlette.responses import JSONResponse
import os
import datetime
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # set specific origins in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query_travel_agent(query:QueryRequest):
    try:
        print(query)
        graph = GraphBuilder(model_provider="groq")
        react_app=graph()
        #react_app = graph.build_graph()

        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f:
            f.write(png_graph)

        print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")
        # Assuming request is a pydantic object like: {"question": "your text"}
        messages={"messages": [query.question]}
        print(messages)
        output = react_app.invoke(messages)
        print(output)
        # If result is dict with messages:
        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content  # Last AI response
        else:
            final_output = str(output)
        
        return {"answer": final_output}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from agent.agentic_workflow import GraphBuilder
# from utils.save_to_doccument import save_document
# from starlette.responses import JSONResponse
# import os
# import datetime
# from dotenv import load_dotenv
# from pydantic import BaseModel
# app = FastAPI()
# class QueryRequest(BaseModel):
#     question: str

# @app.post("/query")
# async def query(query: QueryRequest):
#     try:
#         print(query)
#         graph=GraphBuilder(model_provider="groq")
#         react_app=graph()

#         png_graph=react_app.get_graph().draw_mermaid_png()
#         with open("graph.png", "wb") as f:
#             f.write(png_graph)
#         print("Graph saved as graph.png at",os.getcwd())
#         # messages={"messages",[]}
        
#         messages={"messages": [query.question]}
#         output=react_app.invoke(messages)
#         print(output)
#         if isinstance(output, dict) and "messages" in output:
#             final_output=output["messages"][-1].content
#         else:
#             final_output=str(output)
#         return {"answer": final_output}
#     except Exception as e:
#         return JSONResponse(status_code=500,content={"error": str(e)})
