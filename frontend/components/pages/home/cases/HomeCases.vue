<template>
    <div :class="$style.HomeCases">
        <VButton
            v-if="slider"
            :class="[$style.btn, $style._prev]"
            is-slider
            icon="left"
            :disabled="isAvailable.isBeginning"
            @click="slider.slidePrev()"
        />

        <div
            ref="slider"
            class="slider"
            :class="$style.slider"
        >
            <div class="swiper-wrapper">
                <div
                    v-for="item in data"
                    :key="item.id"
                    class="swiper-slide"
                    :class="$style.case"
                >
                    <div :class="$style.caseContent">
                        <h4 :class="$style.caseTitle">{{ item.attributes.title }}</h4>
                        <div :class="$style.caseText">
                            <div :class="$style.caseTask">
                                <p :class="$style.caseItemTitle">Задачи:&nbsp;</p>
                                <div :class="$style.caseItemText">{{ item.attributes.tasks }}</div>
                            </div>
                            <div :class="$style.caseListWrap">
                                <p :class="$style.caseItemTitle">Что было сделано?</p>
                                <ul :class="$style.list">
                                    <li
                                        v-for="(listItem, ind) in prepareList(item.attributes.text)"
                                        :key="`item_${ind}`"
                                        :class="$style.caseListItem"
                                    >
                                        <div>{{ listItem }}</div>
                                    </li>
                                </ul>
                            </div>
                        </div>

                        <div v-if="image(item)" :class="$style.imageWrap">
                            <div :class="$style.imageTitle">
                                {{ item.attributes.imageTitle }}
                            </div>
                            <NuxtImg
                                format="webp"
                                :src="image(item)"
                                alt="Пример работ"
                                loading="lazy"
                                placeholder
                                fit="contain"
                                :class="$style.image"
                                provider="strapi"
                            />
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <VButton
            v-if="slider"
            :class="[$style.btn, $style._next]"
            is-slider
            icon="right"
            :disabled="isAvailable.isEnd"
            @click="slider.slideNext()"
        />
    </div>
</template>

<script>
export default {
    name: 'HomeCases',

    props: {
        data: {
            type: Array,
            default: () => [],
        },
    },

    data() {
        return {
            slider: null,
        };
    },

    computed: {
        isAvailable() {
            return {
                isBeginning: Boolean(this.slider?.isBeginning),
                isEnd: Boolean(this.slider?.isEnd),
            };
        },
    },

    mounted() {
        this.$nextTick(() => {
            this.initSlider();
        });
    },

    methods: {
        initSlider() {
            this.slider = new this.$Swiper(this.$refs.slider, {
                slidesPerView: 1,
                spaceBetween: 32,
                speed: 800,
            });
        },

        image(val) {
            return val?.attributes?.image?.data?.attributes?.url;
        },

        prepareList(arr) {
            if (!Array.isArray(arr) && !arr?.length) {
                return [];
            }
            return arr[0]?.children?.map(ch => ch?.children[0]?.text);
        },
    },
};
</script>

<style
    lang="scss"
    module
>
    .HomeCases {
        display: flex;
        align-items: center;
    }

    .slider {
        position: relative;
        overflow: hidden;
        width: 100%;
    }

    .case {
        display: flex;
        flex-direction: column;
    }

    .caseTitle {
        font-size: 2.2rem;
        font-weight: 700;
        line-height: 2.4rem;
    }

    .caseContent {
        display: grid;
        grid-template-columns: 1.5fr 1fr;
        gap: 4rem 10rem;
    }

    .caseText {
        //
    }

    .caseTask {
        display: flex;
        margin-bottom: 1.6rem;
    }

    .caseItemTitle {
        font-size: 1.4rem;
        font-weight: 700;
        line-height: 2.4rem;
    }

    .caseListItem,
    .caseItemText {
        font-size: 1.4rem;
        font-weight: 500;
        line-height: 2.4rem;
    }

    .list {
        margin-top: .8rem;
    }

    .caseListItem {
        display: flex;

        &:before {
            content: "";
            display: flex;
            flex-shrink: 0;
            width: .4rem;
            height: .4rem;
            margin-top: 1rem;
            margin-right: .8rem;
            border-radius: 100%;
            background: $light;
        }
    }

    .imageWrap {
        grid-column: 2/3;
        grid-row: 1/3;
    }

    .imageTitle {
        font-size: 1.4rem;
        font-weight: 700;
        line-height: 2.4rem;
    }

    .image {
        width: 100%;
        height: auto;
    }

    .btn {
        &._prev {
            margin-right: 2.4rem;
        }

        &._next {
            margin-left: 2.4rem;
        }

        @include respond-to(tablet) {
            display: none;
        }
    }
</style>
