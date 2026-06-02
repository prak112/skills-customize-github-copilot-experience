from typing import Dict, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Items API - Starter")


class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=300)
    price: float = Field(..., ge=0)


store: Dict[int, Item] = {}
next_id = 1


@app.get("/items")
def list_items():
    return {i: item.dict() for i, item in store.items()}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in store:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **store[item_id].dict()}


@app.post("/items", status_code=201)
def create_item(item: Item):
    global next_id
    store[next_id] = item
    created = {"id": next_id, **item.dict()}
    next_id += 1
    return created


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in store:
        raise HTTPException(status_code=404, detail="Item not found")
    store[item_id] = item
    return {"id": item_id, **item.dict()}


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in store:
        raise HTTPException(status_code=404, detail="Item not found")
    del store[item_id]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter_app:app", host="127.0.0.1", port=8000, reload=True)
