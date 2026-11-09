from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item}")
def read_items(item_id: int):
    return {
        "item_id":item_id
    }

@app.get("/getdata")
def read_items(data):
    return{"data":data}