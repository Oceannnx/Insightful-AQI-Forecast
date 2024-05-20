export const labelAqiQuality = (aqi: number) => {
    if (aqi <= 50) {
        return 'ดีมาก';
    }
    if (aqi <= 100) {
        return 'ดี';
    }
    if (aqi <= 150) {
        return 'ปานกลาง';
    }
    if (aqi <= 200) {
        return 'เริ่มมีผลต่อสุขภาพ';
    }
    if (aqi <= 300) {
        return 'เริ่มอันตราย';
    }
    return 'อันตราย';
}