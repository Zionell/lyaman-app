export default {
    data() {
        return {
            isVisible: true,
        };
    },

    mounted() {
        if (window?.innerWidth > 1024) {
            document.addEventListener('scroll', this.scroll);
        }
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
