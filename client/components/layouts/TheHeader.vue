<template>
    <header :class="[$style.TheHeader, {[$style._fixed]: !isVisible}]">
        <div :class="[$style.wrap, 'container']">
            <SvgIcon :class="$style.logo" name="logo"/>

            <nav :class="$style.nav">
                <nuxt-link
                    v-for="(item, ind) in menuItems"
                    :key="ind"
                    :to="`#${item.value}`"
                    :class="[$style.navItem, 'link']"
                >
                    {{ item.label }}
                </nuxt-link>
            </nav>

            <VButton
                tag="nuxt-link"
                to="#contacts"
                icon="arrow-right"
            >
                Записаться
            </VButton>
        </div>
    </header>
</template>

<script>
import { mapState } from 'vuex';
import VButton from '~/components/ui/button/VButton';
import headerVisibility from '~/mixins/headerVisibility';

export default {
    name: 'TheHeader',

    components: {
        VButton,
    },

    mixins: [headerVisibility],

    computed: {
        ...mapState({
            menuItems: state => state.general.menuItems,
        }),
    },
};
</script>

<style lang="scss" module>
    .TheHeader {
        height: $h-height;
        background: var(--white);
        transition: $transition;

        &._fixed {
            position: fixed;
            top: 0;
            right: 0;
            left: 0;
            z-index: 10;
            width: 100%;
            height: auto;

            .wrap {
                padding-top: 1rem;
                padding-bottom: 1rem;
            }
        }
    }

    .wrap {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .logo {
        width: 17rem;
        height: 3.8rem;
    }

    .nav {
        flex-grow: 1;
        margin: 0 5.3rem;
    }

    .navItem {
        @extend .p16;

        position: relative;
        transition: $transition;

        &:not(:last-child) {
            margin-right: 3rem;
        }

        &:after {
            content: "";
            position: absolute;
            left: 0;
            display: block;
            width: 0;
            height: 1px;
            background: var(--black);
            transition: $transition;
        }

        &:hover {
            &:after {
                width: 100%;
            }
        }
    }
</style>
