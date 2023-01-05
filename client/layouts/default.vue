<template>
    <div :class="[$style.DefaultLayout, 'castom__scroll']">
        <TheHeader/>
        <main>
            <Nuxt/>
        </main>
        <TheFooter/>
    </div>
</template>

<script>
import TheHeader from '~/components/layouts/TheHeader';
import TheFooter from '~/components/layouts/TheFooter';

export default {
    name: 'DefaultLayout',

    components: {
        TheHeader,
        TheFooter,
    },
};
</script>

<style lang="scss" module>
    .DefaultLayout {
        //
    }
</style>
