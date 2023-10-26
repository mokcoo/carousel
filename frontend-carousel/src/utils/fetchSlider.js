import { getSliderUrl,addSliderUrl,deleteSliderUrl,updateSliderUrl} from '../config/url'

export async function getSlider(){
    try{
        const response = await fetch(getSliderUrl)
        if (!response.ok){
            throw new Error('fetch failed')
        }
        return await response.json()
    }catch (err){
        console.error(`Failed fetching ${getSliderUrl}`,err)
        throw err
    }
}
