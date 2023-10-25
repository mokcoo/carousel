from peewee import *
from setting.setting import db


class BaseModel(Model):
    class Meta:
        database = db


# image table
class SliderImage(BaseModel):
    link = CharField(max_length=200, default="")


# SliderItem table
class SliderItem(BaseModel):
    title = CharField(max_length=200, default="")
    description = CharField(max_length=200, default="")
    buttonText = CharField(max_length=200, default="")
    component = CharField(max_length=200, default="")
    backgroundImage = ForeignKeyField(SliderImage)


# slider table
class Slider(BaseModel):
    id = PrimaryKeyField()


# a junction table for achieving many-to-many relationships
# which enables using one id of slider to find multiple entry of sliderItem
class SliderData(BaseModel):
    slider = ForeignKeyField(Slider)
    item = ForeignKeyField(SliderItem)


if __name__ == "__main__":
    db.connect()
    # db.drop_tables([SliderImage, SliderItem, Slider, SliderData])
    db.create_tables([SliderImage, SliderItem, Slider, SliderData])
