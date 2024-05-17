<script lang="ts">
	import SelectionCity from './SelectionCity.svelte';
	import TodayAqi from './TodayAqi.svelte';
	let city: string;
</script>

<SelectionCity bind:selectCity={city} />
<div class="flex justify-center">
	<TodayAqi {city} />
</div>
