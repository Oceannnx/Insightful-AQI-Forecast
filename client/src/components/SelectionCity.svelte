<script lang="ts">
	import { cities } from '../context/cities';
	export let selectCity;
	$: {
		if (selectCity) {
			selectCity.label = cities.find((city) => city.id === selectCity.id)?.label;
		}
	}
</script>

<main class="flex gap-6">
	{#each cities as city}
		<label
			class="has-[:checked]:bg-neutral-50 hover:bg-neutral-100 bg cursor-pointer border text-md p-2 px-5 rounded-md checked:bg-black"
		>
			<input
				type="radio"
				class="hidden"
				name="selectCity"
				value={city.id}
				bind:group={selectCity.id}
			/>
			{city.label}
		</label>
	{/each}
</main>
