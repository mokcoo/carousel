from model.model import *
from setting.setting import db


class CarouselServicer():
    #service for deleting logic
    def delete_carousel(self, id):

        #first check whether the slider is in the table, if not return false
        slider = Slider.get_or_none(Slider.id == id)
        if not slider:
            return False
        #using transcations for data atomic
        with db.atomic() as txn:
            try:
                #loop through all the relational tables and deleting all the entreis that is related to the inputing id
                datas = SliderData.select().where(SliderData.slider == id)
                for data in datas:
                    data.delete_instance()
                    item = SliderItem.get_or_none(SliderItem.id == data.id)
                    if item:
                        image_id = item.backgroundImage_id
                        item.delete_instance()

                        image = SliderImage.get_or_none(SliderImage.id == image_id)
                        if image:
                            image.delete_instance()
                slider.delete_instance()
                return True
            except Exception as e:
                txn.rollback()
                print(f"Error: {e}")
                return False

#service for teh listing api
    def get_carousel(self):

        slider_list = [] # storing the response

        # loop through all the sliders
        sliders = Slider.select()
        for slider in sliders:
            res = self.find_entry(slider.id) # calling the help function to format the response
            slider_list.append(res) # store each slider's information in the list

        return slider_list

# help function for get_carousel and update_carousel
    def find_entry(self,slider_id):
        data = [] # the list which stores each slider item corresponding to the slider_id
        slider_item_list = SliderItem.select().join(SliderData).join(Slider).where(Slider.id == slider_id)
        for sliderItem in slider_item_list:
            slider_image_res = {} # dict for storing the slider_image's information
            slider_image = list(SliderImage.select().where(SliderImage.id == sliderItem.id))
            if slider_image:
                slider_image_res["id"] = slider_image[0].id
                slider_image_res["link"] = slider_image[0].link

            # storing the image's information and item's information
            slider_item_res = {"id": sliderItem.id, "title": sliderItem.title,
                               "description": sliderItem.description, "component": sliderItem.component,
                               "backgroundImage": slider_image_res}

            data.append(slider_item_res)
        res = {"id": slider_id, "data": data}
        return res


    def create_carousel(self, carousel):
        # print(carousel)
        # using transactions
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
                print(f"Error: {e}")
                return False

    def update_carousel(self, id, data):
        # check whether the slider is in the table, otherwise return false
        slider_instance = Slider.get_or_none(Slider.id == id)
        if not slider_instance:
            return False
        with db.atomic() as txn:
            try:
                items = SliderItem.select().join(SliderData).join(Slider).where(Slider.id == id)
                # loop through each item, and update the desired the item
                for slider_item in items:
                    for entry in data:
                        if slider_item.id == entry.id:
                            slider_image = SliderImage().get(SliderImage.id == slider_item.id)
                            slider_image.link = entry.link
                            slider_image.save()

                            slider_item.title = entry.title
                            slider_item.description = entry.description
                            slider_item.buttonText = entry.buttonText
                            slider_item.component = entry.component
                            slider_item.backgroundImage = slider_image
                            slider_item.save()
                return self.find_entry(id) # calling find_entry to return the updated information

            except Exception as e:
                txn.rollback()
                print(f"Error: {e}")
                return False
