from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from form.form import *
from services.carousel import *

app = FastAPI()


@app.post("/carousel/add/")
async def create_carousel(carousel:SliderItemForm):
    print(carousel)
    new_carousel= CarouselServicer()
    if not new_carousel.create_carousel(carousel.id,
                                 carousel.title,
                                 carousel.description,
                                 carousel.buttonText,
                                 carousel.component,
                                 carousel.link):
        raise HTTPException(status_code=404,detail="item id not exist")
    return new_carousel

@app.get("/")
async def test_carousel():
    return {"message":"hi, this is fast api"}