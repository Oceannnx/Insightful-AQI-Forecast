<script lang="ts">
	import { AxiosLib } from '$lib/axios';
	import axios from 'axios';
	import { formatDate } from '../utils/FormatDate';

	export let city: string;

	let data: any;

	const fetchWeeklyPredict = async () => {
		try {
			const result = await AxiosLib.get(`/predict/weekly/${city}`);
			if (result.status === 200) {
				console.log(`${city} ${result.data}`);
				return result.data;
			}
		} catch (error: any) {
			console.log(error.message);
		}
	};
	$: {
		data = fetchWeeklyPredict();
	}

	$: if (city) {
		data = fetchWeeklyPredict();
	}
</script>

<main class="flex border w-3/4 h-1/4 p-10 flex-col">
	<div class="grid grid-cols-3">
		<p>วันที่</p>
		<p>ค่าเฉลี่ย AQI</p>
		<div class="grid grid-cols-2">
			<p>ค่าต่ำสุด</p>
			<p>ค่าสูงสุด</p>
		</div>
	</div>
	{#await data}
		<p>Loading...</p>
	{:then result}
		{#each result as item}
			<div class="grid grid-cols-3">
				<p>{formatDate(item.ds)}</p>
				<p>{Math.ceil(item.yhat)}</p>
				<div class="grid grid-cols-2">
					<p>{Math.ceil(item.yhat_lower)}</p>
					<p>{Math.ceil(item.yhat_upper)}</p>
				</div>
			</div>
		{/each}
	{:catch error}
		<p>{error.message}</p>
	{/await}
</main>
