// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const formatAqiApi = (data:any) => {
    return {
    "aqi": data.aqi,
    "iaqi": {
        "co": data.iaqi.co?.v || undefined,
        "h": data.iaqi.h?.v || undefined,
        "no2": data.iaqi.no2?.v || undefined,
        "o3": data.iaqi.o3?.v || undefined,
        "p": data.iaqi.p?.v || undefined,
        "pm10": data.iaqi.pm10?.v || undefined,
        "pm25": data.iaqi.pm25?.v || undefined,
        "so2": data.iaqi.so2?.v || undefined,
        "t": data.iaqi.t?.v || undefined,
        "w": data.iaqi.w?.v || undefined,
    },
    "time": {
        "s": data.time.s || undefined,
        "tz": data.time.tz || undefined,
        "v": data.time.v || undefined,
        "iso": data.time.iso || undefined
    },
}
}