<template>
    <div :class="$style.HomeCertificates">
        <div
            v-for="(cert, ind) in data"
            :key="cert.id"
            :class="[$style.imgWrap, {[$style._odd]: ind % 2 !== 0 }]"
        >
            <nuxt-img
                format="webp"
                :src="cert.image"
                :alt="cert.text"
                loading="lazy"
                :placeholder="15"
                provider="customProvider"
                :class="$style.image"
            />
        </div>
    </div>
</template>

<script>
export default {
    name: 'HomeCertificates',

    props: {
        data: {
            type: Array,
            default: () => [],
        },
    },
};
</script>

<style lang="scss" module>
    .HomeCertificates {
        display: grid;
        gap: 2.4rem;
    }

    .imgWrap {
        max-width: 55%;

        &._odd {
            justify-self: end;
        }
    }
</style>
