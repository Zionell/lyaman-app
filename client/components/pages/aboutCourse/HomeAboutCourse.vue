<template>
    <div :class="$style.HomeAboutCourse">
        <HomeAboutCourseItem
            v-for="(item, ind) in data"
            :key="ind"
            :data="item"
            :ind="ind"
        />
    </div>
</template>

<script>
import HomeAboutCourseItem from '~/components/pages/aboutCourse/HomeAboutCourseItem';

export default {
    name: 'HomeAboutCourse',

    components: {
        HomeAboutCourseItem,
    },

    props: {
        data: {
            type: Array,
            default: () => [],
        },
    },
};
</script>

<style lang="scss" module>
    .HomeAboutCourse {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 6.9rem 3rem;
    }
</style>
