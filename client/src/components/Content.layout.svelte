<script lang="ts">
	import ColorLabel from './ColorLabel.svelte';
	import HistoryYearly from './HistoryYearly.svelte';
	import PredictRange from './PredictRange.svelte';
	import SelectionCity from './SelectionCity.svelte';
	import TodayAqi from './TodayAqi.svelte';
	import WeeklyPredict from './WeeklyPredict.svelte';
	let city = { id: 'Bangkok', label: 'กรุงเทพ' };
</script>

<SelectionCity bind:selectCity={city} />
<div class="flex flex-col items-center gap-10">
	<TodayAqi {city} />
	<WeeklyPredict {city} />
	<PredictRange {city} />
	<HistoryYearly {city} />
	<ColorLabel />
</div>
