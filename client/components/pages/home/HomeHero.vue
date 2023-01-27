<template>
    <div :class="$style.HomeHero">
        <div :class="['container', $style.wrap]">
            <div :class="$style.content">
                <h1 :class="$style.title">{{ data.title }}</h1>
                <div :class="$style.text" v-html="data.text"/>

                <VButton
                    tag="nuxt-link"
                    to="#contacts"
                    icon="arrow-right"
                >
                    Написать мне
                </VButton>
            </div>
            <div :class="$style.imgWrap">
                <img :src="image" alt="Мое фото">
            </div>
        </div>
    </div>
</template>

<script>
import VButton from '~/components/ui/button/VButton';

export default {
    name: 'HomeHero',

    components: {
        VButton,
    },

    props: {
        data: {
            type: Object,
            default: () => ({}),
        },
    },

    computed: {
        image() {
            const url = this.$api.baseURL + this.data?.img_url;
            return url;
        },
    },
};
</script>

<style lang="scss" module>
    .HomeHero {
        display: flex;
        align-items: center;
        min-height: calc(100vh - $h-height);

        @include respond-to(tablet) {
            padding-top: 5rem;
            padding-bottom: 5rem;
        }

        @include respond-to(mobile) {
            padding-top: 2.4rem;
            padding-bottom: 2.4rem;
        }
    }

    .wrap {
        display: grid;
        grid-template-columns: 1fr 46rem;
        justify-content: space-between;
        gap: 10rem;

        @include respond-to(tablet) {
            grid-template-columns: 1fr;
            gap: 5rem;
            width: 100%;
            height: 100%;
        }

        @include respond-to(mobile) {
            gap: 2rem;
        }
    }

    .content {
        display: flex;
        flex-direction: column;
        align-items: flex-start;

        @include respond-to(tablet) {
            width: 60%;
        }

        @include respond-to(mobile) {
            width: 100%;
        }
    }

    .title {
        @extend .h1;

        @include respond-to(mobile) {
            font-size: 3.2rem;
        }
    }

    .text {
        @extend .p18;

        padding: 4rem 0;

        @include respond-to(tablet) {
            padding: 2.4rem 0;
        }

        @include respond-to(mobile) {
            padding: 1.2rem 0;
            font-size: 1.6rem;
        }
    }

    .imgWrap {
        height: 55rem;

        @include respond-to(tablet) {
            justify-self: end;
            width: 60%;
            height: 100%;
        }

        @include respond-to(mobile) {
            width: 100%;
        }
    }
</style>
