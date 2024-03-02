<template>
    <div :class="$style.LoaderPage">
        <div :class="$style.heartRate">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                x="0px"
                y="0px"
                viewBox="0 0 150 73"
                enable-background="new 0 0 150 73"
                xml:space="preserve"
            >
                <polyline
                    fill="none"
                    stroke="currentColor"
                    stroke-width="3"
                    stroke-miterlimit="10"
                    points="0,45.486 38.514,45.486 44.595,33.324 50.676,45.486 57.771,45.486 62.838,55.622 71.959,9 80.067,63.729 84.122,45.486 97.297,45.486 103.379,40.419 110.473,45.486 150,45.486"
                />
            </svg>
            <div :class="$style.fadeIn"></div>
            <div :class="$style.fadeOut"></div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'LoaderPage',
};
</script>

<style
    lang="scss"
    module
>
    .LoaderPage {
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 100%;
        background-color: $black;
    }

    .heartRate {
        position: relative;
        width: 25rem;
        height: 14rem;
        margin: 2rem auto;
        color: $blue;
    }

    .fadeIn {
        position: absolute;
        top: 0;
        right: 0;
        width: 100%;
        height: 100%;
        background-color: $black;
        animation: heart-in 2.5s linear infinite;
    }

    .fadeOut {
        position: absolute;
        top: 0;
        left: -120%;
        width: 120%;
        height: 100%;
        background: rgb(0 0 0 / 100%);
        background: linear-gradient(to left, rgb(0 0 0 / 100%) 0%, rgb(0 0 0 / 100%) 50%, rgb(0 0 0 / 0%) 100%);
        background: linear-gradient(to left, rgb(0 0 0 / 100%) 0%, rgb(0 0 0 / 100%) 50%, rgb(0 0 0 / 0%) 100%);
        background: linear-gradient(to left, rgb(0 0 0 / 100%) 0%, rgb(0 0 0 / 100%) 50%, rgb(0 0 0 / 0%) 100%);
        background: linear-gradient(to left, rgb(0 0 0 / 100%) 0%, rgb(0 0 0 / 100%) 50%, rgb(0 0 0 / 0%) 100%);
        background: linear-gradient(to right, rgb(0 0 0 / 100%) 0%, rgb(0 0 0 / 100%) 80%, rgb(0 0 0 / 0%) 100%);
        animation: heart-out 2.5s linear infinite;
    }

    @keyframes heart-in {
        0% {
            width: 100%;
        }

        50% {
            width: 0;
        }

        100% {
            width: 0;
        }
    }

    @keyframes heart-out {
        0% {
            left: -120%;
        }

        30% {
            left: -120%;
        }

        100% {
            left: 0;
        }
    }
</style>
