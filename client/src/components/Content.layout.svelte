<script lang="ts">
	import HistoryYearly from './HistoryYearly.svelte';
	import PredictRange from './PredictRange.svelte';
	import SelectionCity from './SelectionCity.svelte';
	import TodayAqi from './TodayAqi.svelte';
	import WeeklyPredict from './WeeklyPredict.svelte';
	let city: string;
</script>

<SelectionCity bind:selectCity={city} />
<div class="flex flex-col items-center gap-10">
	<TodayAqi {city} />
	<WeeklyPredict {city} />
	<PredictRange {city} />
	<HistoryYearly {city} />
</div>
