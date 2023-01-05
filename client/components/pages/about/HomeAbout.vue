<template>
    <div :class="$style.HomeAbout">
        <HomeAboutItem
            v-for="(item, ind) in data"
            :key="ind"
            :data="item"
            :is-even="isEven(ind)"
        />
    </div>
</template>

<script>
import HomeAboutItem from '~/components/pages/about/HomeAboutItem';

export default {
    name: 'HomeAbout',

    components: {
        HomeAboutItem,
    },

    props: {
        data: {
            type: Array,
            default: () => [],
        },
    },

    methods: {
        isEven(ind) {
            return ind % 2 === 0;
        },
    },
};
</script>

<style lang="scss" module>
    .HomeAbout {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 3rem;
    }
</style>
