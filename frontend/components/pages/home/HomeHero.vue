<template>
    <div :class="[$style.HomeHero, 'container']">
        <div :class="$style.content">
            <h1 :class="$style.title">{{ data.title }}</h1>
            <div :class="$style.text" v-html="data.text"/>

            <VButton
                @click="goToContacts"
            >
                {{ data.buttonText }}
            </VButton>
        </div>
        <div :class="$style.right">
            <div :class="$style.imgWrap">
                <NuxtImg
                    v-if="image"
                    format="webp"
                    :src="image"
                    alt="Мое фото"
                    loading="lazy"
                    :placeholder="15"
                    provider="customProvider"
                    :class="$style.image"
                />
            </div>
            <div :class="$style.tags">
                <div :class="$style.tag">
                    <h5 :class="$style.tagTitle">{{ data.advantages_title_1 }}</h5>
                    <div :class="$style.tagText">{{ data.advantages_text_1 }}</div>
                </div>
                <div :class="$style.tag">
                    <h5 :class="$style.tagTitle">{{ data.advantages_title_2 }}</h5>
                    <div :class="$style.tagText">{{ data.advantages_text_2 }}</div>
                </div>
            </div>
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

    computed: {
        image() {
            return this.data?.image?.data?.attributes?.url;
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
        grid-template-columns: 51rem 1fr;
        align-items: center;
        gap: 10rem;
        min-height: calc(calc(var(--vh, 1vh) * 100) - $h-height);

        @include respond-to(tablet) {
            grid-template-columns: 1fr;
            gap: 3.2rem;
        }

        @include respond-to(mobile) {
            gap: 2.4rem;
            min-height: calc(100vh - $h-height-mobile);
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
        @extend .p22;

        padding: 1.6rem 0 3.2rem;
        color: $gray;

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

    .right {
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100%;

        &:after {
            content: "";
            position: absolute;
            top: 50%;
            left: 50%;
            z-index: 1;
            width: 70rem;
            aspect-ratio: 1;
            border-radius: 100%;
            background: rgba(248, 247, 249, .1);
            transform: translate(-50%, -50%);
            filter: blur(200px);
        }
    }

    .imgWrap {
        position: relative;
        z-index: 2;
        overflow: hidden;
        width: 43rem;
        height: 43rem;
        border-radius: 2rem 2rem 0 0;
    }

    .tags {
        position: relative;
        z-index: 2;
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1.2rem;
        width: 100%;
        max-width: 45.6rem;
        padding: 1.2rem;
        border-radius: 1.6rem;
        background: rgba(255, 255, 255, .88);
    }

    .tag {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        color: $dark;
    }

    .tagTitle {
        @extend .p26b;

        @include respond-to(mobile) {
            font-size: 1.6rem;
            line-height: 144%;
        }
    }

    .tagText {
        @extend .p16m;
    }
</style>
