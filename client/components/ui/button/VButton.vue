<template>
    <button
        :class="[$style.VButton, classes]"
        v-bind="$attrs"
        @click.prevent="$emit('click')"
    >
        <transition name="fade" mode="out-in">
            <VLoader v-if="isLoading"/>
            <div v-else :class="$style.wrap">
                <slot></slot>
                <SvgIcon
                    v-if="icon"
                    :class="$style.icon"
                    :name="icon"
                />
            </div>
        </transition>
    </button>
</template>

<script>
export default {
    name: 'VButton',

    props: {
        icon: {
            type: String,
            default: '',
        },

        disabled: {
            type: Boolean,
            default: false,
        },

        color: {
            type: String,
            default: '',
        },

        size: {
            type: String,
            default: '',
        },

        isLoading: {
            type: Boolean,
            default: false,
        },

        isSlider: {
            type: Boolean,
            default: false,
        },
    },

    computed: {
        classes() {
            return {
                [this.$style[`color-${this.color}`]]: this.color,
                [this.$style[`size-${this.size}`]]: this.size,
                [this.$style['is-disabled']]: this.disabled,
                [this.$style['is-loading']]: this.isLoading,
                [this.$style['is-slider']]: this.isSlider,
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
        flex-shrink: 0;
        padding: 1.2rem 2.4rem;
        border-radius: 1.6rem;
        border: 2px solid $light;
        font-size: 2.2rem;
        font-weight: 700;
        line-height: 1.1;
        color: $light;
        transition: $transition;

        &.is-loading,
        &.is-disabled {
            opacity: .4;
            cursor: not-allowed;
        }

        &.is-slider {
            padding: 0;
            border: none;

            .icon {
                width: 2.4rem;
                height: 2.4rem;
                margin-left: 0;
            }
        }

        @include hover {
            background: $light;
            color: $blue;
        }

        &.size-small {
            width: max-content;
            padding: .8rem 2.4rem;
            font-size: 1.4rem;
            font-weight: 700;
        }

        &.color-blue {
            position: relative;
            overflow: hidden;
            border: none;

            &:before {
                content: "";
                position: absolute;
                top: 0;
                left: 0;
                z-index: 1;
                width: 100%;
                height: 100%;
                box-shadow: 0 4px 4px 0 rgba(0, 0, 0, .25);
                background: $linearGradient;
                transition: $transition;
            }

            .wrap {
                position: relative;
                z-index: 2;
            }

            @include hover {
                &:before {
                    opacity: 0;
                }
            }
        }

        @include respond-to(mobile) {
            padding: .4rem 1rem;
            font-size: 1.4rem;
        }
    }

    .wrap {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }

    .icon {
        width: 2rem;
        height: 1rem;
        margin-left: 1rem;
        transition: $transition;
    }
</style>
