<template>
    <div :class="$style.VLoader">
        <div></div>
        <div></div>
        <div></div>
        <div></div>
    </div>
</template>

<script>
export default {
    name: 'VLoader',
};
</script>

<style lang="scss" module>
    .VLoader {
        position: relative;
        display: inline-block;
        width: 8rem;
        height: 2.6rem;

        & div {
            position: absolute;
            top: 50%;
            width: 1.3rem;
            height: 1.3rem;
            border-radius: 50%;
            background: $light;
            transform: translateY(-50%);
            animation-timing-function: cubic-bezier(0, 1, 1, 0);
        }

        & div:nth-child(1) {
            left: .8rem;
            animation: lds-ellipsis1 .6s infinite;
        }

        & div:nth-child(2) {
            left: .8rem;
            animation: lds-ellipsis2 .6s infinite;
        }

        & div:nth-child(3) {
            left: 3.2rem;
            animation: lds-ellipsis2 .6s infinite;
        }

        & div:nth-child(4) {
            left: 5.6rem;
            animation: lds-ellipsis3 .6s infinite;
        }
    }

    @keyframes lds-ellipsis1 {
        0% {
            transform: translateY(-50%) scale(0);
        }

        100% {
            transform: translateY(-50%) scale(1);
        }
    }

    @keyframes lds-ellipsis3 {
        0% {
            transform: translateY(-50%) scale(1);
        }

        100% {
            transform: translateY(-50%) scale(0);
        }
    }

    @keyframes lds-ellipsis2 {
        0% {
            transform: translateY(-50%) translate(0, 0);
        }

        100% {
            transform: translateY(-50%) translate(24px, 0);
        }
    }
</style>
