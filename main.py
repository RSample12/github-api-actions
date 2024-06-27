from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# instantiate a Fact class
class Fact(BaseModel):
    id: int
    fact: str

facts = [Fact(id=1, fact='Dogs bark'), Fact(id=2, fact='Cats meow')]

# get method for all
@app.get('/fact')
async def main():
    return random.choice(facts['fact'])

# get method using id
@app.get('/fact/{id}')
async def find_id(id):
    for item in facts:
        if item.id == int(id):
            return item['fact']
    return

# post method for adding fact
@app.post('/fact/add')
async def add_todo(newFact: Fact):
    facts.append(newFact)
    return newFact

# delete method for deleting facts
@app.delete('/fact/{id}')
async def delete_todo(id):
    for item in facts:
        if item.id == int(id):
            facts.remove(item)
    return