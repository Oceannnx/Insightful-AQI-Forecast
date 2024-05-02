import { AxiosLib } from '$lib/axios';

export async function load() {
	const result = await AxiosLib.get('/predict/today/bangkok');
	return {
		data: result.data
	};
}
