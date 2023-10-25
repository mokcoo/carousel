from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from form.form import *
from services.carousel import *

app = FastAPI()


@app.post("/carousel/add/")
async def create_carousel(carousel:SliderForm):
    new_carousel= CarouselServicer()
    id = new_carousel.create_carousel(carousel.data)


    return {"message":id}

@app.get("/")
async def test_carousel():
    return {"message":"hi, this is fast api"}