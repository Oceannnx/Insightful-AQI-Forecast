import axios from 'axios';
export const axioslib = axios.create({
	baseURL: process.env.REACT_APP_API_URL || 'http://localhost:3001',
	withCredentials: true
});
