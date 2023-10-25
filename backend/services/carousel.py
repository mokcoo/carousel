from model.model import *
from setting.setting import db


class CarouselServicer():
    def get_carousel(self):

        slider_list = []
        sliders = Slider.select()
        for slider in sliders:
            data = []
            slider_item_list = SliderItem.select().join(SliderData).join(Slider).where(Slider.id == slider.id)
            for sliderItem in slider_item_list:
                slider_image_res = {}
                slider_image = list(SliderImage.select().where(SliderImage.id == sliderItem.id))
                if slider_image:
                    slider_image_res["id"] = slider_image[0].id
                    slider_image_res["link"] = slider_image[0].link

                slider_item_res = {"id": sliderItem.id, "title": sliderItem.title,
                                   "description": sliderItem.description, "component": sliderItem.component,
                                   "backgroundImage": slider_image_res}

                data.append(slider_item_res)
            res = {"id": slider.id, "data": data}
            slider_list.append(res)

        return slider_list

    def create_carousel(self, carousel):
        # print(carousel)
        with db.atomic() as txn:
            try:
                slider = Slider()
                slider.save()
                for data in carousel:
                    # create a new slider image
                    slider_image = SliderImage()
                    slider_image.link = data.link
                    slider_image.save()

                    # create a new slideritem
                    slider_item = SliderItem()
                    slider_item.title = data.title
                    slider_item.description = data.description
                    slider_item.buttonText = data.buttonText
                    slider_item.component = data.component
                    slider_item.backgroundImage = slider_image
                    slider_item.save()

                    # create the many to many relationship in the sliderdata table
                    slider_data = SliderData()
                    slider_data.slider = slider.id
                    slider_data.item = slider_item.id
                    slider_data.save()

                return slider.id
            except Exception as e:
                txn.rollback()
                return False
