<script lang="ts">
	import { AxiosLib } from '$lib/axios';
	import { formatDate } from '../utils/formatDate';

	export let city: string;
	let data: any;
	let toggledate: boolean = false;

	let startDate: any = '2024-04-10';
	let endDate: any = '2024-04-20';

	const fetchPredictRangeData = async () => {
		const response = await AxiosLib.get(`/predict/range/${city}/${startDate}/${endDate}`);
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

<main class="flex border w-3/4 h-96 p-10 flex-col bg-amber-600">
	<div class="flex justify-end">
		<input type="date" bind:value={startDate} />
		<input type="date" bind:value={endDate} />
		<input type="button" value="Click" on:click={fetchPredictRangeData} />
	</div>
	<div>
		{#await data}
			<p>Loading...</p>
		{:then data}
			{#if data}
				<div class="h-72 overflow-y-auto bg-red-600">
					{#each data as item}
						<div class="grid grid-cols-3">
							<p>{formatDate(item.ds)}</p>
							<p>{Math.ceil(item.yhat)}</p>
							<div class="grid grid-cols-2">
								<p>{Math.ceil(item.yhat_lower)}</p>
								<p>{Math.ceil(item.yhat_upper)}</p>
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
