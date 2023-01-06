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
        position: relative;

        &:nth-child(4),
        &:last-child {
            & .line {
                display: none;
            }
        }
    }

    .line {
        position: absolute;
        top: 4rem;
        right: 0;
        width: 16.7rem;
        height: 3.2rem;
    }

    .imgWrap {
        width: 4.4rem;
        height: 4.4rem;
    }

    .title {
        @extend .p18b;

        padding: 1.6rem 0 .7rem;
    }

    .text {
        @extend .p16;
    }
</style>
