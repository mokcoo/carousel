import { deleteSliderUrl } from "../config/url";

export async function deleteSliderById(id){
    await fetch(`${deleteSliderUrl}${id}`,{method:'DELETE'}).then(
        ()=>console.log('Delete Successful')
    )
}