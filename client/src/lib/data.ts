/* eslint-disable @typescript-eslint/no-explicit-any */
export const dataConvert = (dataObject: any) => {
	return {
		labels: dataObject.data.map((item: any) => item.ds),
		datasets: [
			{
				label: 'Bangkok PM2.5 Prediction',
				data: dataObject.data.map((item: any) => item.yhat),
				backgroundColor: [
					'rgba(255, 134,159,0.4)',
					'rgba(98,  182, 239,0.4)',
					'rgba(255, 218, 128,0.4)',
					'rgba(113, 205, 205,0.4)',
					'rgba(170, 128, 252,0.4)',
					'rgba(255, 177, 101,0.4)',
					'rgba(255, 177, 101,0.4)'
				],
				borderWidth: 2,
				borderColor: [
					'rgba(255, 134, 159, 1)',
					'rgba(98,  182, 239, 1)',
					'rgba(255, 218, 128, 1)',
					'rgba(113, 205, 205, 1)',
					'rgba(170, 128, 252, 1)',
					'rgba(255, 177, 101, 1)',
					'rgba(255, 177, 101, 1)'
				]
			}
		]
	};
};
