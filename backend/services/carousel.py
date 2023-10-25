from model.model import *
from setting.setting import db

class CarouselServicer():
    def create_carousel(self,carousel):
        print(carousel)

        #database transtractio
        # with db.atomic() as txn:
        #     try:
        #         slider = Slider()
        #         slider.save()
        #         for data in carousel:
        #
        #             #create a new slider image
        #             sliderimage = SliderImage()
        #             sliderimage.link = data.link
        #             sliderimage.save()
        #
        #             #create a new slideritem
        #             slideritem = SliderItem()
        #             slideritem.title = data.title
        #             slideritem.description = data.description
        #             slideritem.buttonText = data.button_text
        #             slideritem.component = data.component
        #             slideritem.backgroundImage = sliderimage
        #             slideritem.save()
        #
        #             #create the many to many relationship in the sliderdata table
        #             sliderdata = SliderData()
        #             sliderdata.slider = slider.id
        #             sliderdata.item = slideritem.id
        #             sliderdata.save()
        #
        #             return id
        #     except Exception as e:
        #         txn.rollback()
        #         return False
        slider = Slider()
        slider.save()
        for data in carousel:
            # create a new slider image
            sliderimage = SliderImage()
            sliderimage.link = data.link
            sliderimage.save()

            # create a new slideritem
            slideritem = SliderItem()
            slideritem.title = data.title
            slideritem.description = data.description
            slideritem.buttonText = data.buttonText
            slideritem.component = data.component
            slideritem.backgroundImage = sliderimage
            slideritem.save()

            # create the many to many relationship in the sliderdata table
            sliderdata = SliderData()
            sliderdata.slider = slider.id
            sliderdata.item = slideritem.id
            sliderdata.save()

        return slider.id
