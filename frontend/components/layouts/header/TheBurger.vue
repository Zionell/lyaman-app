<template>
    <div :class="$style.TheBurger">
        <div :class="$style.burger" @click="isVisible = !isVisible">
            <span ref="pathTop"></span>
            <span ref="pathMiddle"></span>
            <span ref="pathBottom"></span>
        </div>

        <transition name="burger">
            <nav v-if="isVisible" :class="$style.list">
                <button
                    v-for="(item, ind) in menuItems"
                    :key="ind"
                    :class="[$style.navItem, 'link']"
                    @click="handleClick(item.value)"
                >
                    {{ item.label }}
                </button>
            </nav>
        </transition>
    </div>
</template>

<script>
import { mapState } from 'vuex';
import { gsap } from 'gsap';

export default {
    name: 'TheBurger',

    data() {
        return {
            isVisible: false,
        };
    },

    computed: {
        ...mapState({
            menuItems: state => state.general.menuItems,
        }),
    },

    watch: {
        isVisible: {
            immediate: true,
            handler() {
                if (this.isVisible) {
                    gsap.to(this.$refs.pathTop, {
                        rotation: 30,
                        transformOrigin: '-10px 10px',
                        duration: .3,
                    });
                    gsap.to(this.$refs.pathMiddle, {
                        opacity: 0,
                        translateX: '30px',
                        duration: .3,
                    });
                    gsap.to(this.$refs.pathBottom, {
                        rotation: -30,
                        transformOrigin: '17px 0px',
                        duration: .3,
                    });
                } else {
                    gsap.to(this.$refs.pathTop, {
                        rotation: 0,
                        duration: .3,
                    });
                    gsap.to(this.$refs.pathMiddle, {
                        opacity: 1,
                        translateX: 0,
                        duration: .3,
                    });
                    gsap.to(this.$refs.pathBottom, {
                        rotation: 0,
                        duration: .3,
                    });
                }
            },
        },
    },

    methods: {
        handleClick(val) {
            this.isVisible = false;
            this.$router.push({
                path: `#${val}`,
            });
        },
    },
};
</script>

<style lang="scss" module>
    .TheBurger {
        position: relative;
        display: none;

        @include respond-to(mobile) {
            display: flex;
        }
    }

    .burger {
        position: relative;
        z-index: 10;

        & span {
            display: block;
            width: 40px;
            height: 4px;
            background: var(--black);

            &:not(:last-child) {
                margin-bottom: 5px;
            }
        }
    }

    .list {
        position: fixed;
        top: 0;
        left: 0;
        display: grid;
        justify-items: center;
        align-content: center;
        gap: 2rem;
        width: 100%;
        height: 100%;
        background: white;
    }

    .navItem {
        //
    }
</style>
