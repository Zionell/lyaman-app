<template>
    <div :class="$style.HomeMyWorks">
        <VButton
            :class="[$style.btn, $style._prev]"
            type="slider"
            icon="left"
            :disabled="isAvailable.isBeginning"
            @click="slider.slidePrev()"
        />

        <VButton
            :class="[$style.btn, $style._next]"
            type="slider"
            icon="right"
            :disabled="isAvailable.isEnd"
            @click="slider.slideNext()"
        />
        <div
            ref="slider"
            class="slider"
            :class="$style.slider"
        >
            <div class="swiper-wrapper">
                <div
                    v-for="(slide, idx) in data"
                    :key="idx"
                    class="swiper-slide"
                    :class="$style.work"
                >
                    <div :class="$style.workImgWrap">
                        <img
                            :class="$style.workImg"
                            :src="image(slide.images)"
                            alt="Мои работы"
                        >
                    </div>

                    <div :class="$style.workContent">
                        <h3 :class="$style.workTitle" v-html="slide.title"/>

                        <div :class="$style.workText" v-html="slide.text"/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'HomeMyWorks',

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

    beforeDestroy() {
        this.slider = null;
    },

    methods: {
        initSlider() {
            this.slider = new this.$Swiper(this.$refs.slider, {
                slidesPerView: 1,
                speed: 800,
            });
        },

        image(img) {
            const url = this.$api.baseURL + img;
            return url;
        },
    },
};
</script>

<style lang="scss" module>
    .HomeMyWorks {
        position: relative;
        padding: 0 2rem;
    }

    .slider {
        position: relative;
        overflow: hidden;
    }

    .work {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 3.2rem;

        @include respond-to(tablet) {
            grid-template-columns: 1fr;
            gap: 2.4rem;
        }

        @include respond-to(mobile) {
            gap: 1.2rem;
        }
    }

    .workImgWrap {
        width: 100%;
        height: 100%;

        @include respond-to(tablet) {
            order: 2;
            height: 100%;
            max-height: 70rem;
        }

        @include respond-to(mobile) {
            max-height: 30rem;
        }
    }

    .workImg {
        object-fit: contain;
    }

    .workContent {
        order: 1;
    }

    .workTitle {
        @extend .p24b;

        margin-bottom: 3.2rem;

        @include respond-to(tablet) {
            margin-bottom: 2.4rem;
        }

        @include respond-to(mobile) {
            margin-bottom: 1.2rem;
            font-size: 1.6rem;
        }
    }

    .workText {
        @extend .p16;

        @include respond-to(mobile) {
            font-size: 1.4rem;
        }
    }

    .btn {
        position: absolute;
        top: 35%;
        z-index: 10;
        transform: translateY(-50%);

        &._prev {
            left: 0;

            @include respond-to(mobile) {
                left: -1rem;
            }
        }

        &._next {
            right: 0;

            @include respond-to(mobile) {
                right: -1rem;
            }
        }
    }
</style>
