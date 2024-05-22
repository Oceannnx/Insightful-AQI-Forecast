<script lang="ts">
	import logo from '../asset/logo.png';
	import { pageContent } from '../context/pageContent';
	import { scroll } from '../utils/scroll';
	let scrollY = 0;
</script>

<main class="flex flex-col items-center">
	<div class="flex flex-col items-center fixed top-0">
		<img class="w-3/4" src={logo} alt="logo" />
		<div class=" h-fit flex flex-col items-center p-10 w-fit">
			{#each pageContent as item}
				<!-- svelte-ignore a11y-click-events-have-key-events -->
				<!-- svelte-ignore a11y-no-static-element-interactions -->
				<div
					class="w-full h-20 flex justify-center items-center text-white {scroll(
						scrollY,
						item.startScroll,
						item.endScroll
					)}"
					on:click={() => {
						scrollTo({ top: item.center, behavior: 'smooth' });
					}}
				>
					<p class="hover:text-orange-400 text-center cursor-pointer drop-shadow-lg">
						{@html item.label}
					</p>
				</div>
			{/each}
		</div>
	</div>
</main>

<svelte:window bind:scrollY />
