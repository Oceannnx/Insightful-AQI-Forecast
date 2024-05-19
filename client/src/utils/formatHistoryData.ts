export const  transformJsonToMonthlyData = (data) => {
    const data: Array<DayData> = JSON.parse(jsonData);
    const transformedData: MonthlyData = {};

    data.forEach(entry => {
        const date = new Date(entry.date);
        const month = date.getMonth() + 1; // getMonth() returns 0-based index

        if (!transformedData[month]) {
            transformedData[month] = {};
        }

        const day = date.getDate();

        transformedData[month][day] = {
            day: day,
            pm25: entry.pm25,
            pm10: entry.pm10,
            o3: entry.o3,
            no2: entry.no2,
            so2: entry.so2,
            co: entry.co
        };
    });

    return transformedData;
}