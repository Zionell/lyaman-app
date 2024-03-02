<template>
    <div :id="title.value" :class="$style.SectionTemplate">
        <div class="container">
            <h2 :class="$style.title">{{ title.label }}</h2>

            <slot></slot>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SectionTemplate',

    props: {
        title: {
            type: Object,
            default: () => ({}),
        },
    },
};
</script>

<style lang="scss" module>
    .SectionTemplate {
        padding: 5rem 0;
    }

    .title {
        width: 60%;
        margin-bottom: 6.4rem;
        font-family: $ff-bold;
        font-size: 5.2rem;
        line-height: 120%;
        color: $light;

        @include respond-to(tablet) {
            margin-bottom: 4rem;
        }

        @include respond-to(mobile) {
            width: 100%;
            margin-bottom: 2.4rem;
            font-size: 2.4rem;
        }
    }
</style>
