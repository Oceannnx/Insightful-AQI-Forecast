<script lang="ts">
	import { AxiosLib } from '$lib/axios';
	import { colorAqi } from '../utils/colorAqi';
	import { formatDate } from '../utils/formatDate';

	export let city;

	let data: any;

	const fetchWeeklyPredict = async () => {
		try {
			const result = await AxiosLib.get(`/predict/weekly/${city.id}`);
			if (result.status === 200) {
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

<main
	class="flex rounded-md xl:w-3/4 h-1/4 w-full md:w-4/5 flex-col bg-neutral-300 drop-shadow-2xl"
>
	<div class="xl:text-3xl px-10 pt-5 text-xl">พยากรณ์คุณภาพอากาศ 1 อาทิตย์</div>
	<div class="py-5 px-10 pb-10">
		<div class="grid grid-cols-3 pb-5">
			<p class="grid place-content-center text-sm text-center xl:text-lg">วันที่</p>
			<p class="grid place-content-center text-sm text-center xl:text-lg">ค่าเฉลี่ย AQI</p>
			<div class="grid grid-cols-2">
				<p class="grid place-content-center text-sm text-center xl:text-lg">ค่าต่ำสุด</p>
				<p class="grid place-content-center text-sm text-center xl:text-lg">ค่าสูงสุด</p>
			</div>
		</div>
		{#await data}
			<div class="h-72 bg-slate-400 grid place-items-center">
				<div
					class="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-slate-300"
				></div>
			</div>
		{:then result}
			<div class="flex flex-col gap-2">
				{#each result as item}
					<div class="grid grid-cols-3 rounded-md {colorAqi(item.yhat)}">
						<p class="grid place-content-center text-sm text-center xl:text-lg">
							{formatDate(item.ds)}
						</p>
						<p
							class="grid place-content-center p-2 text-sm text-center xl:text-lg {colorAqi(
								item.yhat
							)}"
						>
							{Math.ceil(item.yhat)}
						</p>
						<div class="grid grid-cols-2">
							<p class="grid place-content-center {colorAqi(item.yhat_lower)}">
								{Math.ceil(item.yhat_lower)}
							</p>
							<p class="grid place-content-center {colorAqi(item.yhat_upper)}">
								{Math.ceil(item.yhat_upper)}
							</p>
						</div>
					</div>
				{/each}
			</div>
		{:catch error}
			<p>{error.message}</p>
		{/await}
	</div>
</main>
