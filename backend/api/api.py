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

@app.get("/carousel/list")
async def get_carousel():
    new_carousel = CarouselServicer()
    res = new_carousel.get_carousel()
    return {"message":res}