import React, { useState } from 'react'

export default function Carousel({images}) {
    const [index,setIndex] = useState(0)
    function nextImage(){
        setIndex(index = index>=images.length ? 0 : index+1)
    }
    function prevImage(){
        setIndex(index = index<=0 ? images.length-1 : index-1)
    }
    const imageCarousel = images.map((data)=> <img key={data.id} src={data.link}></img>)
  return (
    <div>
        {imageCarousel}
    </div>
  )
}
