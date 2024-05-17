<script lang="ts">
	import axios from 'axios';
	import { formatAqiApi } from '../utils/formatAqiApi';

	export let city: string;
	let data: any;
	let main: any;
	const fetchTodayAqi = async () => {
		try {
			const result = await axios.get(
				`https://api.waqi.info/feed/${city}/?token=3ad15d8e229a5120ed11e38c946922b0b9a42ac7`
			);
			return formatAqiApi(result.data.data);
		} catch (error: any) {
			console.log(error.message);
		}
	};

	$: if (city) {
		data = fetchTodayAqi();
		if (main) {
			if (data) {
				main.classList.remove('border-red-700');
				main.classList.add('border-green-700', 'bg-green-200', 'text-green-700');
			}
		}
	}
</script>

<main bind:this={main} class="flex border w-3/4 h-1/4 p-10">
	{#await data}
		<h1 class="border w-auto h-auto flex items-center justify-center">Loading...</h1>
		<h2>Loading...</h2>
		<h3>Loading...</h3>
	{:then data}
		{#if data}
			<h1 class="border border-amber-700 w-1/4 flex items-center justify-center">{data.aqi}</h1>
			<div class="px-5">
				<h2>{city}</h2>
				<h3>Latest update : {data.time.s}</h3>
				<p>CO : {data.iaqi.co}</p>
				<p>NO2 : {data.iaqi.no2}</p>
				<p>O3 : {data.iaqi.o3}</p>
				<p>PM10 : {data.iaqi.pm10}</p>
				<p>PM25 : {data.iaqi.pm25}</p>
				<p>SO2 : {data.iaqi.so2}</p>
				<p>Temperature : {data.iaqi.t}</p>
				<p>Humidity : {data.iaqi.h}</p>
				<p>Wind : {data.iaqi.w}</p>
			</div>
		{:else}
			<h1>No data</h1>
		{/if}
	{:catch error}
		<h1>{error.message}</h1>
	{/await}
</main>
