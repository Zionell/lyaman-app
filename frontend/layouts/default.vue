<template>
    <div :class="$style.DefaultLayout">
        <TheHeader/>
        <main :class="$style.main">
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
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 100vh;
        background: $dark;
    }

    .main {
        flex-grow: 1;
    }
</style>
