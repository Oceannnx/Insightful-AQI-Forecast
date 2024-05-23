<script lang="ts">
	import { AxiosLib } from '$lib/axios';
	import { formatDate } from '../context/formatDate';
	import { colorAqi } from '../utils/colorAqi';
	import Swal from 'sweetalert2';

	export let city;
	let data: any;
	let toggledate: boolean = false;

	let startDate: any = new Date().toISOString().split('T')[0];
	let endDate: any;

	const fetchPredictRangeData = async () => {
		if (startDate > endDate) {
			Swal.fire({
				icon: 'error',
				title: 'Error',
				text: 'โปรดเลือกช่วงเวลาให้ถูกต้อง'
			});
			startDate = new Date().toISOString().split('T')[0];
			return;
		}
		const response = await AxiosLib.get(`/predict/range/${city.id}/${startDate}/${endDate}`);
		toggledate = !toggledate;
		return response.data;
	};
	$: {
		let today = new Date();
		today.setDate(new Date().getDate() + 7);
		endDate = today.toISOString().split('T')[0];
	}
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
		<input
			class="p-2 rounded-md"
			type="date"
			min={new Date().toISOString().split('T')[0]}
			bind:value={startDate}
		/>
		<input class="p-2 rounded-md" type="date" min={startDate} bind:value={endDate} />
		<input
			class="p-2 px-5 border rounded-md"
			type="button"
			value="พยากรณ์"
			on:click={fetchPredictRangeData}
		/>
	</div>
	<div class="grid grid-cols-3 py-5">
		<p class="grid place-content-center">วันที่</p>
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
				<div class="h-72 overflow-y-auto flex flex-col gap-2">
					{#each data as item}
						<div class="grid grid-cols-3 rounded-md {colorAqi(item.yhat)}">
							<p class="grid place-content-center">{formatDate(item.ds)}</p>
							<p class="grid place-content-center p-2 {colorAqi(item.yhat)}">
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
			{:else}
				<p>No data</p>
			{/if}
		{:catch error}
			<p>{error.message}</p>
		{/await}
	</div>
</main>
