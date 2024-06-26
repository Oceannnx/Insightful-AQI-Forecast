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

export const contextAqi = (aqi: number) => {
    if (aqi <= 50) {
        return {
            label: 'ดีมาก',
            context:'คุณภาพอากาศดีมาก คุณภาพอากาศถือว่าพึงพอใจและมีความเสี่ยงต่ำหรือไม่มีความเสี่ยงต่อสุขภาพ',
        };
    }
    if (aqi <= 100) {
        return {
            label: 'ดี',
            context:'คุณภาพอากาศดี สำหรับมลพิษบางชนิดอาจมีความกังวลเรื่องสุขภาพ ในระดับปานกลางสำหรับคนจำนวนน้อยมากที่ไวต่อมลพิษทางอากาศอย่างผิดปกติ',
        };
    }
    if (aqi <= 150) {
        return {
            label: 'ปานกลาง',
            context:'สมาชิกของกลุ่มที่อ่อนไหวอาจมีผลกระทบต่อสุขภาพ แต่ประชาชนทั่วไปไม่ค่อยมีผลกระทบ',
        };
    }
    if (aqi <= 200) {
        return {
            label: 'เริ่มมีผลต่อสุขภาพ',
            context:'ทุกคนอาจเริ่มรู้สึกไม่สบาย ผู้ที่เป็นสมาชิกของกลุ่มที่อ่อนไหวอาจมีผลกระทบต่อสุขภาพรุนแรงมากขึ้น',
        };
    }
    if (aqi <= 300) {
        return {
            label: 'เริ่มอันตราย',
            context:'มีผลกระทบต่อสุขภาพสำหรับทุกคน สมาชิกของกลุ่มที่อ่อนไหวอาจมีผลกระทบต่อสุขภาพรุนแรงมากขึ้น',
        };
    }
    return {
        label: 'อันตราย',
        context:'ทุกคนอาจมีผลกระทบต่อสุขภาพอย่างรุนแรง สถานการณ์ฉุกเฉินสำหรับสุขภาพทั้งประชากรทั่วไปและกลุ่มที่อ่อนไหว',
    };
}