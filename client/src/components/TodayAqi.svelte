<script lang="ts">
	import axios from 'axios';
	import { formatAqiApi } from '../utils/formatAqiApi';
	import { contextAqi, labelAqiQuality } from '../utils/labelAqiQuality';
	import { colorAqi } from '../utils/colorAqi';
	import { formatDate } from '../utils/formatDate';
	import info from '../asset/info.svg';
	import { colorLabel } from '../context/colorLabel';

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

<main class="xl:w-3/4 h-1/4 w-full md:w-4/5">
	{#await data}
		<div class="h-72 bg-slate-400 grid place-items-center">
			<div class="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-slate-300"></div>
		</div>
	{:then data}
		{#if data}
			<div class="rounded-md bg-neutral-300 drop-shadow-2xl xl:flex p-10 h-fit xl:h-72 gap-10">
				<h1
					class="xl:w-1/4 w-full flex items-center justify-center xl:text-6xl text-4xl py-10 flex-col relative {colorAqi(
						data.aqi
					)} rounded-md"
				>
					{data.aqi}
					<div>{labelAqiQuality(data.aqi)}</div>
					<div class="group">
						<img src={info} alt="info" class="w-5 h-5 z-10 absolute top-2 right-2" />
						<div
							class="xl:text-sm text-xs z-10 absolute bg-neutral-200 lg:-right-72 -right-2 lg:top-0 p-5 rounded-md shadow-md hidden group-hover:block group-active:block w-full text-left"
						>
							<div class="pb-2">{labelAqiQuality(data.aqi)} {contextAqi(data.aqi).context}</div>
							{#each colorLabel as item}
								<div class="flex justify-items-center p-1">
									<div class="w-5 h-5 rounded-full inline-block {item.color}"></div>
									<div class="inline-block pl-2">{item.label}</div>
								</div>
							{/each}
						</div>
					</div>
				</h1>
				<div class="xl:px-5">
					<h2 class="xl:text-3xl text-2xl">AQI ของ {city.label}</h2>
					<h3>
						อัพเดตล่าสุด : {formatDate(data.time.s)},
						{new Date(data.time.s).getHours()}:00 น.
					</h3>
					<div class="xl:flex xl:justify-center grid">
						<div class="xl:px-4 flex flex-col gap-2">
							<p>
								CO<sub>2</sub> : {#if data.iaqi.co !== undefined}
									{data.iaqi.co} ppm
								{:else}
									ไม่มีข้อมูล
								{/if}
							</p>
							<p>
								NO<sub>2</sub> : {#if data.iaqi.no2 !== undefined}
									{data.iaqi.no2} ppb
								{:else}
									ไม่มีข้อมูล
								{/if}
							</p>
							<p>
								O<sub>3</sub> : {#if data.iaqi.o3 !== undefined}
									{data.iaqi.o3} ppb
								{:else}
									ไม่มีข้อมูล
								{/if}
							</p>
							<p>
								PM 10 : {#if data.iaqi.pm10 !== undefined}
									{data.iaqi.pm10} ไมโครกรัมต่อลูกบาศก์เมตร
								{:else}
									ไม่มีข้อมูล
								{/if}
							</p>
							<p>
								PM 2.5 : {#if data.iaqi.pm25 !== undefined}
									{data.iaqi.pm25} ไมโครกรัมต่อลูกบาศก์เมตร
								{:else}
									ไม่มีข้อมูล
								{/if}
							</p>
						</div>
						<div class="xl:px-4 flex flex-col gap-2">
							<p>
								SO<sub>2</sub> : {#if data.iaqi.so2 !== undefined}
									{data.iaqi.so2} ppb
								{:else}
									ไม่มีข้อมูล
								{/if}
							</p>
							<p>
								อุณหภูมิ : {#if data.iaqi.t !== undefined}
									{data.iaqi.t} องศาเซลเซียส
								{:else}
									ไม่มีข้อมูล
								{/if}
							</p>
							<p>
								ความชื้น : {#if data.iaqi.h !== undefined}
									{data.iaqi.h} %
								{:else}
									ไม่มีข้อมูล
								{/if}
							</p>
							<p>
								ความเร็วลม : {#if data.iaqi.w !== undefined}
									{data.iaqi.w} m/s
								{:else}
									ไม่มีข้อมูล
								{/if}
							</p>
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
