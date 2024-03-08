from fastapi import FastAPI
import time
from phi.assistant.python import PythonAssistant
from phi.file.local.csv import CsvFile

app = FastAPI()
@app.get("/process-query/")
async def process_query():
    try:
        # Hardcoded data
        start_time=time.time()
        python_assistant = PythonAssistant(
            files=[
                CsvFile(
                    path="./IMDB-Movie-Data.csv",
                    description="Contains information about movies from IMDB.",
                )
            ],
            pip_install=True,
            show_tool_calls=True,
        )
        response = python_assistant.run("What is the average rating of movies?",stream=False)
        return {"response": response,"time":time.time()-start_time}
    except Exception as e:
        print(f"An error occurred: {e}")
        # Optionally, return a more informative error response
        return {"error": str(e)}
