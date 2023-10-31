import React, { useState } from 'react'
import { deleteSliderById } from '../utils/deleteSliderById'

export default function DeleteSlider() {
    const [sliderID, setSliderID] = useState(-1)
    // console.log(sliderID)
    function handleDelete(){
        deleteSliderById(sliderID)
    }
  return (
    <div>
        <h5>delete a slider</h5>
        <input onChange={(e)=>{
            setSliderID(e.target.value)}}>
        </input>
        <button onClick={handleDelete}>DELETE</button>
    </div>
  )
}
