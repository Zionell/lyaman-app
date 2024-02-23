<template>
    <header :class="$style.TheHeader">
        <div :class="[$style.wrap, 'container']">
            <SvgIcon
                :class="$style.logo"
                name="logo"
            />

            <nav :class="$style.nav">
                <button
                    v-for="(item, ind) in menuItems"
                    :key="ind"
                    :class="[$style.navItem, 'link', 'p18']"
                    @click="handleClick(item.value)"
                >
                    {{ item.label }}
                </button>
                <span :class="$style.divider"/>
            </nav>
        </div>
        <TheBurger/>
    </header>
</template>

<script>
import { mapState } from 'vuex';
import TheBurger from '~/components/layouts/header/TheBurger';
import { scrollTo } from '~/assets/js/common';

export default {
    name: 'TheHeader',

    components: {
        TheBurger,
    },

    computed: {
        ...mapState({
            menuItems: state => state.general.menuItems,
        }),
    },

    methods: {
        handleClick(val) {
            scrollTo(val, 90);
        },
    },
};
</script>

<style lang="scss" module>
    .TheHeader {
        position: sticky;
        top: 0;
        z-index: 10;
        overflow: hidden;
        display: flex;
        align-items: center;
        height: $h-height;
        background: $dark;
        transition: $transition;

        & .btn {
            @include respond-to(mobile) {
                display: none;
            }
        }

        @include respond-to(mobile) {
            height: $h-height-mobile;
        }
    }

    .wrap {
        display: flex;
        align-items: center;
        justify-content: space-between;

        @include respond-to(mobile) {
            padding-top: .8rem;
            padding-bottom: .8rem;
        }
    }

    .logo {
        width: 17rem;
        height: 3.8rem;
        color: $light;
    }

    .nav {
        @include respond-to(mobile) {
            display: none;
        }
    }

    .navItem {
        position: relative;
        transition: $transition;

        &:not(:last-child) {
            margin-right: 2.4rem;
        }

        &:after {
            content: "";
            position: absolute;
            left: 0;
            display: block;
            width: 0;
            height: 1px;
            background: $light;
            transition: $transition;
        }

        @include hover {
            &:after {
                width: 100%;
            }
        }
    }

    .divider {
        width: 1px;
        height: 2.4rem;
        margin: 0 1.6rem;
        background: $light;
    }
</style>
