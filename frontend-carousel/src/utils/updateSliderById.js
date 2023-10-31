import { updateSliderUrl } from "../config/url";

export async function updateSliderById(id,data){
    console.log(data)
    try{
        const res = await fetch(`${updateSliderUrl}${id}`,{
            method:'PUT',
            headers:{
                'Content-Type':'application/json'
            },
            body:data
        })
        if (res.ok){
            const serverRes = await res.json()
            console.log('Server:',serverRes) 
        }else{
            console.error('Failed to update data')
        }
    }catch(err){
        console.error("There's an error",err)
    }
    
}