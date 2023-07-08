<template>
    <div :class="[$style.HomeHero, 'container']">
        <div :class="$style.left">
            <div :class="$style.imgWrap">
                <nuxt-img
                    format="webp"
                    :src="data.image"
                    alt="Мое фото"
                    loading="lazy"
                    :placeholder="15"
                    provider="customProvider"
                    :class="$style.image"
                />
            </div>
            <div :class="$style.tags">
                <div :class="$style.tag">
                    {{ data.tag1 }}
                </div>
                <div :class="$style.tag">
                    {{ data.tag2 }}
                </div>
            </div>
        </div>
        <div :class="$style.content">
            <h1 :class="$style.title">{{ data.title }}</h1>
            <div :class="$style.text" v-html="data.text"/>

            <VButton
                round
                @click="goToContacts"
            >
                {{ data.btnText }}
            </VButton>
        </div>
    </div>
</template>

<script>
import VButton from '~/components/ui/button/VButton';
import { scrollTo } from '~/assets/js/common';

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

    methods: {
        goToContacts() {
            scrollTo('contacts');
        },
    },
};
</script>

<style lang="scss" module>
    .HomeHero {
        display: grid;
        grid-template-columns: 50rem 1fr;
        align-items: center;
        justify-content: space-between;
        gap: 10rem;
        min-height: calc(100vh - $h-height);
        padding-top: 1.6rem;
        padding-bottom: 1.6rem;

        @include respond-to(tablet) {
            grid-template-columns: 1fr;
            gap: 3.2rem;
            padding-top: 4.8rem;
            padding-bottom: 4.8rem;
        }

        @include respond-to(mobile) {
            gap: 2.4rem;
            min-height: calc(100vh - $h-height-mobile);
            padding-top: 2.4rem;
            padding-bottom: 2.4rem;
        }
    }

    .content {
        display: flex;
        flex-direction: column;
        align-items: flex-start;

        @include respond-to(tablet) {
            order: 1;
        }
    }

    .title {
        @extend .h1;

        @include respond-to(tablet) {
            font-size: 3.2rem;
            line-height: 120%;
        }

        @include respond-to(mobile) {
            font-size: 2.4rem;
        }
    }

    .text {
        @extend .p24;

        padding: 4rem 0;

        @include respond-to(tablet) {
            padding: 2.4rem 0;
            font-size: 1.8rem;
            line-height: 144%;
        }

        @include respond-to(mobile) {
            padding: 1.2rem 0;
            font-size: 1.4rem;
        }
    }

    .left {
        display: grid;
        grid-template-rows: 1fr 7.2rem;
        gap: 2.4rem;

        @include respond-to(tablet) {
            grid-template-rows: 7.2rem 1fr;
            order: 2;
            height: 100%;
        }

        @include respond-to(mobile) {
            grid-template-rows: 1fr 3.2rem;
        }
    }

    .imgWrap {
        padding: 2rem;
        border-radius: 3rem;
        border: 5px solid var(--secondary);

        @include respond-to(tablet) {
            order: 2;
            height: 75rem;
        }

        @include respond-to(mobile) {
            order: 1;
            height: 28rem;
            padding: .8rem;
        }
    }

    .image {
        border-radius: 2rem;
    }

    .tags {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: .5rem;

        @include respond-to(tablet) {
            order: 1;
        }

        @include respond-to(mobile) {
            order: 2;
        }
    }

    .tag {
        @extend .p24;

        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 5rem;
        border: 5px solid var(--secondary);
        color: var(--secondary);

        @include respond-to(mobile) {
            font-size: 1.6rem;
            line-height: 144%;
        }
    }
</style>
