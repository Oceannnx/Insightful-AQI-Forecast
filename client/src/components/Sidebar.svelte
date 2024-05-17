<script lang='ts'>
    import logo from '../asset/logo.png'

    let scrollY = 0
    $:{
        console.log('scorll ' + scrollY)
    }
</script>


<main class='h-full flex flex-col items-center  '>
    <img class='w-3/4' src={logo} alt='logo'>
    <div class="w-3/4 h-fit bg-red-700 flex flex-col items-center">
        {#each Array(5) as _, i}
            <div class="w-full h-20 bg-blue-700 flex justify-center items-center ">
                <p class="hover:text-red-700">Menu {i}</p>
            </div>
        {/each}
    </div>
</main>

<svelte:window bind:scrollY={scrollY} />