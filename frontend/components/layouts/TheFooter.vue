<template>
    <footer :class="$style.TheFooter">
        <div class="container">
            <div :class="$style.footerTop">
                <nuxt-link to="/">
                    <SvgIcon :class="$style.logo" name="logo"/>
                </nuxt-link>
                <nav :class="$style.nav">
                    <nuxt-link
                        v-for="(item, ind) in menuItems"
                        :key="ind"
                        :to="`#${item.value}`"
                        :class="[$style.navItem, 'link', 'p18']"
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
                >{{ link.name }}</a>
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
    }

    .footerTop {
        display: flex;
        align-items: center;
        justify-content: space-between;

        @include respond-to(mobile) {
            flex-direction: column;
            align-items: flex-start;
        }
    }

    .nav {
        display: flex;

        @include respond-to(mobile) {
            align-self: center;
            margin-top: 3.2rem;
        }
    }

    .navItem {
        position: relative;
        transition: $transition;

        &:not(:last-child) {
            margin-right: 2rem;
        }

        &:visited {
            color: $light;
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

        @include respond-to(mobile) {
            font-size: 1.4rem;
        }
    }

    .socialLinks {
        display: grid;
        justify-items: end;
        gap: .5rem;
        margin: 3.2rem 0 3.2rem auto;
        text-align: right;

        @include respond-to(mobile) {
            margin: 2rem 0 2rem auto;
        }
    }

    .link {
        color: $dark;
        transition: $transition;

        @include hover {
            color: $blue;
        }
    }

    .logo {
        width: 17rem;
        height: 3.8rem;
        color: $light;
        transition: $transition;

        @include hover {
            color: $blue;
        }
    }
</style>
