<template>
    <header :class="[$style.TheHeader, {[$style._fixed]: !isVisible}]">
        <div :class="[$style.wrap, 'container']">
            <SvgIcon
                ref="logo"
                :class="$style.logo"
                name="logo"
            />

            <nav :class="$style.nav">
                <a
                    v-for="(item, ind) in menuItems"
                    :key="ind"
                    :href="`#${item.value}`"
                    :class="[$style.navItem, 'link', 'navItem']"
                >
                    {{ item.label }}
                </a>
            </nav>

            <VButton
                :class="[$style.btn, 'button']"
                tag="nuxt-link"
                to="#contacts"
                icon="arrow-right"
                round
            >
                Написать мне
            </VButton>

            <TheBurger/>
        </div>
    </header>
</template>

<script>
import { mapState } from 'vuex';
import headerVisibility from '~/mixins/headerVisibility';
import TheBurger from '~/components/layouts/header/TheBurger';
import { gsap } from 'gsap';
import VButton from '~/components/ui/button/VButton';

export default {
    name: 'TheHeader',

    components: {
        TheBurger,
        VButton,
    },

    mixins: [headerVisibility],

    data() {
        return {
            timeline: null,
        };
    },

    computed: {
        ...mapState({
            menuItems: state => state.general.menuItems,
        }),
    },

    mounted() {
        this.$nextTick(() => {
            // this.initialAnimation();
        });
    },

    methods: {
        initialAnimation() {
            gsap.from(this.$refs?.logo, {
                x: -1000,
                duration: 1,
            });
            gsap.from('.button', {
                x: 1000,
                duration: 1,
            });
            // gsap.from('.navItem', {
            //     x: 100,
            //     duration: 3,
            //     stagger: 0.3,
            // });
            // gsap.utils.toArray('.navItem')
            //     .forEach((item, ind) => {
            //     });
        },
    },
};
</script>

<style lang="scss" module>
    .TheHeader {
        overflow: hidden;
        display: flex;
        align-items: center;
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

        & .btn {
            @include respond-to(mobile) {
                display: none;
            }
        }

        @include respond-to(tablet) {
            position: sticky;
            top: 0;
            z-index: 10;
            height: auto;
        }

        @include respond-to(mobile) {
            background: var(--secondary);
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
    }

    .nav {
        flex-grow: 1;
        margin: 0 6.2rem;

        @include respond-to(mobile) {
            display: none;
        }
    }

    .navItem {
        @extend .p16;

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
            background: var(--black);
            transition: $transition;
        }

        @include hover() {
            &:hover {
                &:after {
                    width: 100%;
                }
            }
        }
    }
</style>
