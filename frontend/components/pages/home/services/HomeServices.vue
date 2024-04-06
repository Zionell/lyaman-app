<template>
    <div :class="$style.HomeServices">
        <div
            v-for="(item, ind) in data"
            :key="item.id"
            :class="[$style.service, {[$style._central]: ind === 1}]"
        >
            <h6 :class="$style.serviceTitle">{{ item.attributes.title }}</h6>

            <ul :class="$style.serviceText">
                <li v-for="(listItem, idx) in prepareList(item.attributes)" :key="`item_${idx}`">
                    <SvgIcon
                        :class="$style.icon"
                        name="success"
                    />

                    <div>{{ listItem }}</div>
                </li>
            </ul>
            <VButton
                :class="$style.btn"
                :color="ind === 1 ? 'blue' : ''"
                size="small"
                @click="goToContacts"
            >
                ОБСУДИТЬ ПРОЕКТ
            </VButton>
        </div>
    </div>
</template>

<script>
import { scrollTo } from '~/assets/js/common';

export default {
    name: 'HomeServices',

    props: {
        data: {
            type: Array,
            default: () => [],
        },
    },

    methods: {
        prepareList(arr) {
            return arr.items[0].children.map(ch => ch.children[0].text);
        },

        goToContacts() {
            scrollTo('contacts');
        },
    },
};
</script>

<style
    lang="scss"
    module
>
    .HomeServices {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 3.2rem;
    }

    .service {
        display: flex;
        flex-direction: column;
        padding: 3.2rem 1.6rem;
        border-radius: .8rem;
        box-shadow: 0 0 8px 0 $gray;
        background: $gray-100;

        &._central {
            border: 1px solid $gray;
        }
    }

    .serviceTitle {
        text-align: center;
        font-size: 3.2rem;
        font-weight: 700;
        line-height: 3.8rem;
    }

    .serviceText {
        display: flex;
        flex-direction: column;
        margin: 2.4rem 0;

        li {
            display: flex;
            align-items: center;
            font-size: 1.6rem;
            font-weight: 400;
            line-height: 2.4rem;
        }
    }

    .icon {
        flex-shrink: 0;
        width: 1.6rem;
        height: 1.6rem;
        margin-right: 1.6rem;
        color: $blue;
    }

    .btn {
        margin: auto auto 0;
    }
</style>
