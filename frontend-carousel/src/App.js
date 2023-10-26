
import { useEffect, useState } from 'react'
import { getSlider } from './utils/fetchSlider'
import Carousel from './component/carousel'



function App() {
  const [slider,setSlider] = useState({ message: [] })
  
  useEffect(()=>{
    const response = async () =>{
      try{
        const data = await getSlider()
        setSlider(data)
      } catch (error) {
        console.error("Error fetching posts:", error);
     }
    }
    response()
    
  },[])
  // console.log(slider.message)
  const list = slider.message.map((item) =>
    item.data.map(dataItem => 
      // <img key={dataItem.id} src={dataItem.backgroundImage.link}></img>
      <Carousel key={dataItem.id} images={dataItem.backgroundImage} ></Carousel>
    )
  );
  return (
    <div>
      <div>{list}</div>
      <p>aaa</p>
      

    </div>
  )
}


export default App;
