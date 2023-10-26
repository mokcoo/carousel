
import { useEffect, useState } from 'react'
import { getSlider } from './utils/fetchSlider'



function App() {
  const [slider,setSlider] = useState('')
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
  for(let i = 0;i<slider.message.length;i++){
    console.log(slider.message[i])
  }
  return (
    <div>
      {/* <div>{slider}</div> */}
      <p>aaa</p>
      

    </div>
  )
}


export default App;
