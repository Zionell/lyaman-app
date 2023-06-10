<template>
    <div :class="[$style.SectionTemplate, {[$style._isBlue]: isBlue}]">
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

        isBlue: {
            type: Boolean,
            default: false,
        },
    },
};
</script>

<style lang="scss" module>
    .SectionTemplate {
        padding: 5rem 0;

        &._isBlue {
            background: var(--secondary);

            .title {
                color: var(--white);
            }
        }
    }

    .title {
        width: 60%;
        margin: 0 auto 6.4rem;
        text-align: center;
        color: var(--secondary);

        @include respond-to(tablet) {
            margin: 0 auto 4rem;
        }

        @include respond-to(mobile) {
            width: 100%;
            margin: 0 auto 2.4rem;
            font-size: 2.4rem;
        }
    }
</style>
