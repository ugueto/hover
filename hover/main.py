from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    company: str
    role: str
    active: bool
    first_name: str
    last_name: str
    email: str
    address: str
    services: list[int]

class Service(BaseModel):
    service_id: int
    company: str
    description: str | None
    users: list[int]


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API is up and running."}

@app.get("/users/{user_id}")
async def read_user(
    user_id: int, 
    query: Annotated[list[str] | None, Query(min_length=10, max_length=50)] = None
    ):
    results = {"user": user_id}
    if query:
        results.update({"query": query})
    return results

@app.post("/users/")
async def create_user(user: User):
    user_dict = user.model_dump()
    return user_dict

@app.get("/services/{service_id}")
async def read_service(
    service_id: int,
    query: Annotated[list[str] | None, Query(min_length=10, max_length=50)] = None
    ):
    results = {"service": service_id}
    if query:
        results.update({"query": query})
    return results

@app.post("/services/")
async def create_service(service: Service):
    service_dict = service.model_dump()
    return service_dict