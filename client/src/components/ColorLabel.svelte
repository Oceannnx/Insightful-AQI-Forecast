<script lang="ts">
	import { colorLabel } from '../context/colorLabel';
</script>

<main class="flex rounded-md bg-neutral-300 drop-shadow-2xl w-3/4 p-10 flex-col">
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
