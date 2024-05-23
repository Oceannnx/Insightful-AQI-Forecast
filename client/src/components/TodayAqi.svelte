<script lang="ts">
	import axios from 'axios';
	import { formatAqiApi } from '../utils/formatAqiApi';
	import { labelAqiQuality } from '../utils/labelAqiQuality';
	import { formatDate } from '../utils/formatDate';
	import { colorAqi } from '../utils/colorAqi';

	export let city;
	let data: any;
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
	}
</script>

<main class="w-3/4 h-1/4">
	{#await data}
		<div class="h-72 bg-slate-400 grid place-items-center">
			<div class="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-slate-300"></div>
		</div>
	{:then data}
		{#if data}
			<div class="rounded-md bg-neutral-300 drop-shadow-2xl flex p-10 h-72">
				<h1
					class="w-1/4 flex items-center justify-center text-6xl flex-col {colorAqi(
						data.aqi
					)} rounded-md"
				>
					{data.aqi}
					<div>{labelAqiQuality(data.aqi)}</div>
				</h1>
				<div class="px-5">
					<h2 class="text-3xl">{city.label}</h2>
					<h3>
						อัพเดตล่าสุด : {formatDate(data.time.s)},
						{new Date(data.time.s).getHours()}:00 น.
					</h3>
					<div class="flex justify-center">
						<div class="px-4 flex flex-col gap-2">
							<p>CO<sub>2</sub> : {data.iaqi.co} ppm</p>
							<p>NO<sub>2</sub> : {data.iaqi.no2} ppb</p>
							<p>O<sub>3</sub> : {data.iaqi.o3} ppb</p>
							<p>PM 1.0 : {data.iaqi.pm10} ไมโครกรัมต่อลูกบาศก์เมตร</p>
							<p>PM 2.5 : {data.iaqi.pm25} ไมโครกรัมต่อลูกบาศก์เมตร</p>
						</div>
						<div class="px-4 flex flex-col gap-2">
							<p>SO<sub>2</sub> : {data.iaqi.so2} ppb</p>
							<p>Temperature : {data.iaqi.t} เซลเซียส</p>
							<p>Humidity : {data.iaqi.h} เปอร์เซ็น</p>
							<p>Wind : {data.iaqi.w} กิโลเมตรต่อชั่วโมง</p>
						</div>
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
