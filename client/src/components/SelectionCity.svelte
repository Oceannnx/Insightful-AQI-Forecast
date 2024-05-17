<script lang="ts">
	import { cities } from '../context/cities';
	export let selectCity = 'Bangkok';
</script>

{#each cities as city}
	<label>
		<input type="radio" name="selectCity" value={city} bind:group={selectCity} />
		{city}
	</label>
{/each}
