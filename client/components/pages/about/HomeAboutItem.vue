<template>
    <div :class="$style.HomeAboutItem">
        <div :class="$style.imgWrap">
            <img
                :class="$style.img"
                :src="image"
                alt="Icon"
            >
        </div>
        <SvgIcon :class="$style.line" :name="isEven ? 'even-line' : 'odd-line'"/>
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
        width: 7.2rem;
        height: 7.2rem;
        padding: 2.4rem;
        border-radius: 50%;
        background: var(--secondary);
    }

    .title {
        @extend .p24b;

        padding: 1.6rem 0 .4rem;
    }

    .text {
        @extend .p16;
    }
</style>
