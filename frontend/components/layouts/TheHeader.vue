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
                <a
                    v-for="(mes, ind) in messengers"
                    :key="ind"
                    :href="mes.link"
                    target="_blank"
                    :class="$style.link"
                >
                    <NuxtImg
                        v-if="image(mes.icon)"
                        format="webp"
                        :src="image(mes.icon)"
                        alt="Фото отзыва"
                        loading="lazy"
                        placeholder
                        fit="contain"
                        :class="$style.image"
                        provider="strapi"
                    />
                </a>
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
            messengers: state => state.general.socialLinks,
        }),
    },

    methods: {
        handleClick(val) {
            scrollTo(val, 90);
        },

        image(val) {
            return val?.data?.attributes?.url;
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
        display: flex;
        align-items: center;

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

    .link {
        transition: $transition;

        &:not(:last-child) {
            margin-right: .8rem;
        }

        @include hover {
            filter: brightness(.5);
        }
    }

    .image {
        width: 3.2rem;
        height: 3.2rem;
    }
</style>
