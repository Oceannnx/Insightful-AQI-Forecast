<script lang="ts">
	import { cities } from '../context/cities';
	export let selectCity;
	$: {
		if (selectCity) {
			selectCity.label = cities.find((city) => city.id === selectCity.id)?.label;
		}
	}
</script>

{#each cities as city}
	<label>
		<input type="radio" name="selectCity" value={city.id} bind:group={selectCity.id} />
		{city.label}
	</label>
{/each}
