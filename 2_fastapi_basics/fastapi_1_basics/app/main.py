from fastapi import FastAPI, Response
from pydantic import BaseModel
from typing import Optional, Union
from enum import Enum
from fastapi import FastAPI, Response
import uvicorn

app = FastAPI()

name = ""
client = dict()


class Gender(Enum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHERS = 'OTHERS'

class User(BaseModel):
    first_name: str
    last_name: Union[str, None]
    gender: Gender

@app.get("/")
def test_get():
    return client

@app.post("/")
def test_post(user: User):
    global client
    if not client:
        client = user.dict()

@app.put("/")
def test_put(user: User):
    global client
    client = user.dict()

@app.delete("/")
def test_delete():
    global client
    client = dict()
    return client

@app.patch("/")
def test_patch(user: User):
    global client
    if client:
        client = user.dict()


@app.options("/")
def test_option(response: Response):
    response.headers["Allow"] = "GET,HEAD,POST,OPTIONS,TRACE,PUT,PATCH,DELETE"
    


@app.head("/")
def test_head():
    ...


@app.trace("/")
def test_trace(response: Response):
    response.headers["TRACE"] = "HTTP/1.1"
    response.status_code = 200
    ...
    return {}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, debug=True, reload=True)






