from pydantic import BaseModel
from typing import List


class SliderItemForm(BaseModel):
    title: str
    description: str
    buttonText: str
    component: str
    link: str
class SliderForm(BaseModel):
    data:List[SliderItemForm]