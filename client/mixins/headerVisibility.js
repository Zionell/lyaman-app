export default {
    data() {
        return {
            isVisible: true,
        };
    },

    mounted() {
        document.addEventListener('scroll', this.scroll);
    },

    beforeDestroy() {
        document.removeEventListener('scroll', this.scroll);
    },

    methods: {
        scroll() {
            const height = window.innerHeight - 100;
            const scroll = window.pageYOffset;
            this.isVisible = height >= scroll;
        },
    },
};
