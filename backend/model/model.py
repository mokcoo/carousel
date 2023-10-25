from peewee import *
from setting.setting import db


class BaseModel(Model):
    class Meta:
        database = db


class SliderImage(BaseModel):
    link = CharField(max_length=200, default="")


class SliderItem(BaseModel):
    title = CharField(max_length=200, default="")
    description = CharField(max_length=200, default="")
    buttonText = CharField(max_length=200, default="")
    component = CharField(max_length=200, default="")
    backgroundImage = ForeignKeyField(SliderImage)


class Slider(BaseModel):
    id = PrimaryKeyField()


class SliderData(BaseModel):
    slider = ForeignKeyField(Slider)
    item = ForeignKeyField(SliderItem)


if __name__ == "__main__":
    db.connect()
    #db.drop_tables([SliderImage, SliderItem, Slider, SliderData])
    db.create_tables([SliderImage, SliderItem, Slider, SliderData])
