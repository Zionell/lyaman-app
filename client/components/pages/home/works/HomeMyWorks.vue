<template>
    <div :class="$style.HomeMyWorks">
        <div class="container">
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
                        <div :class="$style.workImages">
                            <div
                                v-for="(img, ind) in slide.images"
                                :key="ind"
                                :class="$style.workImgWrap"
                            >
                                <img
                                    :class="$style.workImg"
                                    :src="image(img)"
                                    alt="Мои работы"
                                >
                            </div>
                        </div>

                        <div :class="$style.workContent">
                            <h3 :class="$style.workTitle" v-html="slide.title"/>

                            <div :class="$style.workText" v-html="slide.text"/>
                        </div>
                    </div>
                </div>
                <div :class="$style.btns">
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
        //
    }

    .slider {
        position: relative;
        overflow: hidden;
    }

    .work {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 3rem;
    }

    .workImages {
        position: relative;
        width: 100%;
        height: 100%;
        min-height: 60rem;
    }

    .workImgWrap {
        position: absolute;
        width: 35rem;
        height: auto;

        &:nth-child(1) {
            top: 0;
            right: 0;
            z-index: 3;
        }

        &:nth-child(2) {
            top: 50%;
            left: 0;
            z-index: 2;
            height: 40rem;
            transform: translateY(-50%);
        }

        &:nth-child(3) {
            top: 60%;
            right: -5rem;
            z-index: 3;
            width: 30rem;
            transform: translateY(-50%);
        }
    }

    .workImg {
        object-fit: contain;
    }

    .workTitle {
        @extend .p24b;

        margin-bottom: 3.2rem;
    }

    .workText {
        @extend .p16;
    }

    .btn {
        position: absolute;
        top: 50%;
        z-index: 10;
        transform: translateY(-50%);

        &._prev {
            left: 0;
        }

        &._next {
            right: 0;
        }
    }
</style>
