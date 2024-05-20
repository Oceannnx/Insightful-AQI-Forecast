export const colorAqi = (aqi:number) => {
    if(aqi >= 0 && aqi <= 50){
        return 'bg-emerald-500 border-emerald-600'
    } else if(aqi >= 51 && aqi <= 100){
        return 'bg-green-500 border-green-600'
    } else if(aqi >= 101 && aqi <= 150){
        return 'bg-yellow-500 border-yellow-600'
    } else if(aqi >= 150 && aqi <= 200){
        return 'bg-orange-500 border-orange-600'
    } else if(aqi >= 200 && aqi <= 300){
        return 'bg-red-500 border-red-600'
    } else if(aqi >= 300){
        return 'bg-purple-500 border-purple-600'
    }
}