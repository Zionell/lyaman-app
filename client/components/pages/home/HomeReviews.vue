<template>
    <div :class="$style.HomeReviews">
        <VButton
            :class="[$style.btn, $style._prev]"
            type="slider"
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
                    v-for="(slide, idx) in slides"
                    :key="idx"
                    class="swiper-slide"
                    :class="$style.review"
                >
                    <div :class="$style.reviewText" v-html="slide.review"/>
                    <div :class="$style.reviewAuthor" v-html="slide.name"/>
                </div>
            </div>
            <div
                ref="pagination"
                :class="$style.bullets"
            />
        </div>

        <VButton
            :class="[$style.btn, $style._next]"
            type="slider"
            icon="right"
            :disabled="isAvailable.isEnd"
            @click="slider.slideNext()"
        />
    </div>
</template>

<script>
export default {
    name: 'HomeReviews',

    props: {
        slides: {
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
                spaceBetween: 100,
                speed: 800,

                pagination: {
                    el: this.$refs.pagination,
                    type: 'bullets',
                },
            });
        },
    },

};
</script>

<style lang="scss" module>
    .HomeReviews {
        display: flex;
        align-items: center;
    }

    .slider {
        position: relative;
        overflow: hidden;
        width: 100%;

        .bullets {
            position: absolute;
            bottom: 1rem;
            z-index: 10;
            display: flex;
            justify-content: center;

            :global(.swiper-pagination-bullet) {
                width: 5rem;
                height: .4rem;
                border-radius: 0;

                &:not(:last-child) {
                    margin-right: 1rem;
                }
            }

            :global(.swiper-pagination-bullet-active) {
                background: var(--primary);
            }
        }
    }

    .review {
        padding: 7rem;
        border-radius: 2rem;
        background: var(--secondary);
        user-select: none;
    }

    .reviewText {
        font-family: "Roboto", sans-serif;
        font-size: 2.4rem;
        line-height: 3.6rem;
    }

    .reviewAuthor {
        position: relative;
        padding-top: 2.3rem;
        padding-left: 7rem;
        font-size: 2.4rem;
        color: #333;
    }

    .reviewAuthor:before {
        content: "";
        position: absolute;
        top: 65%;
        left: 0;
        display: block;
        width: 6rem;
        height: 3px;
        margin-top: 1px;
        background-color: var(--primary);
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
