from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from form.form import *
from services.carousel import *

app = FastAPI()


@app.post("/carousel/add")
async def create_carousel(carousel: SliderForm):
    # create a carousel servicer instance
    new_carousel = CarouselServicer()

    # retrieve the id
    id = new_carousel.create_carousel(carousel.data)

    return {"message": id}


@app.get("/carousel/list")
async def get_carousel():
    # create a carousel servicer instance
    new_carousel = CarouselServicer()
    # create all the slider information
    res = new_carousel.get_carousel()
    return {"message": res}


@app.delete("/carousel/delete/{id}")
async def delete_carousel(id):
    # create a carousel servicer instance
    new_carousel = CarouselServicer()
    # if id not in databsae return error code
    if not new_carousel.delete_carousel(id):
        raise HTTPException(status_code=404, detail="item not found")
    return {"message": "delete success"}


@app.put("/carousel/update/{id}")
async def update_carousel(id, carousel: SliderForm):
    # create a carouselservicer instance
    new_carousel = CarouselServicer()
    res = new_carousel.update_carousel(id, carousel.data)
    # if id not in database return error code
    if not res:
        raise HTTPException(status_code=404, detail="item not found")
    return res
