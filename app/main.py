from typing import Optional

from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()
PORT = os.environ.get('PORT', 8000)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    uvicorn.run(app, port=PORT, host='0.0.0.0')