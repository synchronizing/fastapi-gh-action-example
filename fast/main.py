from typing import Optional

from fastapi import FastAPI
from fastapi.routing import APIRoute

app = FastAPI(
    title="Fast",
    version=1,
    description="FastAPI example with GitHub Action to generate client code.",
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


# Modifies the operation_id OpenAPI variable for the function name.
for route in app.routes:
    if isinstance(route, APIRoute):
        route.operation_id = route.name
