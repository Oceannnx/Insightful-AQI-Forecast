<script lang="ts">
	import SelectionCity from "./SelectionCity.svelte";

    let city:string
</script>

<SelectionCity bind:selectCity={city} />
<h1>{city}</h1>