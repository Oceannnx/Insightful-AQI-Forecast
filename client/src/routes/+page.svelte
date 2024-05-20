<script lang="ts">
	import imgUrl from '../asset/bangkok_city_2.jpg';
	import Content from '../components/Content.layout.svelte';
	import Sidebar from '../components/Sidebar.svelte';
	export let data;

	const handleStarterButton = () => {
		data.visited = true;
	};
</script>

<main class="overflow-x-hidden">
	{#if !data.visited}
		<body>
			<img class="w-screen h-screen -z-10 absolute blur" src={imgUrl} alt="Bangkok City" />
			<div class="w-screen h-screen flex flex-col justify-center items-center p-10">
				<h1 class="text-7xl font-bold py-3 text-background">Insightful AQI Forecast</h1>
				<div class="py-6">
					<button
						class="text-4xl p-3 rounded-2xl bg-white bg-opacity-50 hover:bg-opacity-70"
						on:click={handleStarterButton}>เริ่มต้นใช้งาน</button
					>
				</div>
			</div>
		</body>
	{:else}
		<main class="w-screen h-auto grid grid-cols-6">
			<div class="bg-amber-700 col-span-1">
				<Sidebar />
			</div>
			<div class="col-span-5 bg-neutral-300">
				<Content />
			</div>
		</main>
	{/if}
</main>

<style>
	.text-background {
		background-image: url('../asset/bangkok_city_3.jpg');
		background-repeat: repeat;
		-webkit-background-clip: text;
		background-clip: text;
		-webkit-text-fill-color: transparent;
		text-align: center;
		font-weight: bold;
		text-transform: uppercase;
		font-family: 'Steelfish Rg', 'helvetica neue', helvetica, arial, sans-serif;
		font-weight: 800;
		-webkit-font-smoothing: antialiased;
	}
</style>
