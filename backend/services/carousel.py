from model.model import *
from setting.setting import db

class CarouselServicer():
    def create_carousel(self,id, title, description, button_text, component, link):
        #print(title)
        if not Slider.select().where(Slider.id == id):
            return False

        #database transtractio
        with db.atomic() as txn:
            try:
                #no specific instruction on how to design the add method, so I just append all the data into the
                #first slider to create a easy exmaple

                #create a new slider image
                sliderimage = SliderImage()
                sliderimage.link = link
                sliderimage.save()

                #create a new slideritem
                slideritem = SliderItem()
                slideritem.title = title
                slideritem.description = description
                slideritem.buttonText = button_text
                slideritem.component = component
                slideritem.backgroundImage = sliderimage
                slideritem.save()

                #create the many to many relationship in the sliderdata table
                sliderdata = SliderData()
                sliderdata.slider = id
                sliderdata.item = slideritem.id
                sliderdata.save()

                return id
            except Exception as e:
                txn.rollback()
                return False
