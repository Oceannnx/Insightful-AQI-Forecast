<script lang="ts">
	import ColorLabel from './ColorLabel.svelte';
	import HistoryYearly from './HistoryYearly.svelte';
	import PredictRange from './PredictRange.svelte';
	import SelectionCity from './SelectionCity.svelte';
	import TodayAqi from './TodayAqi.svelte';
	import WeeklyPredict from './WeeklyPredict.svelte';
	let city = { id: 'Bangkok', label: 'กรุงเทพ' };
</script>

<div class="fixed top-0 z-10 bg-neutral-300 w-full p-6">
	<SelectionCity bind:selectCity={city} />
</div>
<main class="flex flex-col items-center gap-10 py-32">
	<TodayAqi {city} />
	<WeeklyPredict {city} />
	<PredictRange {city} />
	<HistoryYearly {city} />
	<ColorLabel />
</main>
