<template>
    <div :class="$style.HomeReviews">
        <div class="container">
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
                        <div :class="$style.rewiewImgWrap">
                            <img
                                :class="$style.rewiewImg"
                                src="img/Layer_36.png"
                                alt=""
                            >
                        </div>

                        <div :class="$style.reviewContent">
                            <div :class="$style.reviewText">
                                “Lorem ipsum dolor sit amet, consectetur
                                adipiscing elit, sed do
                                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
                                ad
                                minim veniam, quis nostrud
                                exercitation.”
                            </div>
                            <div :class="$style.reviewAuthor">Joshua Earle</div>

                        </div>
                    </div>
                </div>
                <div
                    ref="pagination"
                    :class="$style.bullets"
                />
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'HomeReviews',

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
                slidesPerView: 2.2,
                speed: 800,

                pagination: {
                    el: this.$refs.pagination,
                    bulletClass: 'bullet',
                    bulletActiveClass: '_active',
                    type: 'bullets',
                },
            });
        },
    },

};
</script>

<style lang="scss" module>
    .HomeReviews {
        //
    }

    .reviews {
        margin: 120px auto 0;
        padding: 70px 0;
        background-color: #f8f8f8;
    }

    .review {
        position: relative;
        text-align: left;
    }

    .rewiew_img {
        position: absolute;
        top: 10%;
        left: 8%;
    }

    .rew_img {
        width: 100%;
        padding: 15px;
        border: 3px solid #95e1d3;
    }

    .reviews-content {
        padding-left: 30%;
    }

    .reviews_text {
        font-family: "Roboto", sans-serif;
        font-size: 24px;
        line-height: 36px;
        color: #999;
    }

    .reviews_author {
        position: relative;
        padding-top: 23px;
        padding-left: 70px;
        font-size: 24px;
        color: #333;
    }

    .reviews_author:before {
        content: "";
        position: absolute;
        top: 65%;
        left: 0;
        display: block;
        width: 60px;
        height: 3px;
        margin-top: 1px;
        background-color: #f38181;
    }
</style>
