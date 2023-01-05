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
                    Записаться
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
        height: calc(100vh - $h-height);
    }

    .wrap {
        display: grid;
        grid-template-columns: 1fr 46rem;
        justify-content: space-between;
        gap: 10rem;
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
        @extend .p18;

        padding: 4rem 0;
    }

    .imgWrap {
        height: 55rem;
    }
</style>
