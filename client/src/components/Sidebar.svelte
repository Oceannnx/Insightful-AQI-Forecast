<script lang="ts">
	import logo from '../asset/logo.png';
	import { pageContent } from '../context/pageContent';
	import { scroll } from '../utils/scroll';
	let scrollY = 0;
</script>

<main class="flex flex-col items-center">
	<div class="flex flex-col items-center fixed top-0">
		<img class="w-3/4" src={logo} alt="logo" />
		<div class="w-full h-fit flex flex-col items-center p-10">
			{#each pageContent as item}
				<div
					class="w-full h-20 flex justify-center items-center {scroll(
						scrollY,
						item.startScroll,
						item.endScroll
					)}"
				>
					<p class="hover:text-red-700 text-center">{@html item.label}</p>
				</div>
			{/each}
		</div>
	</div>
</main>

<svelte:window bind:scrollY />
