<script lang="ts">
	import { AxiosLib } from '$lib/axios';
	import { formatDate } from '../utils/formatDate';
	import { colorAqi } from '../utils/colorAqi';

	export let city;
	let data: any;
	let toggledate: boolean = false;

	let startDate: any = '2024-04-10';
	let endDate: any = '2024-04-20';

	const fetchPredictRangeData = async () => {
		const response = await AxiosLib.get(`/predict/range/${city.id}/${startDate}/${endDate}`);
		toggledate = !toggledate;
		return response.data;
	};
	$: if (toggledate) {
		data = fetchPredictRangeData();
	}
	$: if (city) {
		data = fetchPredictRangeData();
	}
</script>

<main class="flex rounded-md bg-neutral-300 drop-shadow-2xl w-3/4 h-fit p-10 flex-col">
	<div class="text-3xl">เลือกช่วงเวลาพยากรณ์</div>
	<div class="flex justify-end gap-5">
		<input class="p-2 rounded-md" type="date" bind:value={startDate} />
		<input class="p-2 rounded-md" type="date" bind:value={endDate} />
		<input
			class="p-2 px-5 border rounded-md"
			type="button"
			value="ทำนาย"
			on:click={fetchPredictRangeData}
		/>
	</div>
	<div class="grid grid-cols-3 py-5">
		<p>วันที่</p>
		<p class="grid place-content-center">ค่าเฉลี่ย AQI</p>
		<div class="grid grid-cols-2">
			<p class="grid place-content-center">ค่าต่ำสุด</p>
			<p class="grid place-content-center">ค่าสูงสุด</p>
		</div>
	</div>
	<div>
		{#await data}
			<div class="h-72 bg-slate-400 grid place-items-center">
				<div
					class="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-slate-300"
				></div>
			</div>
		{:then data}
			{#if data}
				<div class="h-fit max-h-72 overflow-y-auto flex flex-col gap-2">
					{#each data as item}
						<div class="grid grid-cols-3 p-2 rounded-md {colorAqi(item.yhat)}">
							<p>{formatDate(item.ds)}</p>
							<p class="grid place-content-center">{Math.ceil(item.yhat)}</p>
							<div class="grid grid-cols-2">
								<p class="grid place-content-center">{Math.ceil(item.yhat_lower)}</p>
								<p class="grid place-content-center">{Math.ceil(item.yhat_upper)}</p>
							</div>
						</div>
					{/each}
				</div>
			{:else}
				<p>No data</p>
			{/if}
		{:catch error}
			<p>{error.message}</p>
		{/await}
	</div>
</main>
