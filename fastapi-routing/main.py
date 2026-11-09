from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item}")
def read_items(item):
    return{"item_id": item }

@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id, item_id):
    return{
        "user_id":user_id,
        "item_id":item_id
    }

@app.get("/items")
def read_item(skip, limit):
    return {
        "skip" : skip,
        "limit" : limit
    }