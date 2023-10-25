from pydantic import BaseModel
from typing import List


class SliderItemForm(BaseModel):
    id:int
    title: str
    description: str
    buttonText: str
    component: str
    link: str
