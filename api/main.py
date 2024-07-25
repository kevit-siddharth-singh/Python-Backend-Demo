from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI()

# Sample JSON data
json_data = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Doe", "email": "jane@example.com"}
]

@app.get("/data", response_model=List[Dict[str, Any]])
def get_data():
    return json_data

class Item(BaseModel):
    id: int
    name: str
    email: str

@app.post("/data", response_model=List[Dict[str, Any]])
def add_data(item: Item):
    json_data.append(item.dict())
    return json_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
