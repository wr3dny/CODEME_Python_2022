from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
app.counter = 0


class HelloResponse(BaseModel):
    msg: str

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}", response_model= HelloResponse)
async def hello_name(name: str):
    return HelloResponse(msg = f'Hello {name}')


@app.get("/counter")
async def counter():
    app.counter += 1
    return {'counter': app.counter}

class Product(BaseModel):
    name: str
    description: str | None
    price: float
    code: int | None
    tax: float | None


@app.post("/product")
async def create_product(prod: Product):
    return prod