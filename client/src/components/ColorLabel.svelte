<script lang="ts">
	import { colorLabel } from '../context/colorLabel';

	let color: any;
</script>

<main class="flex border w-3/4 p-10 flex-col bg-amber-600">
	<h1>ระดับของคุณภาพอากาศ และ คำอธิบายสี</h1>
	{#each colorLabel as data}
		<div class="grid grid-cols-4 p-2 border {data.color}">
			<div>{data.aqi}</div>
			<div>{data.label}</div>
			<div>{data.healthImplications}</div>
			<div>{data.cautionaryStatement}</div>
		</div>
	{/each}
</main>
