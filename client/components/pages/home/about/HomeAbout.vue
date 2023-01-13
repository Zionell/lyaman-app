<template>
    <div :class="$style.HomeAbout">
        <div :class="$style.itemsWrap">
            <HomeAboutItem
                v-for="(item, ind) in data.ways"
                :key="ind"
                :data="item"
            />
        </div>
        <div :class="$style.imageWrap">
            <img
                :class="$style.img"
                :src="image"
                alt="Icon"
            >
        </div>
    </div>
</template>

<script>
import HomeAboutItem from '~/components/pages/home/about/HomeAboutItem';

export default {
    name: 'HomeAbout',

    components: {
        HomeAboutItem,
    },

    props: {
        data: {
            type: Object,
            default: () => ({}),
        },
    },

    computed: {
        image() {
            const url = this.$api.baseURL + this.data?.image_url;
            return url;
        },
    },
};
</script>

<style lang="scss" module>
    .HomeAbout {
        display: grid;
        grid-template-columns: 50rem 1fr;
        gap: 10rem;

        @include respond-to(tablet) {
            grid-template-columns: 1fr;
            gap: 5rem;
        }

        @include respond-to(mobile) {
            gap: 2.4rem;
        }
    }

    .itemsWrap {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(20rem, 1fr));
        gap: 6rem 9rem;

        @include respond-to(tablet) {
            grid-template-columns: repeat(auto-fill, minmax(35rem, 1fr));
            gap: 2rem 3rem;
        }

        @include respond-to(mobile) {
            gap: 2rem;
        }
    }

    .img {
        object-fit: contain;
    }
</style>
