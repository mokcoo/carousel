# carousel
this is the ERD for the database <br/>
each table contains a primary key id<br/>
SliderData is the junction table for Slider and SliderItem which contains two foreign key targeting Slider and SliderItem<br/>
SliderItem contains a foreign key targeting the SliderImage table<br/>
![329a4eafdc159f0a7875ae7bb1c2e49](https://github.com/mokcoo/carousel/assets/69970162/fd7f5f97-80f3-4064-b30c-cc82ca93929d)

the backend's framework contains:<br/>
api folder: api for backend<br/>
form folder: inputing data's format<br/>
model folder: orm structure for the table<br/>
services folder: service function for api<br/>
setting folder: establishing connection to databse<br/><br/>
if you want to run the project, first change the setting file's database's connection to your local database, then create a database called carousel.<br/>
then use the cli:<br/>
uvicorn main:app<br/><br/>

for the details of the api, I presume that the front end will send a list of SliderItem, which contains all the information and the links. So if this json is sent from the frontend, it will create the desired entries in the four tables
```json
{
    "data":[
        {
            "title":"test15",
            "description":"my_image8",
            "buttonText":"selfImage8",
            "component":"testcomponent8",
            "link":"https://mxshop-files-mokcoo.oss-cn-beijing.aliyuncs.com/c35a0ddb3d3b6bb80f2be63ef42a260.jpg"
        },
        {
            "title":"test15",
            "description":"my_image1",
            "buttonText":"selfImage1",
            "component":"testcomponent1",
            "link":"https://mxshop-files-mokcoo.oss-cn-beijing.aliyuncs.com/c35a0ddb3d3b6bb80f2be63ef42a260.jpg"
        }
    ]
}
```
then if we want to update that those two SliderItems, we can first call the /carousel/list to check the id of this slider, then use that slider and the data which contains the updated information with this json
```json
{
    "data":[
        {
            "id":9,
            "title":"test15",
            "description":"my_image8",
            "buttonText":"selfImage8",
            "component":"testcomponent8",
            "link":"https://mxshop-files-mokcoo.oss-cn-beijing.aliyuncs.com/c35a0ddb3d3b6bb80f2be63ef42a260.jpg"
        },
        {
            "id":10,
            "title":"test15",
            "description":"my_image1",
            "buttonText":"selfImage1",
            "component":"testcomponent1",
            "link":"https://mxshop-files-mokcoo.oss-cn-beijing.aliyuncs.com/c35a0ddb3d3b6bb80f2be63ef42a260.jpg"
        }
    ]
}
