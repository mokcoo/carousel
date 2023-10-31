import React from 'react'

export default function SliderList({slider}) {
    const list = slider.message.map((item)=>{
        const images = item.data.map((data)=>{
            console.log(data.backgroundImage.link);

            return(
                <div key={data.backgroundImage.id}>id: {data.backgroundImage.id} {data.backgroundImage.link}</div>
            )
            
        })
        return(
            <div>
                <p key={item.id}>Slider ID:{item.id}</p>
                <div>Images:{images}</div>
            </div>
            
        )
    })
  return (
    <div>
        <div>sliderList</div>
        <div>{list}</div>
    </div>
    
    
  )
}
