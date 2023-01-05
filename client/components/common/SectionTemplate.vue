<template>
    <div :class="$style.SectionTemplate">
        <div class="container">
            <h2 :class="[$style.title, 'h3']">{{ title }}</h2>

            <slot></slot>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SectionTemplate',

    props: {
        title: {
            type: String,
            default: '',
        },
    },
};
</script>

<style lang="scss" module>
    .SectionTemplate {
        padding: 6.4rem 0 7.5rem;
    }

    .title {
        width: 60%;
        margin: 0 auto 6.4rem;
        text-align: center;
    }
</style>
