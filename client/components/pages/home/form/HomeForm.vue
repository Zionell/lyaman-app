<template>
    <section :class="$style.HomeForm">
        <div :class="[$style.wrap, 'container']">
            <div :class="$style.content">
                <h2 :class="$style.title">Остались вопросы? <br> Заполняй форму!</h2>
            </div>
            <div :class="$style.formWrap">
                <transition name="fade" mode="out-in">
                    <div v-if="isSuccess" :class="$style.formResult">
                        <SvgIcon
                            :class="$style.icon"
                            name="success"
                        />
                        <h3 :class="[$style.resultTitle, 'h4']">Успешно</h3>
                    </div>
                    <div v-else-if="isError" :class="$style.formResult">
                        <SvgIcon
                            :class="$style.icon"
                            name="cross"
                        />
                        <h3 :class="[$style.resultTitle, 'h4']">Ошибка</h3>

                        <VButton
                            round
                            @click="isError = false"
                        >
                            Повторить
                        </VButton>
                    </div>
                    <form
                        v-else
                        :class="$style.form"
                        @submit.prevent="submit"
                    >
                        <VInput
                            v-model="formInfo.name"
                            :error="error.name"
                            label-value="Ваше имя"
                            placeholder="Введите ваше имя"
                        />
                        <VInput
                            v-model="formInfo.email"
                            :error="error.email"
                            label-value="Ваш email"
                            placeholder="Введите ваш email"
                        />
                        <VInput
                            v-model="formInfo.comment"
                            type="textarea"
                            label-value="Комментарий"
                            placeholder="Комментарий ..."
                        />

                        <VButton
                            :is-loading="isLoading"
                            round
                            @click="submit"
                        >
                            Отправить
                        </VButton>
                    </form>
                </transition>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'HomeForm',

    props: {
        data: {
            type: Object,
            default: () => ({}),
        },
    },

    data() {
        return {
            isLoading: false,
            isSuccess: false,
            isError: false,
            timer: null,
            formInfo: {
                name: '',
                email: '',
                comment: '',
            },

            error: {
                name: '',
                email: '',
            },
        };
    },

    beforeDestroy() {
        if (this.timer) {
            clearTimeout(this.timer);
            this.timer = null;
        }
    },

    methods: {
        async submit() {
            try {
                this.isLoading = true;
                if (this.checkError()) {
                    return;
                }
                await this.$axios.$post(this.$api.request, {
                    ...this.formInfo,
                }, {
                    withCredentials: false,
                });
                this.isSuccess = true;
                this.setTimer();
            } catch (e) {
                console.warn(e);
                this.isError = true;
            } finally {
                this.isLoading = true;
            }
        },

        setTimer() {
            this.timer = setTimeout(() => {
                this.isSuccess = false;
            }, 3000);
        },

        checkError() {
            let hasError = false;
            const emailRegex = /[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+/gm;
            this.error = {
                email: '',
                name: '',
            };

            if (!emailRegex.test(this.formInfo.email)) {
                hasError = true;
                this.error.email = 'Неверно заполнено';
            }
            if (!this.formInfo.email) {
                hasError = true;
                this.error.email = 'Обязательное поле';
            }
            if (!this.formInfo.name) {
                hasError = true;
                this.error.name = 'Обязательное поле';
            }

            return hasError;
        },
    },
};
</script>

<style lang="scss" module>
    .HomeForm {
        position: relative;
        padding-top: 10rem;
        padding-bottom: 5rem;

        &:after {
            content: "";
            position: absolute;
            top: 0;
            right: 0;
            left: 0;
            z-index: -1;
            height: 35rem;
            background: var(--secondary);
        }

        @include respond-to(tablet) {
            padding-top: 5rem;
            padding-bottom: 3rem;
        }
    }

    .wrap {
        display: grid;
        grid-template-columns: 1fr 48rem;
        justify-content: space-between;
        gap: 3rem;

        @include respond-to(tablet) {
            grid-template-columns: 1fr;
            gap: 2rem;
        }
    }

    .content {
        max-width: 48rem;

        @include respond-to(tablet) {
            max-width: 50%;
        }

        @include respond-to(mobile) {
            max-width: 65%;
        }
    }

    .title {
        @extend .h3;

        color: var(--white);

        @include respond-to(tablet) {
            font-size: 3.2rem;
        }

        @include respond-to(mobile) {
            font-size: 2.2rem;
        }
    }

    .text {
        @extend .p18;

        color: var(--lightGrey);

        @include respond-to(tablet) {
            font-size: 1.6rem;
        }
    }

    .formWrap {
        height: 50rem;
        padding: 3.2rem 2.4rem;
        border-radius: 3rem;
        border: 1px solid var(--border);
        background: var(--white);
        box-shadow: 0 4px 4px rgba(0, 0, 0, .25);

        @include respond-to(tablet) {
            padding: 2.1rem 1.8rem;
        }
    }

    .formResult {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100%;
    }

    .resultTitle {
        margin: 3.6rem 0;
    }

    .icon {
        width: 7.4rem;
        height: 7.4rem;
        color: var(--primary);
    }

    .form {
        display: grid;
        gap: 3rem;
        height: 100%;

        @include respond-to(tablet) {
            gap: 2rem;
        }
    }
</style>
