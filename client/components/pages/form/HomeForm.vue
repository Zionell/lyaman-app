<template>
    <section :class="$style.HomeForm">
        <div :class="[$style.wrap, 'container']">
            <div :class="$style.content">
                <h2 :class="$style.title">{{ data.title }}</h2>
                <div :class="$style.text" v-html="data.text"/>
            </div>

            <form :class="$style.form" @submit.prevent="submit">
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

                <VButton>
                    Записаться
                </VButton>
            </form>
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

    methods: {
        async submit() {
            try {
                if (this.checkError()) {
                    return;
                }
                await this.$axios.$post(this.$api.request, {
                    ...this.formInfo,
                });
            } catch (e) {
                console.log(e);
            }
        },

        checkError() {
            let hasError = false;
            const emailRegex = /[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+/gm;

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
    }

    .wrap {
        display: grid;
        grid-template-columns: 1fr 48rem;
        justify-content: space-between;
        gap: 3rem;
    }

    .content {
        max-width: 48rem;
    }

    .title {
        @extend .h1;
    }

    .text {
        @extend .p18;

        color: var(--lightGrey);
    }

    .form {
        display: grid;
        gap: 3rem;
        padding: 3.2rem 2.4rem;
        border: 1px solid var(--border);
        background: var(--white);
        box-shadow: 0 4px 4px rgba(0, 0, 0, .25);
    }
</style>
