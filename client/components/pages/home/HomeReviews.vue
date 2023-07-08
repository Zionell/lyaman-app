<template>
    <div :class="$style.HomeReviews">
        <VButton
            v-if="slider"
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
                    v-for="review in data"
                    :key="review.id"
                    class="swiper-slide"
                    :class="$style.review"
                >
                    <div :class="$style.reviewText" v-html="review.text"/>
                    <div :class="$style.reviewAuthor" v-html="review.title"/>
                </div>
            </div>
        </div>

        <VButton
            v-if="slider"
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
                spaceBetween: 100,
                speed: 800,
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
    }

    .review {
        padding: 7rem;
        border-radius: 2rem;
        background: var(--white);
        user-select: none;

        @include respond-to(tablet) {
            padding: 3.6rem;
        }

        @include respond-to(mobile) {
            padding: 1.8rem;
        }
    }

    .reviewText {
        font-family: "Roboto", sans-serif;
        font-size: 2.4rem;
        line-height: 3.6rem;

        @include respond-to(mobile) {
            font-size: 1.8rem;
            line-height: 2.4rem;
        }
    }

    .reviewAuthor {
        position: relative;
        padding-top: 2.3rem;
        padding-left: 7rem;
        font-size: 2.4rem;
        color: var(--grey);

        &:before {
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

        @include respond-to(tablet) {
            padding-left: 5rem;

            &:before {
                width: 3.6rem;
            }
        }

        @include respond-to(mobile) {
            padding-top: 1.2rem;
            padding-left: 4rem;
            font-size: 1.4rem;

            &:before {
                width: 2.4rem;
            }
        }
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
