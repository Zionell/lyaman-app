<template>
    <div :class="$style.HomeAboutItem">
        <div :class="$style.imgWrap">
            <img
                :class="$style.img"
                :src="image"
                alt="Icon"
            >
        </div>
        <h3 :class="$style.title">{{ data.title }}</h3>
        <p :class="$style.text">{{ data.text }}</p>
    </div>
</template>

<script>
export default {
    name: 'HomeAboutItem',

    props: {
        data: {
            type: Object,
            default: () => ({}),
        },

        isEven: {
            type: Boolean,
            default: false,
        },
    },

    computed: {
        image() {
            const url = this.$api.baseURL + this.data?.icon;
            return url;
        },
    },
};
</script>

<style lang="scss" module>
    .HomeAboutItem {
        @include respond-to(tablet) {
            display: grid;
            grid-template-columns: 5rem 1fr;
            gap: .8rem 2rem;
            align-items: start;
        }
    }

    .imgWrap {
        width: 4.4rem;
        height: 4.4rem;

        @include respond-to(tablet) {
            grid-row: 1/3;
            width: 100%;
            height: auto;
        }
    }

    .img {
        object-fit: contain;
    }

    .title {
        @extend .p18b;

        padding: 1.6rem 0 .7rem;

        @include respond-to(tablet) {
            padding: 0;
            font-size: 2.1rem;
        }

        @include respond-to(mobile) {
            font-size: 1.6rem;
        }
    }

    .text {
        @extend .p16;

        @include respond-to(mobile) {
            font-size: 1.4rem;
        }
    }
</style>
