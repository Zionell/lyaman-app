<template>
    <svg
        :class="$style.svg"
        viewBox="0 0 16 16"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
    >
        <rect
            v-if="checked"
            width="16"
            height="16"
            rx="4"
            fill="#FABB18"
        />
        <path
            v-if="checked"
            d="M6.50001 9.85761L4.52123 7.87883L4.40001 7.75761L4.27879 7.87883L3.57879 8.57883L3.45758 8.70005L3.57879 8.82127L6.37879 11.6213L6.50001 11.7425L6.62123 11.6213L12.6212 5.62127L12.7424 5.50005L12.6212 5.37883L11.9212 4.67883L11.8 4.55761L11.6788 4.67883L6.50001 9.85761Z"
            fill="white"
            stroke="white"
            stroke-width="0.342857"
        />
        <rect
            v-if="!checked"
            x="1"
            y="1"
            width="14"
            height="14"
            rx="3"
            :stroke="error ? '#ff0000' : '#D5D5D5'"
            stroke-width="2"
        />
    </svg>
</template>

<script>
export default {
    name: 'CheckboxSvg',
    props: {
        checked: {
            type: Boolean,
            default: false,
        },

        error: {
            type: Boolean,
            default: false,
        },
    },
};
</script>

<style lang="scss" module>
    .svg {
        width: 1.6rem;
        height: 1.6rem;
    }
</style>
