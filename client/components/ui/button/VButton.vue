<template>
    <component
        :is="tag"
        :class="[$style.VButton, classes]"
        v-bind="$attrs"
        @click.prevent="$emit('click')"
    >
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
            validator: () => ['primary', 'secondary', 'outlined', 'slider'],
        },

        icon: {
            type: String,
            default: '',
        },

        disabled: {
            type: Boolean,
            default: false,
        },
    },

    computed: {
        classes() {
            return {
                [this.$style[this.type]]: this.type,
                [this.$style['is-disabled']]: this.disabled,
            };
        },
    },
};
</script>

<style lang="scss" module>
    .VButton {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 1rem 2rem;
        border: 1px solid var(--primary);
        background: var(--primary);
        font-size: 1.6rem;
        font-weight: 500;
        line-height: 2.6rem;
        letter-spacing: -.029rem;
        color: var(--white);
        transition: $transition;

        &.slider {
            width: 5rem;
            height: 5rem;
            padding: 0;
            border-radius: 50%;

            .icon {
                width: 3rem;
                height: 3rem;
                margin-left: 0;
            }
        }

        &.is-disabled {
            pointer-events: none;
            opacity: .6;
        }

        @include hover() {
            &:hover {
                background: var(--white);
                color: var(--primary);
            }
        }

        @include respond-to(mobile) {
            padding: .4rem 1rem;
            font-size: 1.4rem;
        }
    }

    .icon {
        width: 2rem;
        height: 1rem;
        margin-left: 1rem;
        transition: $transition;
    }
</style>
