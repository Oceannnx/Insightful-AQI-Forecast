<script lang="ts">
	import { cities } from '../context/cities';
	export let selectCity;
	$: {
		if (selectCity) {
			selectCity.label = cities.find((city) => city.id === selectCity.id)?.label;
		}
	}
</script>

<main class="xl:flex gap-6 hidden">
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

<main class="xl:hidden gap-6 grid-cols-1 w-full">
	<select bind:value={selectCity.id} class="w-full p-2 rounded-md">
		{#each cities as city}
			<option value={city.id}>
				{city.label}
			</option>
		{/each}
	</select>
</main>
