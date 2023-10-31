import { deleteSliderUrl } from "../config/url";

export async function deleteSliderById(id){
    try{
        const res = await fetch(`${deleteSliderUrl}${id}`,{method:'DELETE'})
        if(res.ok){
            const response = res.json()
            console.log(response)
        }else{
            console.log("Failed to delete")
        }
    }catch(err){
        console.error("Error Occured",err)
    }
    
}