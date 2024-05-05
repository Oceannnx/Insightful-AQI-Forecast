export const getLocation = () => {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition((position) => {
			console.log(position.coords.latitude, position.coords.longitude);
		});
	} else {
		console.log('Geolocation is not supported by this browser.');
	}
};
