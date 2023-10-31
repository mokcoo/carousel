
import { useEffect, useState } from 'react'
import { getSlider } from './utils/fetchSlider'
import Carousel from './component/carousel'



function App() {
  const [slider,setSlider] = useState({ message: [] })
  const [images,setImages] = useState([])
  const [sliderID,setSliderID] = useState(1)
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
  console.log(slider.message)
  // const list = slider.message.map((item) =>
  //     {
  //       item.map(data => {
  //         setImages([...images,data.backgroundImage.link])
  //     })
  //   }
  // );
  console.log(images)
  return (
    <div>
      {/* <div>{list}</div> */}
      <Carousel slider={slider} sliderID={sliderID}></Carousel>
      <p>aaa</p>
      

    </div>
  )
}


export default App;
