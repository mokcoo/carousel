import React from 'react'

export default function findImageById(slider,id) {
    let images = []
    const newSlider = slider.message.find(m =>m.id===id)
    if(newSlider){
      const links = newSlider.data.map(val => images.push(val.backgroundImage.link));
    }
    return images
}
