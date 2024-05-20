<script lang="ts">
	import { getLocation } from '$lib/Geolocation';
	import imgUrl from '../asset/bangkok_city_2.jpg';
	import Content from '../components/Content.layout.svelte';
	import Sidebar from '../components/Sidebar.svelte';
	export let data;

	const handleStarterButton = () => {
		data.visited = true;
	};
	getLocation();
</script>

<main class="overflow-x-hidden">
	{#if !data.visited}
		<body>
			<img class="w-screen h-screen -z-10 absolute" src={imgUrl} alt="Bangkok City" />
			<div
				class="w-fit h-screen flex flex-col justify-center items-start p-10 bg-slate-400 opacity-80"
			>
				<h1 class="text-6xl py-3">Insightful AQI Forecast</h1>
				<div class="py-6">
					<button class="text-xl hover:" on:click={handleStarterButton}>เริ่มต้นใช้งาน</button>
				</div>
			</div>
		</body>
	{:else}
		<main class="w-screen h-screen grid grid-cols-8">
			<div class="bg-amber-700">
				<Sidebar />
			</div>
			<div class="col-span-7 bg-neutral-300">
				<Content />
			</div>
		</main>
	{/if}
</main>
