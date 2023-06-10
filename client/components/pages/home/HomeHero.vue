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
                tag="nuxt-link"
                to="#contacts"
                round
            >
                {{ data.btnText }}
            </VButton>
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
};
</script>

<style lang="scss" module>
    .HomeHero {
        display: grid;
        grid-template-columns: 50rem 1fr;
        align-items: center;
        justify-content: space-between;
        gap: 10rem;
        height: calc(100vh - $h-height);
        padding-top: 1.6rem;
        padding-bottom: 1.6rem;
    }

    .content {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }

    .title {
        @extend .h1;
    }

    .text {
        @extend .p24;

        padding: 4rem 0;
    }

    .left {
        display: grid;
        grid-template-rows: 1fr 7.2rem;
        gap: 2.4rem;
    }

    .imgWrap {
        padding: 2rem;
        border-radius: 5rem;
        border: 5px solid var(--secondary);
    }

    .image {
        border-radius: 5rem;
    }

    .tags {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: .5rem;
    }

    .tag {
        @extend .p24;

        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 5rem;
        border: 5px solid var(--secondary);
        color: var(--secondary);
    }
</style>
