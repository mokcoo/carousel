import React, { useState } from 'react'
import SliderList from '../component/sliderList'
import { ADDSLIDER,UPDATESLIDER,DELETESLIDER,GETSLIDER } from '../global/status'
import DeleteSlider from '../component/deleteSlider'
export default function Crud({slider}) {
  const [status,setStatus] = useState(GETSLIDER)
  return (
    <div>
      <div>crud</div>
      <button onClick={()=>setStatus(GETSLIDER)}>slider list</button>
      <button onClick={()=>setStatus(UPDATESLIDER)}>update slider</button>
      <button onClick={()=>setStatus(ADDSLIDER)}>add slider</button>
      <button onClick={()=>setStatus(DELETESLIDER)}>delete slider</button>

      {status === GETSLIDER && <SliderList slider={slider}></SliderList>}
      {status === DELETESLIDER && <DeleteSlider></DeleteSlider>}
    </div>
    
    
  )
}
