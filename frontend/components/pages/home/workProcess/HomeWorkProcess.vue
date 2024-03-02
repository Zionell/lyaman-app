<template>
    <ul :class="$style.HomeWorkProcess">
        <li
            v-for="(item, ind) in data"
            :key="item.id"
            :class="[$style.item, {[$style._isRight]: ind % 2 !== 0}]"
        >
            <div
                :class="$style.itemWrap"
            >
                <div :class="$style.itemPoint">
                    <span></span>
                </div>
                <h4 :class="$style.itemTitle">{{ ind+1 }}. {{ item.attributes.title }}</h4>
                <div :class="$style.itemText" v-html="item.attributes.text"></div>
            </div>
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
        position: relative;
        display: flex;
        flex-direction: column;
        gap: 3.2rem;

        &:before {
            content: "";
            position: absolute;
            top: 0;
            left: 50%;
            width: 1px;
            height: 100%;
            background: $light;
            transform: translateX(-50%);
        }

        @include respond-to(mobile) {
            flex-direction: column;
            gap: 1.8rem;
        }
    }

    .item {
        position: relative;
        display: flex;

        &._isRight {
            justify-content: flex-end;
        }
    }

    .itemWrap {
        width: 51.6rem;
        padding: 2.4rem 4rem;
        border-radius: 1.6rem;
        background: rgb(255 255 255 / 11%);
    }

    .itemPoint {
        position: absolute;
        top: 50%;
        left: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 2rem;
        height: 2rem;
        border-radius: 100%;
        border: 2px solid $light;
        background: $dark;
        transform: translate(-50%, -50%);

        span {
            width: 50%;
            height: 50%;
            border-radius: 100%;
            background: $blue;
        }
    }

    .itemTitle {
        margin-bottom: 2.4rem;
        font-family: $ff-bold;
        font-size: 2.1rem;
        line-height: 3.4rem;
        color: $blue;

        @include respond-to(mobile) {
            font-size: 1.8rem;
        }
    }

    .itemText {
        font-family: $ff-medium;
        font-size: 1.4rem;
        line-height: 2.4rem;
    }
</style>
