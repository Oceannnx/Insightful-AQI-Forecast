<script lang="ts">
	import { AxiosLib } from '$lib/axios';
	export let city;

	let year: number = new Date().getFullYear() - 1;
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
	let month: number = 1;

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

<main class="flex border w-3/4 h-96 p-10 flex-col bg-amber-600">
	<h1 class="text-3xl text-center">Historical AQI Data</h1>
	<h2 class="text-2xl text-center">{city.label}</h2>
	<select bind:value={month}>
		{#each monthTH as month (month.monthId)}
			<option value={month.monthId}>{month.month}</option>
		{/each}
	</select>
	<input
		type="number"
		min="2017"
		max={new Date().getFullYear()}
		bind:value={year}
		class="w-1/4 p-2 border border-black"
	/>
	{#await data}
		<p>Loading...</p>
	{:then data}
		{#if data}
			<div class="flex flex-col">
				{#each data as item}
					<!-- svelte-ignore a11y-interactive-supports-focus -->
					{#if new Date(item.date).getMonth() + 1 === month}
						<div class="flex justify-between">
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
