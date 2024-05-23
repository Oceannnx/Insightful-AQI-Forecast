<script lang="ts">
	import { AxiosLib } from '$lib/axios';
	import { colorAqi } from '../utils/colorAqi';
	export let city;

	let year: number = new Date().getFullYear();
	let data: any;
	let monthTH = [
		{ monthId: 1, month: 'มกราคม' },
		{ monthId: 2, month: 'กุมภาพันธ์' },
		{ monthId: 3, month: 'มีนาคม' },
		{ monthId: 4, month: 'เมษายน' },
		{ monthId: 5, month: 'พฤษภาคม' },
		{ monthId: 6, month: 'มิถุนายน' },
		{ monthId: 7, month: 'กรกฎาคม' },
		{ monthId: 8, month: 'สิงหาคม' },
		{ monthId: 9, month: 'กันยายน' },
		{ monthId: 10, month: 'ตุลาคม' },
		{ monthId: 11, month: 'พฤศจิกายน' },
		{ monthId: 12, month: 'ธันวาคม' }
	];
	let month: number = new Date().getMonth() + 1;

	const fetchHistoryYearlyData = async () => {
		const response = await AxiosLib.get(`/history/${city.id}/${year}`);

		return response.data;
	};
	$: {
		data = fetchHistoryYearlyData();
	}
	$: if ((city, year, month)) {
		data = fetchHistoryYearlyData();
	}
</script>

<main class="flex rounded-md bg-neutral-300 drop-shadow-2xl w-3/4 p-10 flex-col">
	<div class="grid grid-cols-2">
		<div class="w-full">
			<h1 class="text-3xl">ประวัติคุณภาพอากาศ</h1>
			<h2 class="text-2xl">{city.label}</h2>
		</div>
		<div class="flex justify-end items-center gap-5 px-5">
			<select bind:value={month} class="p-2 h-fit rounded-md">
				{#each monthTH as month (month.monthId)}
					<option value={month.monthId}>{month.month}</option>
				{/each}
			</select>
			<input
				type="number"
				min="2017"
				max={new Date().getFullYear()}
				bind:value={year}
				class="h-fit p-2 border border-black rounded-md"
			/>
		</div>
	</div>
	{#await data}
		<div class="h-72 bg-slate-400 grid place-items-center">
			<div class="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-slate-300"></div>
		</div>
	{:then data}
		{#if data}
			<div class="grid grid-cols-2 gap-2 py-5">
				{#each data as item}
					<!-- svelte-ignore a11y-interactive-supports-focus -->
					{#if new Date(item.date).getMonth() + 1 === month}
						<div class="flex justify-between p-1 border rounded-sm {colorAqi(item.pm25)}">
							<p>{item.date}</p>
							<p>{item.pm25}</p>
						</div>
					{/if}
				{/each}
			</div>
		{:else}
			<p>No data</p>
		{/if}
	{:catch error}
		<p>{error.message}</p>
	{/await}
</main>

<style>
	/* Chrome, Safari, Edge, Opera */
	input::-webkit-outer-spin-button,
	input::-webkit-inner-spin-button {
		-webkit-appearance: none;
		margin: 0;
	}

	/* Firefox */
	input[type='number'] {
		-moz-appearance: textfield;
	}
</style>
