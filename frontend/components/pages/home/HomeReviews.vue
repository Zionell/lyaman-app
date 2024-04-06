<template>
    <div :class="$style.HomeReviews">
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
                    v-for="review in data"
                    :key="review.id"
                    class="swiper-slide"
                    :class="$style.review"
                >
                    <NuxtImg
                        v-if="image(review)"
                        format="webp"
                        :src="image(review)"
                        alt="Фото отзыва"
                        loading="lazy"
                        placeholder
                        fit="contain"
                        :class="$style.image"
                        provider="strapi"
                    />
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
                slidesPerView: 3,
                spaceBetween: 32,
                speed: 800,
            });
        },

        image(val) {
            return val?.attributes?.image?.data?.attributes?.url;
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
        overflow: hidden;
        display: flex;
        align-items: center;
        width: 35rem;
        height: 35rem;
        user-select: none;
    }

    .image {
        width: 100%;
        height: auto;
        object-fit: contain;
        border-radius: .8rem;
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
