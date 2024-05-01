import axios from 'axios';

export const AxiosLib = axios.create({
	baseURL: import.meta.env.VITE_BACKEND_URL ?? 'http://localhost:3000',
	withCredentials: true
});
