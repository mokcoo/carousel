import { addSliderUrl } from "../config/url";

export async function addNewSlider(data){
    //console.log(data)
    try{
        const res = await fetch(`${addSliderUrl}`,{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:data
        })
        if (res.ok){
            const serverRes = await res.json()
            console.log('Server:',serverRes) 
        }else{
            console.error('Failed to submit data')
        }
    }catch(err){
        console.error("There's an error",err)
    }
    
}