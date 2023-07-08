<template>
    <ul :class="$style.HomeWorkProcess">
        <li
            v-for="item in data"
            :key="item.id"
            :class="$style.item"
        >
            <div :class="$style.itemTop">
                <span></span>
            </div>
            <h4 :class="$style.itemTitle">{{ item.title }}</h4>
            <div :class="$style.itemText" v-html="item.text"></div>
        </li>
    </ul>
</template>

<script>
export default {
    name: 'HomeWorkProcess',

    props: {
        data: {
            type: Array,
            default: () => [],
        },
    },
};
</script>

<style lang="scss" module>
    .HomeWorkProcess {
        display: flex;
        justify-content: center;
        gap: 3.2rem;

        @include respond-to(mobile) {
            flex-direction: column;
            gap: 1.8rem;
        }
    }

    .item {
        width: 26rem;
    }

    .itemTop {
        display: flex;
        align-items: center;

        span {
            display: flex;
            flex-shrink: 0;
            width: 2.4rem;
            height: 2.4rem;
            margin-right: 2.4rem;
            border-radius: 50%;
            background: var(--white);

            @include respond-to(mobile) {
                width: 1.4rem;
                height: 1.4rem;
            }
        }

        &:after {
            content: "";
            width: 60%;
            border: 1px dashed var(--lightGrey);
            opacity: .4;
        }
    }

    .itemTitle {
        @extend .p24b;

        margin: 1.6rem 0 .4rem;
        color: var(--white);

        @include respond-to(mobile) {
            font-size: 1.8rem;
        }
    }

    .itemText {
        @extend .p16;

        color: var(--white);

        @include respond-to(mobile) {
            font-size: 1.4rem;
        }
    }
</style>
