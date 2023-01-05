<template>
    <div :class="$style.HomeAboutCourseItem" :style="style(ind)">
        <div :class="$style.content">
            <h3 :class="$style.title">{{ data.title }}</h3>
            <div :class="$style.text" v-html="data.text"/>
        </div>
    </div>
</template>

<script>
export default {
    name: 'HomeAboutCourseItem',

    props: {
        data: {
            type: Object,
            default: () => ({}),
        },

        ind: {
            type: Number,
            default: 0,
        },
    },

    methods: {
        style(ind) {
            return {
                backgroundImage: `url(/images/aboutCourse/${ind + 1}.png)`,
            };
        },
    },
};
</script>

<style lang="scss" module>
    .HomeAboutCourseItem {
        min-height: 27.4rem;
        padding: 4rem 0 0 8rem;
        background-repeat: no-repeat;
    }

    .content {
        height: 100%;
        padding: 2.8rem 3.2rem;
        background: linear-gradient(151deg, #8b9bdc 0%, rgba(255, 255, 255, 0) 43%);
    }

    .title {
        @extend .p24b;

        margin-bottom: 1.6rem;
    }

    .text {
        @extend .p16;
    }
</style>
