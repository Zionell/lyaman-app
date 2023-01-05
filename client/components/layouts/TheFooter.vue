<template>
    <footer :class="$style.TheFooter">
        <div class="container">
            <div :class="$style.footerTop">
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
            </div>

            <div :class="$style.socialLinks">
                <a
                    v-for="(link, ind) in socialLinks"
                    :key="ind"
                    :class="$style.link"
                    :href="link.link"
                    target="_blank"
                >{{ link.label }}</a>
            </div>

            <MyLogo/>
        </div>
    </footer>
</template>

<script>
import { mapState } from 'vuex';
import MyLogo from '~/components/common/MyLogo';

export default {
    name: 'TheFooter',

    components: {
        MyLogo,
    },

    computed: {
        ...mapState({
            menuItems: state => state.general.menuItems,
            socialLinks: state => state.general.socialLinks,
        }),
    },
};
</script>

<style lang="scss" module>
    .TheFooter {
        padding-top: 3.2rem;
        padding-bottom: 3.2rem;
        background: var(--secondary);
    }

    .footerTop {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .nav {
        display: flex;
    }

    .navItem {
        position: relative;
        transition: $transition;

        &:not(:last-child) {
            margin-right: 2rem;
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

    .socialLinks {
        @extend .p14b;

        display: grid;
        gap: .5rem;
        margin: 3.2rem 0 3.2rem auto;
        text-align: right;
    }

    .link {
        color: var(--black);
        transition: $transition;

        &:hover {
            color: var(--primaryHover);
        }
    }

    .logo {
        width: 17rem;
        height: 3.8rem;
    }
</style>
