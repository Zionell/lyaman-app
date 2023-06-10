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
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(1rem, 26rem));
        justify-content: center;
        gap: 3.2rem;
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
    }

    .itemText {
        @extend .p16;

        color: var(--white);
    }
</style>
