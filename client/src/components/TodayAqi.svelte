<script lang="ts">
	import axios from 'axios';
	import { formatAqiApi } from '../utils/formatAqiApi';
	import { labelAqiQuality } from '../utils/labelAqiQuality';
	import { formatDate } from '../utils/formatDate';

	export let city;
	let data: any;
	let main: any;
	const fetchTodayAqi = async () => {
		try {
			const result = await axios.get(
				`https://api.waqi.info/feed/${city.id}/?token=3ad15d8e229a5120ed11e38c946922b0b9a42ac7`
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
			<h1 class="border border-amber-700 w-1/4 flex items-center justify-center text-6xl flex-col">
				{data.aqi}
				<div>{labelAqiQuality(data.aqi)}</div>
			</h1>
			<div class="px-5">
				<h2 class="text-2xl">{city.label}</h2>
				<h3>Latest update : {formatDate(data.time.s)}</h3>
				<div class="flex justify-center">
					<div class="px-4">
						<p>CO<sub>2</sub> : {data.iaqi.co} ppm</p>
						<p>NO<sub>2</sub> : {data.iaqi.no2} ppb</p>
						<p>O<sub>3</sub> : {data.iaqi.o3} ppb</p>
						<p>PM 1.0 : {data.iaqi.pm10} ไมโครกรัมต่อลูกบาศก์เมตร</p>
						<p>PM 2.5 : {data.iaqi.pm25} ไมโครกรัมต่อลูกบาศก์เมตร</p>
					</div>
					<div class="px-4">
						<p>SO<sub>2</sub> : {data.iaqi.so2} ppb</p>
						<p>Temperature : {data.iaqi.t} เซลเซียส</p>
						<p>Humidity : {data.iaqi.h} เปอร์เซ็น</p>
						<p>Wind : {data.iaqi.w} กิโลเมตรต่อชั่วโมง</p>
					</div>
				</div>
			</div>
		{:else}
			<h1>No data</h1>
		{/if}
	{:catch error}
		<h1>{error.message}</h1>
	{/await}
</main>
