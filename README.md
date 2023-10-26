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
this is the full view of my json after calling the /carousel/list api,the link is an image I stored the aliyun's oss
```json
{
    "message": [
        {
            "id": 1,
            "data": [
                {
                    "id": 1,
                    "title": "test8",
                    "description": "my_image8",
                    "component": "testcomponent8",
                    "backgroundImage": {
                        "id": 1,
                        "link": "https://mxshop-files-mokcoo.oss-cn-beijing.aliyuncs.com/c35a0ddb3d3b6bb80f2be63ef42a260.jpg"
                    }
                },
                {
                    "id": 2,
                    "title": "test1",
                    "description": "my_image1",
                    "component": "testcomponent1",
                    "backgroundImage": {
                        "id": 2,
                        "link": "https://mxshop-files-mokcoo.oss-cn-beijing.aliyuncs.com/c35a0ddb3d3b6bb80f2be63ef42a260.jpg"
                    }
                }
            ]
        },
        {
            "id": 3,
            "data": [
                {
                    "id": 5,
                    "title": "test10",
                    "description": "my_image8",
                    "component": "testcomponent8",
                    "backgroundImage": {
                        "id": 5,
                        "link": "https://mxshop-files-mokcoo.oss-cn-beijing.aliyuncs.com/c35a0ddb3d3b6bb80f2be63ef42a260.jpg"
                    }
                },
                {
                    "id": 6,
                    "title": "test10",
                    "description": "my_image1",
                    "component": "testcomponent1",
                    "backgroundImage": {
                        "id": 6,
                        "link": "https://mxshop-files-mokcoo.oss-cn-beijing.aliyuncs.com/c35a0ddb3d3b6bb80f2be63ef42a260.jpg"
                    }
                }
            ]
        },
        {
            "id": 4,
            "data": [
                {
                    "id": 7,
                    "title": "test11",
                    "description": "my_image8",
                    "component": "testcomponent8",
                    "backgroundImage": {
                        "id": 7,
                        "link": "https://mxshop-files-mokcoo.oss-cn-beijing.aliyuncs.com/c35a0ddb3d3b6bb80f2be63ef42a260.jpg"
                    }
                },
                {
                    "id": 8,
                    "title": "test11",
                    "description": "my_image1",
                    "component": "testcomponent1",
                    "backgroundImage": {
                        "id": 8,
                        "link": "https://mxshop-files-mokcoo.oss-cn-beijing.aliyuncs.com/c35a0ddb3d3b6bb80f2be63ef42a260.jpg"
                    }
                }
            ]
        },
        {
            "id": 5,
            "data": [
                {
                    "id": 9,
                    "title": "test15",
                    "description": "my_image8",
                    "component": "testcomponent8",
                    "backgroundImage": {
                        "id": 9,
                        "link": "https://mxshop-files-mokcoo.oss-cn-beijing.aliyuncs.com/c35a0ddb3d3b6bb80f2be63ef42a260.jpg"
                    }
                },
                {
                    "id": 10,
                    "title": "test15",
                    "description": "my_image1",
                    "component": "testcomponent1",
                    "backgroundImage": {
                        "id": 10,
                        "link": "https://mxshop-files-mokcoo.oss-cn-beijing.aliyuncs.com/c35a0ddb3d3b6bb80f2be63ef42a260.jpg"
                    }
                }
            ]
        }
    ]
}
```
for the details of the api, I presume that the front end will send a list of SliderItem, which contains all the information and the links. So if this json is sent from the frontend, it will create the desired entries in the four tables and return the id of that slider
```json
{
    "data":[
        {
            "title":"test14",
            "description":"my_image8",
            "buttonText":"selfImage8",
            "component":"testcomponent8",
            "link":"https://mxshop-files-mokcoo.oss-cn-beijing.aliyuncs.com/c35a0ddb3d3b6bb80f2be63ef42a260.jpg"
        },
        {
            "title":"test14",
            "description":"my_image1",
            "buttonText":"selfImage1",
            "component":"testcomponent1",
            "link":"https://mxshop-files-mokcoo.oss-cn-beijing.aliyuncs.com/c35a0ddb3d3b6bb80f2be63ef42a260.jpg"
        }
    ]
}
```
then if we want to update that those two SliderItems, we can first call the /carousel/list to check the id of this slider, then use that slider's id along with the data which contains the updated information with this json,if success it will return the updated json. Like below.
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
```
for the delete, we only need to provide the id of that slider and then it will go through all related fields and do the operations<br/>

Based on the interface provided by aimerce, I changed the id of slider to optional as well as the SliderItem, so it can be used when using the update logic, but for the creation ones, we only the the list of data since peewee will automatically assign the id for use. <br/>
Also, since each time when updating, deleting, and creating is called, it is associated with mutiple tables, so I used the transcations for data atomic.
