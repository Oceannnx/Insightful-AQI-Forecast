import axios from 'axios';

export const AxiosLib = axios.create({
	baseURL: import.meta.env.VITE_BACKEND_URL ?? 'https://insightful-aqi-forecast.onrender.com',
	withCredentials: true,
	headers: {
		'Content-Type': 'application/json',
	},
});
