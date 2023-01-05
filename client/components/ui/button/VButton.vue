<template>
    <component :is="tag" :class="[$style.VButton, classes]">
        <slot></slot>
        <SvgIcon
            v-if="icon"
            :class="$style.icon"
            :name="icon"
        />
    </component>
</template>

<script>
export default {
    name: 'VButton',

    props: {
        tag: {
            type: String,
            default: 'button',
            validator: () => ['button', 'div', 'a', 'nuxt-link'],
        },

        type: {
            type: String,
            default: 'primary',
            validator: () => ['primary', 'secondary', 'outlined'],
        },

        icon: {
            type: String,
            default: '',
        },
    },

    computed: {
        classes() {
            return {
                [this.$style[this.type]]: this.type,
            };
        },
    },
};
</script>

<style lang="scss" module>
    .VButton {
        display: flex;
        align-items: center;
        padding: 1rem 2rem;
        border: 1px solid var(--primary);
        background: var(--primary);
        font-size: 1.6rem;
        font-weight: 500;
        line-height: 2.6rem;
        letter-spacing: -.029rem;
        color: var(--white);
        transition: $transition;

        &:hover {
            background: var(--white);
            color: var(--primary);
        }
    }

    .icon {
        width: 2rem;
        height: 1rem;
        margin-left: 1rem;
        transition: $transition;
    }
</style>
