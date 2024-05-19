<script lang="ts">
	import { AxiosLib } from '$lib/axios';
	export let city: string;

	let year: number = new Date().getFullYear() - 1;
	let data: any;

	const fetchHistoryYearlyData = async () => {
		const response = await AxiosLib.get(`/history/${city}/${year}`);
		console.log(response);
		return response.data;
	};
	$: {
		data = fetchHistoryYearlyData();
	}

	$: if (city) {
		data = fetchHistoryYearlyData();
	}
</script>

<main class="flex border w-3/4 h-96 p-10 flex-col bg-amber-600">
	{#await data}
		<p>Loading...</p>
	{:then data}
		{#if data}
			<div class="grid grid-cols-12">
				{#each data as item}
					<div
						class="border border-teal-600 w-5 h-5"
						role="button"
						on:mouseover={() => console.log(item)}
						on:focus={() => console.log(item)}
					></div>
				{/each}
			</div>
		{:else}
			<p>No data</p>
		{/if}
	{:catch error}
		<p>{error.message}</p>
	{/await}
</main>
