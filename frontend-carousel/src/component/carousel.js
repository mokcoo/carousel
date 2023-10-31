import React, { useEffect, useState } from 'react'

export default function Carousel({slider,sliderID}) {
    const [index,setIndex] = useState(0)
    const [images,setImages] = useState([])
    
    useEffect(()=>{
      const newSlider = slider.message.find(m =>m.id===sliderID)
      if(newSlider){
        const links = newSlider.data.map(val => val.backgroundImage.link);
        setImages(links);
      }
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
