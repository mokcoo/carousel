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
setting folder: establishing connection to databse<br/>
if you want to run the project, first change the setting file's database's connection to your local database, then create a database called carousel.<br/>
use the cli:<br/>
uvicorn main:app<br/>

