from pydantic import BaseModel
from typing import List, Optional


# the form which stores all the data that is needed for creating the slider
class SliderItemForm(BaseModel):
    id: Optional[int] = 1
    title: str
    description: str
    buttonText: str
    component: str
    link: str


class SliderForm(BaseModel):
    id: Optional[int] = 1  # an optional id for updating logic
    data: List[SliderItemForm]  # a list of sliderItemForm data
