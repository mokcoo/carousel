import React, { useEffect, useState } from 'react'
import findImageById from '../utils/findImageById'

export default function Carousel({slider,sliderID}) {
    const [index,setIndex] = useState(0)
    const [images,setImages] = useState([])
    
    useEffect(()=>{
      const link = findImageById(slider,sliderID)
      setImages(link);
      
    },[slider, sliderID])
    
    function nextImage() {
      const newindex = index >= images.length - 1 ? 0 : index + 1;
      setIndex(newindex);
  }

  function prevImage() {
      const newindex = index <= 0 ? images.length - 1 : index - 1;
      setIndex(newindex);
  }
  return (
    <div>
        <img src={images[index]}></img>
        <button onClick={nextImage}>nextImage</button>
        <button onClick={prevImage}>prevImage</button>
    </div>
    
  )
}
